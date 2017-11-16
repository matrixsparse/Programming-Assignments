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
                "chapter": chapter
            }
            print(data)
            info_list.append(data)
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

        self.novel.insert_many(novel_list)

    def handle(self):
        """
        逻辑处理
        :return: 
        """
        for i in url_list:
            self.get_chapter_links_from(i)

    def get_data(self):
        """
        获取数据
        :return: 
        """
        print('chapter_count:', self.novel.count())
        # novel_list = self.novel.find()
        # for i in novel_list:
        #     print(i)


if __name__ == "__main__":
    s = Spider()
    s.get_data()
