# Linux下安装mongodb

## 下载mongodb

```bash
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-3.4.10.tgz
```

## 解压压缩文件

```bash
tar -zxvf mongodb-linux-x86_64-3.4.10.tgz -C /usr/local/
```

## 文件重命名

```bash
mv mongodb-linux-x86_64-3.4.10 mongodb
```

bin下的mongod就是MongoDB的服务端进程

mongo就是其客户端

其它的命令用于MongoDB的其它用途如MongoDB文件导出

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flhmypkxakj20ro0a675a.jpg)

## 创建目录

```bash
mkdir -p /data/mongodb/mongodb_data/
mkdir -p /data/mongodb/mongodb_log/
```

## 设置MongoDB数据库

```bash
vim /usr/local/mongodb/mongodb.conf
```

```bash
port=27017 # 端口号
dbpath=/data/mongodb/mongodb_data/ #数据库路径
logpath=/data/mongodb/mongodb_log/mongodb.log # 日志输出文件路径
pidfilepath=/usr/local/mongodb/mongo.pid
fork=true # 设置后台运行
logappend=true # 日志输出方式
```

## 启动mongodb

```bash
/usr/local/mongodb/bin/mongod --maxConns 20000 --config /usr/local/mongodb/mongodb.conf
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flhmn1ww6lj20yl02ndfv.jpg)

### 查看mongodb是否启动成功

```bash
netstat -ntlp
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flhmn29rpbj20sd037t8s.jpg)

## 停止mongodb

```bash
/usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.shutdownServer()"
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flhmn29vo3j20w503774d.jpg)

## 查看mongodb状态

```bash
/usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.stats()"
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flhmn23eulj20tr0awdga.jpg)

## 编写脚本管理mongodb

```bash
vim /usr/local/mongodb/mongodb.sh
```

```bash
#!/bin/sh
# @Copyright (C), 2017, matrix

case "$1" in
    start)
        /usr/local/mongodb/bin/mongod --maxConns 20000 --config /usr/local/mongodb/mongodb.conf
    ;;
    status)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.stats()"
    ;;
    stop)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.shutdownServer()"
    ;;
    restart)
        /usr/local/mongodb/bin/mongo localhost:27017/admin --eval "db.shutdownServer()"
        /usr/local/mongodb/bin/mongod --maxConns 20000 --config /usr/local/mongodb/mongodb.conf
    ;;
    *)
        echo "Usage: sh $(basename "$0") {start|status|stop|restart}"
        exit 1
esac
exit 0
```

## mongodb基本操作

```bash
show dbs:显示数据库列表 
show collections：显示当前数据库中的集合（类似关系数据库中的表） 
show users：显示用户
use <db name>：切换当前数据库，这和MS-SQL里面的意思一样 
db.help()：显示数据库操作命令，里面有很多的命令 
db.foo.help()：显示集合操作命令，同样有很多的命令，foo指的是当前数据库下，一个叫foo的集合，并非真正意义上的命令 
db.foo.find()：对于当前数据库中的foo集合进行数据查找（由于没有条件，会列出所有数据） 
db.foo.find( { a : 1 } )：对于当前数据库中的foo集合进行查找，条件是数据中有一个属性叫a，且a的值为1
MongoDB没有创建数据库的命令，但有类似的命令。
如：如果你想创建一个"Test"的数据库，先运行use Test命令，之后就做一些操作（如：db.createCollection('user')）,这样就可以创建一个名叫"myTest"的数据库
```

## 使用supervisor进程管理器启动mongodb
