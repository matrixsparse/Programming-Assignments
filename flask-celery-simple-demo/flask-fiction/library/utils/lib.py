#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import smtplib
import traceback
from email.mime.text import MIMEText
from library.config.development import Config
from library.utils.mail import Mail
from email.mime.multipart import MIMEMultipart


def email_me(subject, content, send_to=None, attch_file=None, images=None):
    """
    发送邮件
    :param subject: str 邮件主题
    :param content: str 邮件内容
    :param send_to: list 收件人列表 ['xxx@gmail.com', 'xxx@qq.com']
    :param attch_file: list or str 邮件附件列表，举例：只有一个附件时：/data/file.zip 或者 ['data/file.zip']，多个附件时：['/data/file1.zip', '/data/file2.zip']
    :param images: dict 邮件内容中加入图片，使用举例：message='picture<br><img src="cid:xxxx">'，images={'xxxx': '/data/pic.png'}，其中，邮件内容里面的xxxx一定要跟images里面的xxxx对应
    :return:
    """
    opts = Config.MAIL_CONFIG
    if send_to and (isinstance(send_to, list) or isinstance(send_to, tuple)):
        opts['send_to'] = ','.join(send_to)
    m = Mail(opts=opts)
    content = content.replace('\n', '<br>')
    try:
        if not m.send_html(subject, content, attch_file, images):
            print('发送邮件失败:subject=%s,content=%s,send_to=%s,attch_file=%s,images=%s' % (
                subject, content, send_to, attch_file, images))
            return False
        return True
    except:
        print('发送邮件失败:err=%s' % (traceback.format_exc(),))
        return False


if __name__ == "__main__":
    email_me('测试邮件', '这是个测试内容！')
