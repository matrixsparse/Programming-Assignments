# data analysis procedure

* 提出想要回答或解决的问题
* 数据再加工[数据采集和数据清理]

```bash
采集相关数据->研究数据，处理研究过程中遇到的问题->数据探索
```

## Numpy和Pandas的一维数据结构

>pandas读取csv

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import pandas as pd

# 1.使用pandas内置read_csv函数读取文件
employment_data = pd.read_csv('employment-above-15.csv')
# 2.查看具体列
print(employment_data['Country'])
# 3.查询去重后的国家数
print(len(employment_data['Country'].unique()))
```

>pandas和numpy的一维数据结构

| Pandas        | Numpy           |
| ------------- |:-------------:| 
| Series        | Array | 
| Series是建立在Numpy数组的基础上，在使用Series之前应该先掌握Numpy数组      | centered      | Numpy是多维的
