# Python装饰器学习之九步入门

## 简单函数，准备附加额外功能

```bash
# -*- coding: utf-8 -*-

"""
示例一：调用两次函数
"""


def myfunc():
    print("myfunc() called.")


myfunc()
myfunc()
```

>运行结果

```bash
myfunc() called.
myfunc() called.
```

## 使用装饰函数在函数执行前和执行后分别附加额外功能

```bash
# -*- coding: utf-8 -*-

"""
示例2：替换函数(装饰)
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句：myfunc = deco(myfunc)
"""


def deco(func):
    print("before myfunc() called.")
    func()
    print("after myfunc() called.")
    return func


def myfunc():
    print("myfunc() called.")


myfunc = deco(myfunc)
myfunc()
myfunc()
```

>运行结果

```bash
before myfunc() called.
myfunc() called.
after myfunc() called.
myfunc() called.
myfunc() called.
```

## 使用语法糖@来装饰函数

```bash
# -*- coding: utf-8 -*-

"""
示例3：使用语法糖@来装饰函数，相当于"myfunc = deco(myfunc)"
但发现新函数只在第一次被调用，且原函数多调用了一次
"""


def deco(func):
    print('before myfunc() called.')
    func()
    print('after myfunc() called.')
    return func


@deco
def myfunc():
    print('myfunc() called.')

myfunc()
myfunc()
```

>运行结果

```bash
before myfunc() called.
myfunc() called.
after myfunc() called.
myfunc() called.
myfunc() called.
```

## 使用内嵌包装函数来确保每次新函数都被调用

```bash
# -*- coding: utf-8 -*-

"""
示例4：使用内嵌包装函数来确保每次新函数都被调用，
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
"""


def deco(func):
    def _deco():
        print('before myfunc() called.')
        func()
        print('after myfunc() called.')
        # 不需要返回func，实际上应返回原函数的返回值
    return _deco


@deco
def myfunc():
    print('myfunc() called.')
    return 'ok'


myfunc()
myfunc()
```

>运行结果

```bash
before myfunc() called.
myfunc() called.
after myfunc() called.
before myfunc() called.
myfunc() called.
after myfunc() called.
```

## 对带参数的函数进行装饰

```bash
# -*- coding: utf-8 -*-

"""
示例5：对带参数的函数进行装饰
内嵌包装函数的形参和返回值与原函数相同，装饰函数返回内嵌包装函数对象
"""


def deco(func):
    def _deco(a, b):
        print('before myfunc() called.')
        ret = func(a, b)
        print('before myfunc() called. result：%s' % ret)
        return ret

    return _deco


@deco
def myfunc(a, b):
    print('myfunc(%s,%s) called.' % (a, b))
    return a + b


myfunc(1, 2)
myfunc(3, 4)
```

>运行结果

```bash
before myfunc() called.
myfunc(1,2) called.
before myfunc() called. result：3
before myfunc() called.
myfunc(3,4) called.
before myfunc() called. result：7
```

## 对参数数量不确定的函数进行装饰

```bash
# -*- coding: utf-8 -*-
"""
示例6：对参数数量不确定的函数进行修饰
参数用(*args,**kwargs)，自动适应变参和命名参数
"""


def deco(func):
    def _deco(*args, **kwargs):
        print('before %s called.' % (func.__name__))
        ret = func(*args, **kwargs)
        print('after %s result = %s' % (func.__name__, ret))
        return ret

    return _deco


@deco
def myfunc(a, b):
    print('myfunc(%s,%s) called.' % (a, b))
    return a + b


@deco
def myfunc2(a, b, c):
    print('myfunc(%s,%s,%s) called.' % (a, b, c))
    return a + b + c


myfunc(1, 2)
myfunc(3, 4)
myfunc2(1, 2, 3)
myfunc2(4, 5, 6)
```

>运行结果

```bash
before myfunc called.
myfunc(1,2) called.
after myfunc result = 3
before myfunc called.
myfunc(3,4) called.
after myfunc result = 7
before myfunc2 called.
myfunc(1,2,3) called.
after myfunc2 result = 6
before myfunc2 called.
myfunc(4,5,6) called.
after myfunc2 result = 15
```

## 让装饰器带参数

```bash
# -*- coding: utf-8 -*-
"""
示例7：让装饰器带参数
"""


def deco(arg):
    def _deco(func):
        def _deco():
            print('before %s called [%s] .' % (func.__name__, arg))
            func()
            print('after %s called [%s] .' % (func.__name__, arg))

        return _deco

    return _deco


@deco('mymodule')
def myfunc():
    print('myfunc() called.')


@deco('module')
def myfunc2():
    print('myfunc2() called.')


myfunc()
myfunc2()
```

>运行结果

```bash
before myfunc called [mymodule] .
myfunc() called.
after myfunc called [mymodule] .
before myfunc2 called [module] .
myfunc2() called.
after myfunc2 called [module] .
```

## 装饰器带类参数

```bash
# -*- coding: utf-8 -*-
"""
示例8：装饰器带类参数
"""


class locker(object):
    def __init__(self):
        print('locker.__init__ should be not called.')

    @staticmethod
    def acquire():
        print('locker.acquire() called.(这是静态方法)')

    @staticmethod
    def release():
        print('locker.release() called.(不需要对象实例)')


def deco(cls):
    """
    cls必须实现acquire()和release()方法
    """

    def _deco(func):
        def _deco():
            print('before %s called [%s].' % (func.__name__, cls))
            cls.acquire()
            try:
                return func
            finally:
                cls.release()

        return _deco

    return _deco


@deco(locker)
def myfunc():
    print('myfunc() called.')


myfunc()
myfunc()
```

>运行结果

```bash
before myfunc called [<class '__main__.locker'>].
locker.acquire() called.(这是静态方法)
locker.release() called.(不需要对象实例)
before myfunc called [<class '__main__.locker'>].
locker.acquire() called.(这是静态方法)
locker.release() called.(不需要对象实例)
```

## 装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器

>mylocker.py

```bash
# -*- coding: utf-8 -*-
"""
示例9：公共类
"""


class mylocker(object):
    def __init__(self):
        print('mylocker.__init__ should be not called.')

    @staticmethod
    def acquire():
        print('mylocker.acquire() called.')

    @staticmethod
    def unlock():
        print('mylocker.unlock() called.')


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print('lockerex.acquire() called.')

    @staticmethod
    def unlock():
        print('lockerex.unlock() called.')


def lockhelper(cls):
    """cls必须实现acquire和release的静态方法"""

    def _deco(func):
        def _deco(*args, **kwargs):
            print('before %s called [%s] .' & (func.__name__, cls))
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return _deco

    return _deco
```

>example.py

```bash
# -*- coding: utf-8 -*-

from application.utils.mylocker import *


class example(object):
    @lockhelper(mylocker)
    def myfunc(self):
        print('myfunc() called.')

    @lockhelper(mylocker)
    @lockhelper(lockerex)
    def myfunc2(self, a, b):
        print('myfunc2() called.')
        return a + b


if __name__ == "__main__":
    a = example()
    a.myfunc()
    print(a.myfunc())
    print(a.myfunc2(1, 2))
    print(a.myfunc2(3, 4))
```

>运行结果

```bash
# -*- coding: utf-8 -*-
"""
示例9：公共类
"""


class mylocker(object):
    def __init__(self):
        print('mylocker.__init__ should be not called.')

    @staticmethod
    def acquire():
        print('mylocker.acquire() called.')

    @staticmethod
    def unlock():
        print('mylocker.unlock() called.\n')


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print('lockerex.acquire() called.')

    @staticmethod
    def unlock():
        print('lockerex.unlock() called.\n')


def lockhelper(cls):
    """cls必须实现acquire和release的静态方法"""

    def _deco(func):
        def _deco(*args, **kwargs):
            print('before %s called [%s] .' % (func.__name__, cls))
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return _deco

    return _deco
```

>运行结果

```bash
before myfunc called [<class 'application.utils.mylocker.mylocker'>] .
mylocker.acquire() called.
myfunc() called.
mylocker.unlock() called.

before myfunc called [<class 'application.utils.mylocker.mylocker'>] .
mylocker.acquire() called.
myfunc() called.
mylocker.unlock() called.

None
before _deco called [<class 'application.utils.mylocker.mylocker'>] .
mylocker.acquire() called.
before myfunc2 called [<class 'application.utils.mylocker.lockerex'>] .
lockerex.acquire() called.
myfunc2() called.
lockerex.unlock() called.

mylocker.unlock() called.

3
before _deco called [<class 'application.utils.mylocker.mylocker'>] .
mylocker.acquire() called.
before myfunc2 called [<class 'application.utils.mylocker.lockerex'>] .
lockerex.acquire() called.
myfunc2() called.
lockerex.unlock() called.

mylocker.unlock() called.

7
```