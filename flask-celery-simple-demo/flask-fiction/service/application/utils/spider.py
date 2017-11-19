#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import time

import pymongo
import requests
from bs4 import BeautifulSoup

url_list = ['http://www.qu.la/book/3952/']

# url_list = ['http://www.qu.la/book/3952/', 'http://www.qu.la/book/16431/', 'http://www.qu.la/book/3137/']

url_addr = 'http://www.qu.la'


class Spider(object):
    def __init__(self):
        """
        配置初始化
        """
        self.client = pymongo.MongoClient('localhost', 27017)
        self.spider = self.client['spider']
        self.section = self.spider['section']
        self.info = self.spider['info']

    def get_chapter_links_from(self, url):
        """
        请求列表页面，获取章节页面地址
        :param url: 
        :return: 
        """
        chapter_list = []

        wb_data = requests.get(url)

        # print(wb_data.text)

        time.sleep(1.5)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        titles = soup.select('#info > h1')
        for i in titles:
            title = i.get_text().strip()
            if callable(s.section.find({'title': title})):
                return {'code': 0, 'data': '已获取 %s 章节数据' % title}

        img_list = soup.select('#fmimg > img')
        for img in img_list:
            img_url = '{}{}'.format(url_addr, img['src'])
        page_chapter_list = soup.select('#list > dl > dd')
        for i in page_chapter_list:
            url = '%s%s' % (url_addr, i.a['href'])
            chapter = i.get_text().strip()
            data = {
                "url": url,
                "title": title,
                "img_url": img_url.strip(),
                "chapter": chapter
            }
            print(data)
            chapter_list.append(data)

        self.section.insert_many(chapter_list)
        self.get_content_from(title)

        soup.decompose()

    def get_content_from(self, title):
        """
        获取章节内容
        :param url: 
        :return: 
        """
        info_list = []

        for info in self.section.find({'title': title}):
            url = info.get('url', '')
            if url:
                wb_data = requests.get(url)

                time.sleep(1.5)
                soup = BeautifulSoup(wb_data.text, 'lxml')
                content = soup.select('#content')
                content = [i.get_text().replace('\xa0', '').replace('\u3000', '') for i in content]

                data = {
                    'title': info.get('title', ''),
                    'chapter': info.get('chapter', ''),
                    'content': content
                }

                # self.novel.insert_one(info)
                info_list.append(data)

        soup.decompose()
        self.info.insert_many(info_list)

    def get_chapter_list(self):
        """
        获取章节列表页数据
        :return: 
        """
        chatper_list = []
        for i in self.section.find({'title': '我是至尊'}):
            title = i.get('title', '')
            img_url = i.get('img_url', '')
            if title:
                chatper_list.append(i.get('chapter', ''))
        result = {
            'title': title,
            'img_url': img_url,
            'chatper': chatper_list
        }
        return result

    def get_content_data(self, title, chapter):
        """
        获取内容页数据
        :return: 
        """
        novel_info = self.info.find_one({'title': title, 'chapter': chapter})
        result = {
            'title': novel_info.get('title'),
            'chapter': novel_info.get('chapter'),
            'content': novel_info.get('content')
        }
        return result

    def update_chapter_data(self, title, source_url):
        """
        更新章节数据
        :param title: 
        :return: 
        """
        if not callable(s.section.find({'title': title})):
            return {'code': 0, 'data': '无法查询到 %s 的章节数据，请抓取章节数据' % title}

        chapter_list = []
        info_list = []
        his_chapter_list = [i.get('chapter') for i in self.section.find({'title': title})]

        wb_data = requests.get(source_url)

        time.sleep(1.5)

        soup = BeautifulSoup(wb_data.text, 'lxml')
        titles = soup.select('#info > h1')
        for i in titles:
            title = i.get_text().strip()
        img_list = soup.select('#fmimg > img')
        for img in img_list:
            img_url = '{}{}'.format(url_addr, img['src'])
        page_chapter_list = soup.select('#list > dl > dd')
        for p in page_chapter_list:
            url = '%s%s' % (url_addr, p.a['href'])
            chapter = p.get_text().strip()
            if chapter not in his_chapter_list:
                data = {
                    "url": url,
                    "title": title,
                    "img_url": img_url.strip(),
                    "chapter": chapter
                }
                chapter_list.append(data)
        self.section.insert_many(chapter_list)

        for c in chapter_list:
            url = c.get('url', '')
            if url:
                wb_data = requests.get(url)

                time.sleep(1.5)
                soup = BeautifulSoup(wb_data.text, 'lxml')
                content = soup.select('#content')
                content = [i.get_text().replace('\xa0', '').replace('\u3000', '') for i in content]

                data = {
                    'title': c.get('title', ''),
                    'chapter': c.get('chapter', ''),
                    'content': content
                }

                # self.novel.insert_one(info)
                info_list.append(data)

        self.section.insert_many(info_list)
        soup.decompose()


if __name__ == "__main__":
    s = Spider()
    s.get_chapter_links_from('http://www.qu.la/book/3952/')
    # s.get_content_from('我是至尊')
    # s.update_chapter_data('我是至尊')
    # s.section.delete_one({'chapter': '第九十章 要可爱,要萌!'})
    # s.info.delete_one({'chapter': '第九十章 要可爱,要萌!'})
    # print(s.novel.count())
    # print([i for i in s.section.find({'chapter': '第九十章 要可爱,要萌!'})])
