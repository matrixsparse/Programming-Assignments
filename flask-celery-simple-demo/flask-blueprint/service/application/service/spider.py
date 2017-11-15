#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


# 为了操作MongoDB数据库，需要引入pymongo库
import pymongo
import urllib.request
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
    def insert_info(url):
        # 请求列表页面，获取页面数据
        wb_data = urllib.request.urlopen(url)
        print(wb_data.read())

        # 开始解析数据，采用lxml解析引擎
        soup = BeautifulSoup(wb_data.read(), 'lxml')
        print(soup)

        # soup.select 得到的列表，变量名最好是复数形式
        titles = soup.select('')


if __name__ == "__main__":
    s = Spider()
    s.insert_info('')
