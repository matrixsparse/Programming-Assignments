#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import time
# 为了操作MongoDB数据库，需要引入pymongo库
import pymongo
import requests
from bs4 import BeautifulSoup


class Spider(object):
    def __init__(self):
        # 连接MongoDB，数据库地址位：localhost，端口号为：27017
        client = pymongo.MongoClient('localhost', 27017)
        # 从MongoDB中选择名称为biquge的数据库
        biquge = client['biquge']
        info = biquge['info']

    # 写解析列表页面的代码，先requests库获取网页数据，在BeatifulSoup解析网页数据
    # 1.把信息插入数据库
    def insert_info(self, url):
        # 请求列表页面，获取页面数据
        wb_data = requests.get(url)

        # print(wb_data.text)

        # 开始解析数据，采用lxml解析引擎
        # 延迟一秒钟，
        time.sleep(1.5)

        # 开始解析网页数据
        soup = BeautifulSoup(wb_data.text, 'lxml')

        # soup.select 得到的列表，变量名最好是复数形式
        titles = soup.select('#info > h1')
        for i in titles:
            print('title：', i.get_text())


if __name__ == "__main__":
    s = Spider()
    s.insert_info('http://www.qu.la/book/16431/')
