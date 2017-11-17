# python变量问题

## locals()

```bash
def test(arg):
    z = 1
    print locals()

test(4)
```

## globals()

```bash
from sys import *
print(globals())
```

## hasattr(object, name)

```bash
判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False
```

```bash
hasattr(t, "name")
```

## getattr(object, name[,default])

```bash
获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选
需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
可以在后面添加一对括号
```

```bash
getattr(t, "age","18")
```

## setattr(object, name, values)

```bash
setattr(t, "age", "18")   #为属相赋值，并没有返回值
```

