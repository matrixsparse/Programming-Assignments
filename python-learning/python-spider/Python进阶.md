# Python进阶

## 函数式编程

```bash
函数：function
函数式：functional，编程范式
```

```bash
函数式编程是一种抽象计算的编程模式
```

```bash
函数不等于函数式，计算不等于计算机
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flop51rah3j20dl099aa1.jpg)

* map()函数

```bash
接收一个函数f和一个list，并通过把函数f依次作用在list的每个元素上，得到一个新的list并返回
```

```bash
map()函数不改变原有的list，而是返回一个新的list
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

def format_name(x):
    return x.upper()


if __name__ == "__main__":
    print([i for i in map(format_name, ['Ada', 'Tom', 'Andy'])])
```

>运行结果

```bash
['ADA', 'TOM', 'ANDY']
```

* reduce()函数

```bash
reduce()传入的函数f必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

from functools import reduce


def fun(x, y):
    return x + y

if __name__ =="__main__":
    print(reduce(fun, [1, 3, 5, 6, 9]))
```

>运行结果

```bash
24
```

* filter()函数

```bash
filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

def is_odd(x):
    return x % 2 == 1


if __name__ == "__main__":
    print([i for i in filter(is_odd, [1, 4, 6, 7, 9, 12, 17])])
```

>运行结果

```bash
[1, 7, 9, 17]
```

* python中自定义排序函数

```bash
sorted()是高阶函数，可以接收一个比较函数来实现自定义排序，传入两个待比较的元素x，y，
如果x应该排在y前面，返回-1
如果x应该排在y后面，返回1
如果x和y相等，返回0
```

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

if __name__ == "__main__":
    print(sorted([35, 6, 12, 34, 55, 21, 9], reverse=False))
```

>运行结果

```bash
[6, 9, 12, 21, 34, 35, 55]
```