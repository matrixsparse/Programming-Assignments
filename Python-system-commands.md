# Python执行系统命令

>Python调用系统执行命令类&方法

* os.system()：无法获得到输出和返回值的
* os.popen()：返回的是 file read 的对象，对其进行读取 read() 的操作可以看到执行的输出，但无法获取返回值
* commands：可以通过getstatusoutput方法获取输出和返回值
* subprocess：可以通过getstatusoutput方法获取输出和返回值

>os模块中的os.system()这个函数来执行shell命令

这个方法得不到shell命令的输出

```bash
os.system('ls')
```

>popen()#这个方法能得到命令执行后的结果是一个字符串，要自行处理才能得到想要的信息

```bash
import os
str = os.popen("ls").read()
a = str.split("\n")
for b in a:
    print b
```

>commands模块#可以很方便的取得命令的输出（包括标准和错误输出）和执行状态位

```bash
import commands
a,b = commands.getstatusoutput('ls')
a是退出状态
b是输出的结果。
>>> import commands
>>> a,b = commands.getstatusoutput('ls')
>>> print a
0
>>> print b
anaconda-ks.cfg
install.log
install.log.syslog
```

>subprocess模块

使用subprocess模块可以创建新的进程，可以与新建进程的输入/输出/错误管道连通，并可以获得新建进程执行的返回状态。使用subprocess模块的目的是替代os.system()、os.popen*()、commands.*等旧的函数或模块。

```bash
import subprocess
1、subprocess.call(command, shell=True)
#会直接打印出结果
2、subprocess.Popen(command, shell=True) 也可以是subprocess.Popen(command, stdout=subprocess.PIPE, shell=True) 这样就可以输出结果了。
如果command不是一个可执行文件，shell=True是不可省略的。
shell=True意思是shell下执行command

这四种方法都可以执行shell命令
```