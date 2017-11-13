# -*- coding: utf-8 -*-

import os

data_arr = [{'parent_id': 1, 'ask_name': '自拍杆',
             'answer_name': '自拍亲，如果您已购买超级QQ会员就可以看的到兑换码， 在当前活动页面里面输入兑换码——填写收货地址——然后下载辣妈帮，在【发现】页底部点击【福利小助手】—— 输入手机号查询是否兑换成功和物流信息 。杆',
             'uid': 1, 'bid': 1},
            {'parent_id': 2, 'ask_name': '育儿指南原入口取消引导',
             'answer_name': '在“辣妈爱看”栏目下，就可以找到您需要的“育儿指南大全”。该帐号还有更多精彩育儿资讯，还等什么，就差你啦 ^^', 'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦身',
             'answer_name': '关于“瘦身”的问题，可以 <a href="http://wx.api.lmbang.com/index.php?c=lmbangIndex&a=search&k=%E7%98%A6%E8%BA%AB">【点击这里查看】</a>',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '减肥',
             'answer_name': '关于“瘦身”的问题，可以 <a href="http://wx.api.lmbang.com/index.php?c=lmbangIndex&a=search&k=%E7%98%A6%E8%BA%AB">【点击这里查看】</a>',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '收腰',
             'answer_name': '关于“瘦身”的问题，可以 <a href="http://wx.api.lmbang.com/index.php?c=lmbangIndex&a=search&k=%E7%98%A6%E8%BA%AB">【点击这里查看】</a>',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦腰',
             'answer_name': '关于“瘦身”的问题，可以 <a href="http://wx.api.lmbang.com/index.php?c=lmbangIndex&a=search&k=%E7%98%A6%E8%BA%AB">【点击这里查看】</a>',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦身',
             'answer_name': '瘦身的概念比减肥来得更健康更理性，因此采取的方式也应该更科学。既然瘦身是在雕塑 完美的体型，那么局部瘦身就是一个很重要的概念，健康有效不容易反弹，也收到广泛的好评',
             'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '减肥',
             'answer_name': '瘦身的概念比减肥来得更健康更理性，因此采取的方式也应该更科学。既然瘦身是在雕塑 完美的体型，那么局部瘦身就是一个很重要的概念，健康有效不容易反弹，也收到广泛的好评',
             'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '收腰',
             'answer_name': '瘦身的概念比减肥来得更健康更理性，因此采取的方式也应该更科学。既然瘦身是在雕塑 完美的体型，那么局部瘦身就是一个很重要的概念，健康有效不容易反弹，也收到广泛的好评',
             'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦腰',
             'answer_name': '瘦身的概念比减肥来得更健康更理性，因此采取的方式也应该更科学。既然瘦身是在雕塑 完美的体型，那么局部瘦身就是一个很重要的概念，健康有效不容易反弹，也收到广泛的好评',
             'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦身', 'answer_name': '想要开始你的节食计划，首先要计算食物的热量。用这种方式你可以测量自己进食了多少卡路里', 'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '减肥', 'answer_name': '想要开始你的节食计划，首先要计算食物的热量。用这种方式你可以测量自己进食了多少卡路里', 'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '收腰', 'answer_name': '想要开始你的节食计划，首先要计算食物的热量。用这种方式你可以测量自己进食了多少卡路里', 'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦腰', 'answer_name': '想要开始你的节食计划，首先要计算食物的热量。用这种方式你可以测量自己进食了多少卡路里', 'uid': 1,
             'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦身', 'answer_name': '科学家发现健康体质人群肠道内有一种叫“约氏乳杆菌”的益生菌的数量远远高于肥胖人群，这种菌直接参与肠道的代谢',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '减肥', 'answer_name': '科学家发现健康体质人群肠道内有一种叫“约氏乳杆菌”的益生菌的数量远远高于肥胖人群，这种菌直接参与肠道的代谢',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '收腰', 'answer_name': '科学家发现健康体质人群肠道内有一种叫“约氏乳杆菌”的益生菌的数量远远高于肥胖人群，这种菌直接参与肠道的代谢',
             'uid': 1, 'bid': 1},
            {'parent_id': 3, 'ask_name': '瘦腰', 'answer_name': '科学家发现健康体质人群肠道内有一种叫“约氏乳杆菌”的益生菌的数量远远高于肥胖人群，这种菌直接参与肠道的代谢',
             'uid': 1, 'bid': 1}]


def save_data_to_cstopic(topic_data=None):
    bot_dir = '/Users/matrix/Desktop/topic/'
    fileName = bot_dir + 'wechattopic.top'
    rule = '\ntopic: ~wechattopic keep repeat ()\r\n\n'
    if os.path.exists(fileName):
        pass
    else:
        if os.path.exists(bot_dir):
            with open(fileName, 'a+') as f:
                f.write(rule)
                for data in topic_data:
                    f.write(data)
        else:
            os.mkdir(bot_dir)
            with open(fileName, 'a+') as f:
                f.write(rule)
                for data in topic_data:
                    f.write(data)


if __name__ == "__main__":
    ask_dict = {}
    answer_dict = {}
    data_list = []
    ask_list = []
    answer_list = []
    for data in data_arr:
        parent_id = 'parent_id:' + str(data.get('bid', '')) + ":" + str(data.get('uid', '')) + ":" + str(
            data.get('parent_id', ''))
        data_list.append(parent_id)
    key = set(data_list)

    for y in key:
        ask_name_key = y + '|ask_name'
        answer_name_key = y + '|answer_name'
        ask_dict.update({ask_name_key: []})
        answer_dict.update({answer_name_key: []})
    # print(ask_dict)
    # print(answer_dict)

    for data in data_arr:
        for y in key:
            parent_id = 'parent_id:' + str(data.get('bid', '')) + ":" + str(data.get('uid', '')) + ":" + str(
                data.get('parent_id', ''))
            ask_name_key = y + '|ask_name'
            answer_name_key = y + '|answer_name'
            if y == parent_id:
                ask_name = ask_dict[ask_name_key]
                ask_name.append('"' + data.get('ask_name', '') + '"')

                answer_name = answer_dict[answer_name_key]
                answer_name.append(data.get('answer_name', ''))
                ask_dict.update({ask_name_key: ask_name})
                answer_dict.update({answer_name_key: answer_name})
    # print(ask_dict)
    # print(answer_dict)

    topic_data = []
    for ask in ask_dict:
        for answer in answer_dict:
            if ask.split('|')[0] == answer.split('|')[0]:
                ask_str = ' '.join(set(ask_dict[ask]))
                answer_str = '[' + ']\n\t['.join(set(answer_dict[answer])) + ']'
                str = 'u: ([' + ask_str + '])' + '\r\n\t' + answer_str + '\r\n\n'
                topic_data.append(str)

    save_data_to_cstopic(topic_data)
