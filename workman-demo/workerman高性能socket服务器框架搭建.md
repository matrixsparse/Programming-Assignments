# workerman高性能socket服务器框架搭建

## 安装Apache服务器

>是否安装Apahce

```bash
apachectl -v
```

>安装Apache

```bash
yum install httpd
```

>启动Apache

```bash
/etc/init.d/httpd start
```

>Apache的默认网站根目录

```bash
/var/www/html
```

>配置文件路径

```bash
/etc/httpd/conf/httpd.conf
```

## 安装workerman依赖

```bash
yum install php-cli php-process git gcc php-devel php-pear libevent-devel -y
```

```bash
pecl install channel://pecl.php.net/libevent-0.1.0 # 提示libevent installation [autodetect]: 按回车
```

```bash
echo extension=libevent.so > /etc/php.d/libevent.ini
```

```bash
service httpd restart  
```

## 下载workman

```bash
git clone https://github.com/walkor/Workerman
```

## 使用HTTP协议对外提供Web服务

### 创建http_test.php【能引用到Workerman/Autoloader.php即可】

>进入目录

```bash
 ~/Workerman/
```

>编辑http_test.php文件

```bash
vim http_test.php
```

>http_test.php

```bash
<?php
use Workerman\Worker;
require_once __DIR__ . '/Autoloader.php';

// 创建一个Worker监听2345端口，使用http协议通讯
$http_worker = new Worker("http://0.0.0.0:2345");

// 启动4个进程对外提供服务
$http_worker->count = 4;

// 接收到浏览器发送的数据时回复hello world给浏览器
$http_worker->onMessage = function($connection, $data)
{
    // 向浏览器发送hello world
    $connection->send('hello world');
};

// 运行worker
Worker::runAll();
```

>启动程序

```bash
php http_test.php start
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9dx0irlkj20no05rt8v.jpg)

>访问浏览器地址栏：http://192.168.3.242:2345/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9dvu8lx6j20ir03uwef.jpg)


## 使用WebSocket协议对外提供服务

### 创建ws_test.php文件

>进入目录

```bash
 ~/Workerman/
```

>创建ws_test.php文件

```bash
vim ws_test.php
```

>ws_test.php

```bash
<?php
use Workerman\Worker;
require_once __DIR__ . '/Autoloader.php';

// 创建一个Worker监听2346端口，使用websocket协议通讯
$ws_worker = new Worker("websocket://0.0.0.0:2346");

// 启动4个进程对外提供服务
$ws_worker->count = 4;

// 当收到客户端发来的数据后返回hello $data给客户端
$ws_worker->onMessage = function($connection, $data)
{
    // 向客户端发送hello $data
    $connection->send('hello ' . $data);
};

// 运行worker
Worker::runAll();
```

>启动服务

```bash
php ws_test.php start
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9e0eunlpj20ns05p74g.jpg)

### 测试

打开chrome浏览器，按F12打开调试控制台，在Console一栏输入(或者把下面代码放入到html页面用js运行)

>清空控制台

```bash
console.clear()
```

```bash
ws = new WebSocket("ws://192.168.3.242:2346");
ws.onopen = function() {
    alert("连接成功");
    ws.send('tom');
    alert("给服务端发送一个字符串：tom");
};
ws.onmessage = function(e) {
    alert("收到服务端的消息：" + e.data);
};
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9e5okgscj214w0efdgk.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9e5ovejvj20x10dx751.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9e5ovu61j20yl0e3q3q.jpg)

## 直接使用TCP传输数据

### 创建ws_test.php文件

>进入目录

```bash
 ~/Workerman/
```

>创建tcp_test.php

```bash
vim tcp_test.php
```

>tcp_test.php

```bash
<?php
use Workerman\Worker;
require_once __DIR__ . '/Autoloader.php';

// 创建一个Worker监听2347端口，不使用任何应用层协议
$tcp_worker = new Worker("tcp://0.0.0.0:2347");

// 启动4个进程对外提供服务
$tcp_worker->count = 4;

// 当客户端发来数据时
$tcp_worker->onMessage = function($connection, $data)
{
    // 向客户端发送hello $data
    $connection->send('hello ' . $data);
};

// 运行worker
Worker::runAll();
```

>启动服务

```bash
php tcp_test.php start
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9hkiu8l4j20ml05rjrj.jpg)

>命令行运行

```bash
telnet 127.0.0.1 2347
Trying 127.0.0.1...
Connected to 127.0.0.1.
Escape character is '^]'.
tom
hello tom
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl9hm35skdj20ls07i0sr.jpg)