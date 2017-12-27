# Php + nginx + Laravel
## 软件版本
```bash
php 7
nginx
Laravel
```
## 安装net-tools
```bash
yum -y install net-tools
```
## 安装仓库
>IUS
```bash
yum install https://centos7.iuscommunity.org/ius-release.rpm
```
IUS仓库里面有我们需要的一些新的软件包，比如 PHP 7。
注意我们安装的是为 CentOS 7 这个系统准备的 IUS 仓库
如果你的系统是 CentOS 6，你需要到 IUS 网站上去查找适合的仓库的下载地址
## 安装Nginx
```bash
yum install nginx -y            #安装nginx
systemctl start nginx            #启动nginx
systemctl enable nginx           #开启自启动
```
## 查看Nginx版本
```bash
nginx -v
```
### 在地址栏访问安装Nginx的服务器的IP地址：http://192.168.153.120/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmvex0c32ij21f80aqt9d.jpg)

## 配置nginx虚拟主机
```bash
虚拟主机允许我们在同一台服务器上运行多个网站，可以为不同的域名绑定不同的目录

访问这个域名的时候，会打开对应目录里面的东西

达到服务器多站点访问的效果
```
```bash
cd /etc/nginx/conf.d
```
```bash
vim test.conf
```
```bash
server {
  listen        80;
  server_name   test.earnp.com;
  root          /var/www/html/;
  index         index.php index.html;

  location / {
    try_files $uri $uri/ /index.php?$query_string;
  }

  location ~ \.php$ {
    fastcgi_pass 0.0.0.0:9000;
    fastcgi_index index.php;
    include fastcgi.conf;
  }
}
```
```bash
注意：try_files $uri $uri/ /index.php?$query_string;
是开启从写路由，其他网页都是404就是重写路由没有开启
第二个Location设置了让虚拟主机可以去处理PHP的请求
```
### 重启nginx或者重新加载nginx
```bash
systemctl reload nginx
```
## 删除php相关安装包
```bash
yum remove php*
```
## PHP7源码编译安装
```bash
nginx能够执行php文件，需要去安装一下php-fpm
```
```bash
[root@node01 ~]# cd /data/server/
[root@node01 server]# wget -c http://cn2.php.net/distributions/php-7.0.5.tar.gz
```
```bash
[root@node01 server]# tar -zxvf php-7.0.5.tar.gz -C ./
```
### 安装php拓展模块
```bash
yum -y install gcc libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel zlib zlib-devel curl curl-devel openssl openssl-devel
```
### configure PHP 7
```bash
./configure --prefix=/data/server/php7 --enable-fpm --with-fpm-user=nginx --with-fpm-group=nginx --with-mysqli --with-zlib --with-curl --with-gd --with-jpeg-dir --with-png-dir --with-freetype-dir --with-openssl --enable-mbstring --enable-xml --enable-session --enable-ftp --enable-pdo -enable-tokenizer --enable-zip
```
### 编译安装
```bash
make
```
```bash
make install
```
```bash
cp php.ini-development /data/server/php7/lib/php.ini
```
### 验证php是否安装成功
```bash
[root@node01 php-7.0.5]# /data/server/php7/bin/php -v
PHP 7.0.5 (cli) (built: Dec 27 2017 17:47:13) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
```
### 查看已经安装的模块
```bash
[root@node01 php-7.0.5]# /data/server/php7/bin/php -m
```
```bash
[PHP Modules]
Core
ctype
curl
date
dom
fileinfo
filter
ftp
gd
hash
iconv
json
libxml
mbstring
mysqli
mysqlnd
openssl
pcre
PDO
pdo_sqlite
Phar
posix
Reflection
session
SimpleXML
SPL
sqlite3
standard
tokenizer
xml
xmlreader
xmlwriter
zip
zlib

[Zend Modules]
```
### 重启php
```bash
systemctl reload php-fpm
```
### 配置php-fpm
```bash
cp /data/server/php7/etc/php-fpm.conf.default /data/server/php7/etc/php-fpm.conf
cp /data/server/php7/etc/php-fpm.d/www.conf.default /data/server/php7/etc/php-fpm.d/www.conf
```
### 配置php环境变量
```bash
vim .bashrc
export PHP_HOME=/data/server/php7
export PATH=$PATH:$PHP_HOME/bin
source .bashrc
```
```bash
[root@node01 ~]# php -v
PHP 7.0.5 (cli) (built: Dec 27 2017 17:47:13) ( NTS )
Copyright (c) 1997-2016 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2016 Zend Technologies
````
### 修改php-fpm.conf文件
```bash
vim /data/server/php7/etc/php-fpm.conf
```
将
```bash
user = nobody
group = nobody
```
改成
```bash
user = root
group = root
```
### 测试php是否安装成功
```bash
vim /var/www/html/test.php
```
```bash
<?php
   phpinfo();
?>
```
