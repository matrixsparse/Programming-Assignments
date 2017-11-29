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
if False:
    print('计算平均值：', employment.mean())
    print('计算全局标准差：', employment.std())
    print('计算方差：', employment.var())
    print('获取最大值：', employment.max())
    print('获取最小值：', employment.min())
    print('获取最大值的索引：', employment.argmax())
    print('获取最小值的索引：', employment.argmin())
    print('计算所有元素累积和：', employment.cumsum())
    print('计算所有元素累积积：', employment.cumprod())
    print('计算总和：', employment.sum())


def max_employment(countries, employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.
    '''
    max_country = countries[employment.argmax()]  # Replace this with your code
    max_value = employment.max()  # Replace this with your code

    return (max_country, max_value)


if __name__ == "__main__":
    print(max_employment(countries, employment))
```

>运行结果

```bash
('Angola', 75.699996949999999)
```

### Numpy向量化运算

| Math Operations        | Logical Operations       | Comparison Operations   |
| ------------- |:-------------:|:-------------:| 
| Add：+        | And：&        | Greater：>        | 
| Subtract ：-        | Or：\|        |  Greater or equal：>=        | 
| Multiply：*        | Not：~        |  Less：<>        | 
| Divide：/        | 如果要进行这些运算，需数组中有布尔值     |  Less or equal：<=        | 
| Exponentiate：**        | 如果你的数组时整数，这些符号的运算就会变成按位与、按位或和按位取反运算      | Equal：==        | 
|         |       | Not equal：!=        | 

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import numpy as np

# numpy中支持向量化运算
# 可以将向量看作为一个数字列表
n1 = np.array([1, 2, 3])
n2 = np.array([4, 5, 6])
# 标量
scalar = 3

# 向量相加
print(n1 + n2)

# 向量乘以标量
print(n1 * scalar)

# 向量相减
print(n2 - n1)
```

### 计算国家整体教育普及率

>如何计算一个国家的整体教育普及率

```bash
female = 97.35583
male = 95.47622

overall = (female + male) / 2
```

假设 女性 和 男性 的教育普及率是这上面两个值

要获得整体的教育普及率,需要把两个值相加并除以2

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix


import numpy as np

# Change False to True for each block of code to see what it does

# Arithmetic operations between 2 NumPy arrays
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([1, 2, 1, 2])

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)

# Arithmetic operations between a NumPy array and a single number
if False:
    a = np.array([1, 2, 3, 4])
    b = 2

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a ** b)

# Logical operations with NumPy arrays
if False:
    a = np.array([True, True, False, False])
    b = np.array([True, False, True, False])

    print(a & b)
    print(a | b)
    print(~a)

    print(a & True)
    print(a & False)

    print(a | True)
    print(a | False)

# Comparison operations between 2 NumPy Arrays
if False:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([5, 4, 3, 2, 1])

    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a == b)
    print(a != b)

# Comparison operations between a NumPy array and a single number
if False:
    a = np.array([1, 2, 3, 4])
    b = 2

    print(a > b)
    print(a >= b)
    print(a < b)
    print(a <= b)
    print(a == b)
    print(a != b)

# First 20 countries with school completion data
countries = np.array([
    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',
    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',
    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',
    'Cambodia', 'Cameroon', 'Cape Verde'
])

# Female school completion rate in 2007 for those 20 countries
female_completion = np.array([
    97.35583, 104.62379, 103.02998, 95.14321, 103.69019,
    98.49185, 100.88828, 95.43974, 92.11484, 91.54804,
    95.98029, 98.22902, 96.12179, 119.28105, 97.84627,
    29.07386, 38.41644, 90.70509, 51.7478, 95.45072
])

# Male school completion rate in 2007 for those 20 countries
male_completion = np.array([
    95.47622, 100.66476, 99.7926, 91.48936, 103.22096,
    97.80458, 103.81398, 88.11736, 93.55611, 87.76347,
    102.45714, 98.73953, 92.22388, 115.3892, 98.70502,
    37.00692, 45.39401, 91.22084, 62.42028, 90.66958
])


def overall_completion_rate(female_completion, male_completion):
    '''
    Fill in this function to return a NumPy array containing the overall
    school completion rate for each country. The arguments are NumPy
    arrays giving the female and male completion of each country in
    the same order.
    '''
    # 用 / 2.，而不是 / 2。
    # 在 Python 2 中，将一个整数除以另一个整数 (2)，会舍去分数。
    # 所以如果输入是整数值，就会丢失信息。因此使用浮点数值 (2.)，我们就能保留结果小数点后的值了
    overall = (female_completion + male_completion) / 2.
    return overall


if __name__ == "__main__":
    print(overall_completion_rate(female_completion, male_completion))
```

### 归一化数据

```bash
在数据分析中，一个常常需要回答的问题是某一个数据点与其他数据点相比有何区别？

例如：美国就业率与其他国家就业率的差异，它比平均值更高还是更低？两者相差多少？

将各数据点转换为相对于平均值的标准偏差值，这叫做数据标准化

比如：2007年的就业数据平均就业率是58.6%，标准偏差是10.5%，美国就业率是62.3%

那么美国就业率和平均就业率之间的差距是3.7%，这约等于0.35个标准偏差，也就是标准偏差的三分之一

而墨西哥2007点的平均就业率约为57.9%，因此墨西哥就业率与平均就业率之间的差距为-0.7%

注意：用负值来表示这个值低于平均值，用正值表示这个值高于平均值

这可以转换为低于平均值0.067个的标准偏差
```

>如何标准化一个单独的数据点

```bash
def standardize_data(values):
    standardize_value = (values - values.mean()) / values.std
    return standardize_value
```

```bash
可以通过减法来计算具体某值与平均值之间的差距

然后 将其除以标准偏差，来将这个结果转换为标准差数量
```

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

# Change this country name to change what country will be printed when you
# click "Test Run". Your function will be called to determine the standardized
# score for this country for each of the given 5 Gapminder variables in 2007.
# The possible country names are available in the Downloadables section.

country_name = 'United States'


# For United States in 2007, the result of calling your function for each variable is:
# employment: 0.349293777492
# female_completion: 0.650689392332
# gdp: 2.01628478851
# life_expectancy: 0.911161638736
# male_completion: 0.518614632009

# For China in 2007, the result of calling your function for each variable is:
# employment: 1.35026042548
# female_completion: No data for China in 2007.
# gdp: -0.502844633532
# life_expectancy: 0.54735759814
# male_completion: No data for China in 2007.

def standardize_data(values):
    '''
    Fill in this function to return a standardized version of the given values,
    which will be in a NumPy array. Each value should be translated into the
    number of standard deviations that value is away from the mean of the data.
    (A positive number indicates a value higher than the mean, and a negative
    number indicates a value lower than the mean.)
    '''
    return (values - values.mean()) / values.std()


if __name__ == "__main__":
    # print(standardize_data(employment))
    print('某国就业率与其他国家就业率的差异')
    for x, y in zip(countries, standardize_data(employment)):
        print(x, "：", y)
```

