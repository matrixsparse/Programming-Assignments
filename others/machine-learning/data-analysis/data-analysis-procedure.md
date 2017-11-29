# data analysis procedure

* 提出想要回答或解决的问题
* 数据再加工[数据采集和数据清理]

```bash
采集相关数据->研究数据，处理研究过程中遇到的问题->数据探索
```

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

## Numpy和Pandas的一维数据结构

| Pandas        | Numpy           |
| ------------- |:-------------:| 
| Series        | Array | 
| Series是建立在Numpy数组的基础上，在使用Series之前应该先掌握Numpy数组      | Numpy是多维的，支持向量运算

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import numpy as np

# First 20 countries with employment data
countries = np.array([
    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',
    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',
    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
    'Belize', 'Benin', 'Bhutan', 'Bolivia',
    'Bosnia and Herzegovina'
])

# Employment data in 2007 for those 20 countries
employment = np.array([
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076
])

# Change False to True for each block of code to see what it does

# Accessing elements
if False:
    print(countries[0])
    print(countries[3])

# Slicing
if False:
    print(countries[0:3])
    print(countries[:3])
    print(countries[17:])
    print(countries[:])

# Element types
if False:
    print(countries.dtype)
    print(employment.dtype)
    print(np.array([0, 1, 2, 3]).dtype)
    print(np.array([1.0, 1.5, 2.0, 2.5]).dtype)
    print(np.array([True, False, True]).dtype)
    print(np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)

# Looping
if False:
    for country in countries:
        print('Examining country {}'.format(country))

    for i in range(len(countries)):
        country = countries[i]
        country_employment = employment[i]
        print('Country {} has employment {}'.format(country,
                                                    country_employment))

# Numpy functions
if True:
    print('计算平均值：', employment.mean())
    print('计算全局标准差：', employment.std())
    print('计算最大值：', employment.max())
    print('计算总和：', employment.sum())


def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    max_country = None  # Replace this with your code
    max_value = None  # Replace this with your code

    return (max_country, max_value)
```

### Numpy向量化运算

| Math Operations        | Logical Operations       | Comparison Operations   |
| ------------- |:-------------:|:-------------:| 
| Add：+        | And：&        | Greater：>        | 
| Subtract ：-        | Or：|        |  Greater or equal：>=        | 
| Multiply：*        | Not：~        |  Less：<>        | 
| Divide：/        | 如果要进行这些运算，需数组中有布尔值     |  Less or equal：<=        | 
| Exponentiate：**        | 如果你的数组时整数，这些符号的运算就会变成按位与、按位或和按位取反运算      | Equal：==        | 
|         |       | Not equal：!=        | 

```bash

```