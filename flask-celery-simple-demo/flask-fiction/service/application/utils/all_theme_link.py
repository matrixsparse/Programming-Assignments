#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import re
import time
import requests
from bs4 import BeautifulSoup
from service.application.utils.mongoqueue import MongoQueue

source_addr = 'http://www.qu.la'
theme_queue = MongoQueue('fiction_list', 'theme_queue')  # 存每一个主题页面的链接
spider_queue = MongoQueue('fiction_list', 'crawl_queue')  # 实例化封装数据库操作这个类，这个表是存每一页书籍的链接的
chapter_queue = MongoQueue('fiction_list', 'chapter_queue')  # 存储章节信息
content_queue = MongoQueue('fiction_list', 'content_queue')  # 存储章节内容


def get_subject_link_from():
    """
    获取类目链接
    :return: 
    """
    wb_data = requests.get(source_addr)
    # 解决python 3.x 使用BeautifulSoup解析中文网页的中文全是乱码问题
    # page.encoding：根据链接头来猜测响应内容的编码方式
    # page.apparent_encoding：会从内容中分析出响应的内容编码方式
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for i in soup.select('#wrapper > div.nav > ul > li > a'):
        if i.get_text().strip() == '首页':
            continue
        if i.get_text().strip() == '永久书架':
            continue
        if i.get_text().strip() == '排行榜单':
            continue
        if i.get_text().strip() == '排行榜单':
            continue
        if i.get_text().strip() == '完本小说':
            continue
        if i.get_text().strip() == '阅读记录':
            continue
        else:
            url = '{}{}'.format(source_addr, i['href'].strip())
            subject = i.get_text().strip()
            theme_queue.push_theme(url, subject)


def get_page_link_from():
    """
    获取类目下文章链接
    :return: 
    """
    for i in theme_queue.find():
        url = i.get('_id')
        wb_data = requests.get(url)
        wb_data.encoding = wb_data.apparent_encoding
        soup = BeautifulSoup(wb_data.text, 'lxml')
        s1_list = soup.find_all('span', attrs={'class': 's1'})
        s2_list = soup.find_all('span', attrs={'class': 's2'})
        s4_list = soup.find_all('span', attrs={'class': 's4'})
        for s1, s2, s4 in zip(s1_list, s2_list, s4_list):
            # print(s1.get_text().replace('[', '').replace(']', ''), s2.get_text(),
            #       '{}{}'.format(source_addr, s2.a['href']), s4.get_text())
            title = s2.get_text().strip()
            author = s4.get_text().strip()
            book_style = s1.get_text().replace('[', '').replace(']', '').strip()
            book_introduction = ''
            book_url = '{}{}'.format(source_addr, s2.a['href'].strip())
            spider_queue.push_book(title, author, book_style, book_introduction, book_url)


def get_chapter_info_from():
    """
    获取章节链接
    :return: 
    """
    for s in spider_queue.find():
        title = s.get('title', '')
        if title:
            url = s.get('_id', '')
            # url = 'http://www.qu.la/book/49807/'
            wb_data = requests.get(url)
            wb_data.encoding = wb_data.apparent_encoding
            soup = BeautifulSoup(wb_data.text, 'lxml')
            img_url = '{}{}'.format(source_addr, soup.select('#fmimg > img'))
            chapter_list = soup.select('#list > dl > dd > a')
            for c in chapter_list:
                print(c)
                chapter_name = c.get_text().strip()
                chapter_url = '{}{}'.format(source_addr, c['href'].strip())
                print('chapter_url：', chapter_url)
                chapter_queue.push_chapter(title, img_url, chapter_name, chapter_url)


def get_content_info_from(url, title, chapter_name):
    """
    获取章节内容
    :return: 
    """
    # url = 'http://www.qu.la/book/29448/10613618.html'
    if url:
        wb_data = requests.get(url)

        time.sleep(1.5)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        content = soup.select('#content')
        content = [i.get_text().replace('\xa0', '').replace('\u3000', '') for i in content]
        content_queue.push_content(title, chapter_name, content)


def get_novel_category_info(skip_num, limit_num):
    """
    获取不同类别下的小说
    :return: 
    """
    novel_list = []
    for novel in spider_queue.find().skip(skip_num).limit(limit_num):
        novel_list.append(novel)

    return {'code': 0, 'result': novel_list}


if __name__ == "__main__":
    # get_subject_link_from()
    # get_page_link_from()
    # get_chapter_info_from()
    # for i in chapter_queue.find():
    #     print(i.get('chapter_url'), i.get('title'), i.get('chapter_name'))
    #     get_content_info_from(i.get('chapter_url'), i.get('title'), i.get('chapter_name'))
    x = 20
    y = 10
    for i in spider_queue.find().skip(x).limit(y):
        print(i)
