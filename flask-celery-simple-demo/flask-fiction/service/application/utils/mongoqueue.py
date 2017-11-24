#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from pymongo import MongoClient, errors
from _datetime import datetime, timedelta


class MongoQueue():
    """
    封装数据库操作：【使用了多线程以及多线程每个进程，需要知道哪些URL已经爬取过了，哪些URL需要爬取】
    """

    def __init__(self, db, collection, timeout=300):
        # 给每个URL设置两种状态
        # 所有初始的URL状态：outstanding【等待爬取的URL】
        # 开始爬取的状态：processing【正在进行的URL】
        # 爬取完成状态：complete【爬取完成的URL】
        # 失败URL重置状态：outstanding
        # 设置计时参数，超过这个值时，将状态重置为outstanding
        self.OUTSTANDING = 1
        self.PROCESSING = 1
        self.COMPLETE = 1
        self.client = MongoClient('localhost', 27017)
        self.Client = self.client[db]
        self.db = self.Client[collection]
        self.timeout = timeout

    def __bool__(self):
        record = self.db.find_one({'status': {'$ne': self.COMPLETE}})
        return True if record else False

    def push_theme(self, url, title):
        """
        添加新URL以及URL主题名进队列
        :param url: 
        :param title: 
        :param number: 
        :return: 
        """
        try:
            self.db.insert({'_id': url, 'status': self.OUTSTANDING, 'subject': title})
            print(url, '插入队列成功中')
        except errors.DuplicateKeyError as e:
            print(title, url, '已经存在队列中')
            pass

    def push_queue(self, url):
        try:
            self.db.insert({'_id': url, 'status': self.OUTSTANDING})
            print(url, '插入队列成功')
        except errors.DuplicateKeyError as e:
            # 插入失败则是已经存在队列了
            print(url, '已经存在队列中')
            pass

    def push_book(self, title, author, book_style, book_introduction, book_url):
        """
        插入书籍数据
        :param title: 
        :param author: 
        :param book_style: 
        :param book_introduction: 
        :param book_url: 
        :return: 
        """
        try:
            self.db.insert(
                {'_id': book_url, 'title': title, 'author': author, 'book_style': book_style,
                 'book_introduction': book_introduction})
            print(title, '书籍队列成功')
        except errors.DuplicateKeyError as e:
            print(title, '数据已经存在队列中')

    def push_chapter(self, title, img_url, chapter_name, chapter_url):
        """
        插入章节数据
        :param title: 
        :param img_url: 
        :param chapter: 
        :param chapter_url: 
        :return: 
        """
        try:
            self.db.insert(
                {'title': title, 'img_url': img_url, 'chapter_name': chapter_name,
                 'chapter_url': chapter_url})
            print(title, '%s数据插入队列成功' % chapter_name)
        except errors.DuplicateKeyError as e:
            print(title, '数据已经存在队列中')

    def push_content(self, title, chapter_name, content):
        """
        插入内容数据
        :param title: 
        :param content: 
        :return: 
        """
        try:
            self.db.insert(
                {'title': title, 'chapter_name': chapter_name, 'content': content})
            print(title, '%s 插入章节内容数据 成功' % (chapter_name))
        except errors.DuplicateKeyError as e:
            print(title, '数据已经存在队列中')

    def select(self):
        record = self.db.find_and_modify(query={'status': self.OUTSTANDING},
                                         update={'$set': {'status': self.PROCESSING, 'timestamp': datetime.now()}})
        if record:
            return record['_id']
        else:
            self.repair()
            raise KeyError

    def repair(self):
        record = self.db.find_and_modify(query={'timestamp': {'$lt': datetime.now() - timedelta(seconds=self.timeout)},
                                                'status': {'$ne': self.COMPLETE}
                                                },
                                         update={'$set': {'status': self.OUTSTANDING}})  # 超时时要更改状态
        if record:
            print('重置URL', record['_id'])

    def complete(self, url):
        self.db.update({'_id': url}, {'$set': {'status': self.COMPLETE}})

    def find(self):
        """
        返回查询结果
        :return: 
        """
        return self.db.find()

    def find_book_style(self, book_style):
        """
        返回查询结果
        :return: 
        """
        return self.db.find({'book_style': book_style})

    def count(self):
        """
        返回查询结果
        :return: 
        """
        return self.db.count()


if __name__ == "__main__":
    pass
