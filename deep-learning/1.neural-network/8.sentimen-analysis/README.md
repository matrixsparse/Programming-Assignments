# sentiment analysis

深度学习就是一套工具，根据已知的数据，通过使用神经网络，预测我们想要知道的事物

```bash
自然语言处理就是对人类语言的研究，使用一系列工具，如机器学习

将学习情感分类，这种分类能够判断人类生成的一段文字是正面或是负面的

所以在此情况下，我们已知一段人类生成的语言文本，想要预测的是这些正面或负面标签之一
```

神经网络所做的唯一的事情就是搜索两个数据集之间直接或间接的`相关性`

```bash
为了让神经网络来做训练，我们需要给它提供2个有意义的数据集

第一个数据集必须代表我们已知的信息
第二个数据集必须代表我们想要知道的信息

随着网络不断训练，它将不断寻找两组数据集之间的相关性
最终能够根据一组的输入，预测另一组的数值
```

* Sentiment_Classification_Projects.ipynb - 这个迷你项目的 notebook，你会用它来练习和完成迷你项目。
* Sentiment_Classification_Solutionss.ipynb - 含有 Andrew 对课程迷你项目解决方案的 notebook，可供你参考
* reviews.txt - 含有 25000 条影评
* labels.txt - 针对 reviews.txt 中的影评的 positive/negative 情感标签

```bash
将加载入一组IMDB的电影评论

这些标签与评论一一对应

人们给电影从一星到五星打分

我们简化成了正面评价：高于三星，负面评价：低于三星
```

## 激活 python3 conda 环境

```bash
[root@sparsematrix ~]# conda create --name sentiment-analysis python=3.6
```

### 进入新环境

```bash
source activate sentiment-analysis
```

## 安装 numpy、jupyter、notebook、matplotlib、scikit-learn、bokeh

```bash
conda install numpy jupyter notebook matplotlib scikit-learn bokeh
```

## 下载项目

```bash
git clone https://github.com/udacity/cn-deep-learning.git
```

```bash
cd cn-deep-learning/tutorials/sentiment-network
```

## 启动 Jupyter notebook 服务器

```bash
jupyter notebook Sentiment_Classification_Projects.ipynb --ip=0.0.0.0
```

## 打开 Sentiment_Classification_Projects.ipynb

>在浏览器地址栏访问

```bash
http://服务器ip:8888/notebooks/Sentiment_Classification_Projects.ipynb
```

## 退出环境

```bash
source deactivate
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2018, matrix

from collections import Counter
import numpy as np


# 加载数据集
def pretty_print_review_and_label(i):
    print(labels[i] + "\t:\t" + reviews[i][:80] + "...")


# 加载 25000 条影评
g = open('/data/server/cn-deep-learning/tutorials/sentiment-network/reviews.txt', 'r')  # What we know!
reviews = list(map(lambda x: x[:-1], g.readlines()))
print("--------------- 影评 start -----------------")
# print(reviews)
# 查看影评数据条数
print('查看影评数据条数：', len(reviews))
print("--------------- end 影评 -----------------")
g.close()

# 加载针对 reviews.txt 中的影评的 positive/negative 情感标签
g = open('/data/server/cn-deep-learning/tutorials/sentiment-network/labels.txt', 'r')  # What we WANT to know!
labels = list(map(lambda x: x[:-1].upper(), g.readlines()))
print("--------------- 情感标签 start -----------------")
print('查看情感标签：', labels[0])
print("--------------- end 情感标签 -----------------")
g.close()

# 查看影评数据及情感标签
print("--------------- 查看影评数据及情感标签 start -----------------")
print("labels.txt \t : \t reviews.txt\n")
pretty_print_review_and_label(2137)
pretty_print_review_and_label(12816)
pretty_print_review_and_label(6267)
pretty_print_review_and_label(21934)
pretty_print_review_and_label(5297)
pretty_print_review_and_label(4998)
print("--------------- end 查看影评数据及情感标签 -----------------")

# 统计positive影评条数、negative影评条数、所有打标签的影评数据
# Create three Counter objects to store positive, negative and total counts
positive_counts = Counter()
negative_counts = Counter()
total_counts = Counter()

# 开始计算
for i in range(len(reviews)):
    if (labels[i] == 'POSITIVE'):
        # print(labels[i])
        # print(reviews[i])
        for word in reviews[i].split(" "):
            positive_counts[word] += 1
            total_counts[word] += 1
    else:
        for word in reviews[i].split(" "):
            negative_counts[word] += 1
            total_counts[word] += 1

# print(total_counts)

# Examine the counts of the most common words in positive reviews
print('----------------------- 打印 positive 词词频 start -----------------------------')
print(positive_counts.most_common())
print('----------------------- end 打印 positive 词词频 -----------------------------')

# Examine the counts of the most common words in negative reviews
print('----------------------- 打印 negative 词词频 start -----------------------------')
print(negative_counts.most_common())
print('----------------------- end 打印 negative 词词频 -----------------------------')

# Create Counter object to store positive/negative ratios
pos_neg_ratios = Counter()

# TODO: Calculate the ratios of positive and negative uses of the most common words
#       Consider words to be "common" if they've been used at least 100 times
# pos_neg_ratios[word] = positive_counts[word] / float(negative_counts[word]+1)
```

单个单词比整个评论更能对正负标签作出预测
现在，要将数据集转换成数字，运用刚刚的理论和思想
让神经网络以这种特定的方式来寻找相关性，传入神经网络，使其能够寻找相关性并做出正确的正负预测

对每个单词计数，将这些计数作为输入值传入神经网络
这些数值与你预测的结果具有相关性，就预测正标签和父标签来说
神经网络还无法直接根据单词预测正负
我们的做法是以数字的形式代表"正"和"负"

数字1代表正，数字0代表负