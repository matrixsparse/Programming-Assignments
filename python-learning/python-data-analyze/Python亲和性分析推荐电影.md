# Python亲和性分析推荐电影

## 下载数据

```bash
http://grouplens.org/datasets/movielens
```

## 用pandas加载数据

```bash
# -*- coding: utf-8 -*-
import os
import pandas as pd

# 1.获取数据集
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml-100k')
ratings_filename = os.path.join(data_folder, 'u.data')
print(ratings_filename)

# 2.用pandas加载数据
# 设置第一行不为header、分隔符
all_ratings = pd.read_csv(ratings_filename, delimiter='\t', header=None,
                          names=['UserID', 'MovieID', 'Rating', 'Datetime'])

# 解析时间戳数据
all_ratings['Datetime'] = pd.to_datetime(all_ratings['Datetime'], unit='s')

# print(all_ratings)
# print('解析时间戳数据：\n',)
print('查看前五条记录：\n', all_ratings[:5])
```

>运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkow9i0tl0j20rs0mhdhs.jpg)

```bash
上述图表，表示用户#196在1997-12-04 15:55:49为电影#242打了3分(满分是5分)
```

## Apriori算法的实现

```bash
数据挖掘的目标：如果用户喜欢某些电影，那么他们也会喜欢这部电影
```

```bash
要确定用户是不是喜欢某一部电影，因此创建新特征Favorable，若用户喜欢该电影，值为true
```

```bash
# -*- coding: utf-8 -*-
import os
import pandas as pd

# 1.获取数据集
data_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ml-100k')
ratings_filename = os.path.join(data_folder, 'u.data')
print(ratings_filename)

# 2.用pandas加载数据
# 设置第一行不为header、分隔符
all_ratings = pd.read_csv(ratings_filename, delimiter='\t', header=None,
                          names=['UserID', 'MovieID', 'Rating', 'Datetime', 'Favorable'])

# 解析时间戳数据
all_ratings['Datetime'] = pd.to_datetime(all_ratings['Datetime'], unit='s')

# print(all_ratings)
# print('解析时间戳数据：\n',)

all_ratings['Favorable'] = all_ratings['Rating'] > 3

# print('查看前五条记录：\n', all_ratings[:5])

# 抽取一部分数据做训练集
ratings = all_ratings[all_ratings['UserID'].isin(range(200))]

# print(ratings)

# 新建数据集，只包括用户喜欢某部电影的数据行
favorable_ratings = ratings[ratings["Favorable"]]

# 把v.values存储为frozenset，便于快速判断用户是否为某部电影打过分，集合比列表速度快
favorable_reviews_by_users = dict((k, frozenset(v.values)) for k, v in favorable_ratings.groupby("UserID")["MovieID"])

# 创建一个数据框，以便了解每部电影的影迷数量
num_favorable_by_movie = ratings[["MovieID", "Favorable"]].groupby("MovieID").sum()

# 查看最受欢迎的五部电影
print(num_favorable_by_movie.sort("Favorable", ascending=False)[:5])
```

>运行结果

```bash
MovieID   Favorable        
50           100.0
100           89.0
258           83.0
181           79.0
174           74.0
```
