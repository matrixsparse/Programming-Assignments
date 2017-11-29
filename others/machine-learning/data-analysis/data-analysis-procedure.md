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
| Multiply：*        | Not：~        |  Less：<        | 
| Divide：/        | 如果要进行这些运算，需数组中有布尔值     |  Less or equal：<=        | 
| Exponentiate：**        | 如果你的数组是整数，这些符号的运算就会变成按位与、按位或和按位取反运算      | Equal：==        | 
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

### NumPy索引数组

```bash
当你有两个长度相同的Numpy数组时，还可以进行另一种计算

Numpy数组需含有布尔值，第一个数组可包含任何类型的数据，不仅仅是数字

例如：

假设你的第一个数组 a 包含 1、2、3、4和5 

你的第二个数组b 包含 布尔值 FFTTT

那么a[b]将返回，包含元素3、4、5的较短数组

第二个数组被称为索引数组，它告诉你应保留第一个数组的哪些元素

在这里 我们没有保留1 因为这一项是假值

我们没有保留2 因为它是假值

但我们保留了3、4、5，因为它是真值

当你把它与之前的向量运算相结合后，它的用处是很大的

在这个例子中，保留了大于2的所有值

所以，可以用代码b = a > 2来创建布尔数组b
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import numpy as np

# Change False to True for each block of code to see what it does

# Using index arrays
if False:
    a = np.array([1, 2, 3, 4])
    b = np.array([True, True, False, False])

    print(a[b])
    print(a[np.array([True, False, True, False])])

# Creating the index array using vectorized operations
if False:
    a = np.array([1, 2, 3, 2, 1])
    b = (a >= 2)

    print(b)
    print(a[b])
    print(a[a >= 2])

# Creating the index array using vectorized operations on another array
if False:
    a = np.array([1, 2, 3, 4, 5])
    b = np.array([1, 2, 3, 2, 1])

    print(b == 2)
    print(a[b == 2])


def mean_time_for_paid_students(time_spent, days_to_cancel):
    '''
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).

    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    
    注销前至少注册7天的学生上课时间
    '''
    # 注销前至少注册7天的学生为True，否则为False
    return time_spent[days_to_cancel >= 7].mean()


# Time spent in the classroom in the first week for 20 students
time_spent = np.array([
    12.89697233, 0., 64.55043217, 0.,
    24.2315615, 39.991625, 0., 0.,
    147.20683783, 0., 0., 0.,
    45.18261617, 157.60454283, 133.2434615, 52.85000767,
    0., 54.9204785, 26.78142417, 0.
])

# Days to cancel for 20 students
days_to_cancel = np.array([
    4, 5, 37, 3, 12, 4, 35, 38, 5, 37, 3, 3, 68,
    38, 98, 2, 249, 2, 127, 35
])

if __name__ == "__main__":
    print(mean_time_for_paid_students(time_spent, days_to_cancel))
```

### Pandas Series

```bash
Series 与 Numpy数组类似

比如：如果你有一个名为s的Series

那么s.describe函数可以打出平均值，标准偏差，中位数以及与Series有关的其他统计数据

Numpy数据没有这个函数

Series还有一些其他优于数组的地方
```

```bash
def variable_correlation(variable1,variable2):
    both_above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    both_below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    is_same_direction = ''
    num_same_direction = ''
```

```bash
首先要计算出有多少组数据点，相对其平均值的方向相同

也就是 两者都高于或都低于平均值
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import pandas as pd

countries = ['Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda',
             'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan',
             'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus',
             'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia']

life_expectancy_values = [74.7, 75., 83.4, 57.6, 74.6, 75.4, 72.3, 81.5, 80.2,
                          70.3, 72.1, 76.4, 68.1, 75.2, 69.8, 79.4, 70.8, 62.7,
                          67.3, 70.6]

gdp_values = [1681.61390973, 2155.48523109, 21495.80508273, 562.98768478,
              13495.1274663, 9388.68852258, 1424.19056199, 24765.54890176,
              27036.48733192, 1945.63754911, 21721.61840978, 13373.21993972,
              483.97086804, 9783.98417323, 2253.46411147, 25034.66692293,
              3680.91642923, 366.04496652, 1175.92638695, 1132.21387981]

# Life expectancy and gdp data in 2007 for 20 countries
life_expectancy = pd.Series(life_expectancy_values)
gdp = pd.Series(gdp_values)

# Change False to True for each block of code to see what it does

# Accessing elements and slicing
if False:
    print(life_expectancy[0])
    print(gdp[3:6])

# Looping
if False:
    for country_life_expectancy in life_expectancy:
        print('Examining life expectancy {}'.format(country_life_expectancy))

# Pandas functions
if False:
    print(life_expectancy.mean())
    print(life_expectancy.std())
    print(gdp.max())
    print(gdp.sum())

# Vectorized operations and index arrays
if False:
    a = pd.Series([1, 2, 3, 4])
    b = pd.Series([1, 2, 1, 2])

    print(a + b)
    print(a * 2)
    print(a >= 3)
    print(a[a >= 3])


def variable_correlation(variable1, variable2):
    '''
    Fill in this function to calculate the number of data points for which
    the directions of variable1 and variable2 relative to the mean are the
    same, and the number of data points for which they are different.
    Direction here means whether each value is above or below its mean.

    You can classify cases where the value is equal to the mean for one or
    both variables however you like.

    Each argument will be a Pandas series.

    For example, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([4, 5, 6, 7]), then the output would be (4, 0).
    This is because 1 and 4 are both below their means, 2 and 5 are both
    below, 3 and 6 are both above, and 4 and 7 are both above.

    On the other hand, if the inputs were pd.Series([1, 2, 3, 4]) and
    pd.Series([7, 6, 5, 4]), then the output would be (0, 4).
    This is because 1 is below its mean but 7 is above its mean, and
    so on.
    '''
    both_above = (variable1 > variable1.mean()) & (variable2 > variable2.mean())
    both_below = (variable1 < variable1.mean()) & (variable2 < variable2.mean())
    is_same_direction = both_above | both_below
    num_same_direction = is_same_direction.sum()
    num_different_direction = len(variable1) - num_same_direction

    return (num_same_direction, num_different_direction)


if __name__ == "__main__":
    print(variable_correlation(pd.Series([1, 2, 3, 4]), pd.Series([4, 5, 6, 7])))
```

### Series索引

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix
import pandas as pd

countries = [
    'Afghanistan', 'Albania', 'Algeria', 'Angola',
    'Argentina', 'Armenia', 'Australia', 'Austria',
    'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh',
    'Barbados', 'Belarus', 'Belgium', 'Belize',
    'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
]

employment_values = [
    55.70000076, 51.40000153, 50.5, 75.69999695,
    58.40000153, 40.09999847, 61.5, 57.09999847,
    60.90000153, 66.59999847, 60.40000153, 68.09999847,
    66.90000153, 53.40000153, 48.59999847, 56.79999924,
    71.59999847, 58.40000153, 70.40000153, 41.20000076,
]

# Employment data in 2007 for 20 countries
employment = pd.Series(employment_values, index=countries)


def max_employment(employment):
    '''
    Fill in this function to return the name of the country
    with the highest employment in the given employment
    data, and the employment in that country.

    The input will be a Pandas series where the values
    are employment and the index is country names.

    Try using the Pandas idxmax() function. Documention can
    be found here:
    http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.idxmax.html
    '''
    # 获取最大值
    max_country = employment.argmax()
    # 获取指定索引的值
    max_value = employment.loc[employment.argmax()]

    return (max_country, max_value)


if __name__ == "__main__":
    print(max_employment(employment))
```

>运行结果

```bash
('Angola', 75.699996949999999)
```

### pandas向量化运算和Series索引

```bash
当你将两个Numpy数组相加时，由于没有索引，你相加的是同一位置的元素

就目前的这些Series而言，它们的位置和索引值都是一样的，如果情况有变，你认为会发生什么？

如果根据索引，而不是位置来进行加法虞世南，又会怎样？

如果你把两个索引值不同的Series相加呢？
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import pandas as pd

# Change False to True for each block of code to see what it does

# Addition when indexes are the same
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
    print(s1 + s2)

# Indexes have same elements in a different order
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['b', 'd', 'a', 'c'])
    print(s1 + s2)

# Indexes overlap, but do not have exactly the same elements
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
    print(s1 + s2)

# Indexes do not overlap
if False:
    s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
    s2 = pd.Series([10, 20, 30, 40], index=['e', 'f', 'g', 'h'])
    print(s1 + s2)
```

### 填充缺失值

```bash
如果把两个索引值不同的Series相加，其结果就是NaN

但在大多数情况下，可能不希望输出的Series中出现NaN或非数字

怎么样才能使结果中不出现NaN？

使用Series的dropna函数，消除部分或全部缺失数据标签
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])


# Try to write code that will add the 2 previous series together,
# but treating missing values from either series as 0. The result
# when printed out should be similar to the following line:
# print pd.Series([1, 2, 13, 24, 30, 40], index=['a', 'b', 'c', 'd', 'e', 'f'])

def method01(s1, s2):
    sum_result = s1 + s2
    return sum_result.dropna()


def method02(s1, s2):
    return s1.add(s2, fill_value=0)


if __name__ == "__main__":
    print('--------------------- method01 start ---------------------------------')
    print(method01(s1, s2))
    print('--------------------- end method01 ---------------------------------')
    print('--------------------- method02 start ---------------------------------')
    print(method02(s1, s2))
    print('--------------------- end method02 ---------------------------------')
```

>运行结果

```bash
--------------------- method01 start ---------------------------------
c    13.0
d    24.0
dtype: float64
--------------------- end method01 ---------------------------------
--------------------- method02 start ---------------------------------
a     1.0
b     2.0
c    13.0
d    24.0
e    30.0
f    40.0
dtype: float64
--------------------- end method02 ---------------------------------
```

### Pandas Series Apply()

apply主要应用在没有Series内置函数的时候

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import pandas as pd

# Change False to True to see what the following block of code does

# Example pandas apply() usage (although this could have been done
# without apply() using vectorized operations)
if False:
    s = pd.Series([1, 2, 3, 4, 5])


    def add_one(x):
        return x + 1


    print(s.apply(add_one))

names = pd.Series([
    'Andre Agassi',
    'Barry Bonds',
    'Christopher Columbus',
    'Daniel Defoe',
    'Emilio Estevez',
    'Fred Flintstone',
    'Greta Garbo',
    'Humbert Humbert',
    'Ivan Ilych',
    'James Joyce',
    'Keira Knightley',
    'Lois Lane',
    'Mike Myers',
    'Nick Nolte',
    'Ozzy Osbourne',
    'Pablo Picasso',
    'Quirinus Quirrell',
    'Rachael Ray',
    'Susan Sarandon',
    'Tina Turner',
    'Ugueth Urbina',
    'Vince Vaughn',
    'Woodrow Wilson',
    'Yoji Yamada',
    'Zinedine Zidane'
])


def reverse_names(name):
    '''
    Fill in this function to return a new series where each name
    in the input series has been transformed from the format
    "Firstname Lastname" to "Lastname, FirstName".

    Try to use the Pandas apply() function rather than a loop.
    '''
    name_split = name.split(' ')
    Lastname = name_split[1]
    FirstName = name_split[0]
    return Lastname + ", " + FirstName


if __name__ == "__main__":
    print(names.apply(reverse_names))
```

### 在Pandas中绘图

如果变量 data 是一个 NumPy 数组或 Pandas Series，就像它是一个列表一样

```bash
import matplotlib.pyplot as plt
plt.hist(data)
```

```bash
Pandas 还有在后台使用 matplotlib 的内置绘图函数，因此如果 data 是一个 Series，你可以使用 data.hist() 创建直方图

有时候 Pandas 封装器更加方便

例如，你可以使用 data.plot() 创建 Series 的线条图

Series 索引被用于 x 轴，值被用于 y 轴
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import pandas as pd
import seaborn as sns

# The following code reads all the Gapminder data into Pandas DataFrames. You'll
# learn about DataFrames next lesson.

path = '/datasets/ud170/gapminder/'
employment = pd.read_csv(path + 'employment_above_15.csv', index_col='Country')
female_completion = pd.read_csv(path + 'female_completion_rate.csv', index_col='Country')
male_completion = pd.read_csv(path + 'male_completion_rate.csv', index_col='Country')
life_expectancy = pd.read_csv(path + 'life_expectancy.csv', index_col='Country')
gdp = pd.read_csv(path + 'gdp_per_capita.csv', index_col='Country')

# The following code creates a Pandas Series for each variable for the United States.
# You can change the string 'United States' to a country of your choice.

employment_us = employment.loc['United States']
female_completion_us = female_completion.loc['United States']
male_completion_us = male_completion.loc['United States']
life_expectancy_us = life_expectancy.loc['United States']
gdp_us = gdp.loc['United States']

# Uncomment the following line of code to see the available country names
# print employment.index.values

# Use the Series defined above to create a plot of each variable over time for
# the country of your choice. You will only be able to display one plot at a time
# with each "Test Run".

if __name__ == "__main__":
    pass
```