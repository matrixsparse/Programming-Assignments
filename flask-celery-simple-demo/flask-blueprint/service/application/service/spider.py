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
        self.novel = self.spider['novel']

    def get_chapter_links_from(self, url):
        """
        请求列表页面，获取章节页面地址
        :param url: 
        :return: 
        """

        info_list = []

        wb_data = requests.get(url)

        # print(wb_data.text)

        time.sleep(1.5)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        titles = soup.select('#info > h1')
        for i in titles:
            title = i.get_text()
        chapter_list = soup.select('#list > dl > dd')
        for i in chapter_list:
            url = '%s%s' % (url_addr, i.a['href'])
            chapter = i.get_text()
            data = {
                "url": url,
                "title": title,
                "chapter": chapter.strip()
            }
            print(data)
            info_list.append(data)
        soup.decompose()
        self.get_content_from(info_list)

    def get_content_from(self, info_list):
        """
        获取内容页面内容
        :param url: 
        :return: 
        """
        novel_list = []

        for info in info_list:
            url = info.get('url', '')
            if url:
                wb_data = requests.get(url)

                time.sleep(1.5)
                soup = BeautifulSoup(wb_data.text, 'lxml')
                content = soup.select('#content')
                content = [i.get_text().replace('\xa0', '').replace('\u3000', '') for i in content]

                info['content'] = content

                # self.novel.insert_one(info)
                novel_list.append(info)

        soup.decompose()
        self.novel.insert_many(novel_list)

    def get_chapter_data(self):
        """
        获取章节列表页数据
        :return: 
        """
        chatper_list = []
        for i in self.novel.find({'title': '我是至尊'}):
            title = i.get('title', '')
            if title:
                chatper_list.append(i.get('chapter', ''))
        result = {
            'title': title,
            'chatper': chatper_list
        }
        return result

    def get_content_data(self, title, chapter):
        """
        获取内容页数据
        :return: 
        """
        novel_info = self.novel.find_one({'title': title, 'chapter': chapter})
        result = {
            'title': novel_info.get('title'),
            'chapter': novel_info.get('chapter'),
            'content': novel_info.get('content')
        }
        return result


if __name__ == "__main__":
    s = Spider()
    s.get_content_data('我是至尊', ' 第一章 兄弟情义莫论酒,男儿行世必拔刀!')
