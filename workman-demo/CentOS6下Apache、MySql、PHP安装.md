## 更新yum源
```bash
由于默认的yum源是国外服务器，所以使用yum命令安装软件时会等待很久，且默认源上的软件不是最新的
```
>备份yum源
```bash
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```
>安装yum源
```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-6.repo
```
>生成缓存
```bash
yum makecache
```
## 安装Apache服务器
>是否安装Apahce
```bash
apachectl -v
```
>安装Apache
```bash
yum install httpd
```
or
```bash
yum install httpd.x86_64
```
>启动Apache
```bash
/etc/init.d/httpd start
```
or
```bash
apachectl start
```
>Apache的默认网站根目录
```bash
/var/www/html
```
>配置文件路径
```bash
/etc/httpd/conf/httpd.conf
```
>更改apache默认网站目录
```bash
vim /etc/httpd/conf/httpd.conf
```
找到 DocumentRoot “/data/website/html” 这一段 #apache的根目录
把/var/www/html 这个目录改为/data/website/html
>查看apache服务状态
```bash
systemctl status httpd.service
```
>SSH异常“Failed to start OpenSSH Server daemon”问题排查
```bash
sshd -t
```
## 安装MySql
```bash
yum list installed | grep mysql # 查看是否已经安装
yum install mysql-server -y # 安装服务端
yum install mysql-devel -y # 这个应该是组件，不知道有什么用
yum install mysql -y # 安装客户端
```
```bash
service mysqld start # 启动
service mysqld stop # 停止
mysqladmin -u root password 123456 # 设置密码
mysql -u root -p # 登录
service mysqld restart # 重启
```
>注意
```bash
改密码后要重启Mysql服务器
```
## 安装PHP运行环境
```bash
yum install php php-fpm php-bcmatch php-gd php-mbstring php-mcrypt php-mysql php-devel php-pecl-memcache -y
```
>测试是否安装成功
```bash
vi /var/www/html/info.php
```
```bash
<html>
<body>
<h1>It's work!</h1>
<?php
    echo 'HELLO WORLD';
    phpinfo();
?>
</body>
</html>
```
>重启Apache服务器
```bash
/etc/init.d/httpd restart
```
>在浏览器地址栏访问：http://192.168.3.243/info.php

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl2o12audaj210z0k3tbr.jpg)
## 配置Apache使其支持PHP
```bash
这篇笔记写的时间比较长了，不记得当时需不需要在Apache中配置组件支持PHP，如果你访问网站内的.php文件返回源码或下载文件，那么就需要配置组件。
需要在httpd.conf中添加以下代码，修改后重启Apache服务

LoadModule php5_module modules/libphp5.so

AddType application/x-httpd-php .php
AddType application/x-httpd-php-source .phps
```
## 安装MySql图形管理界面phpMyAdmin
```bash
从官网上下载下来（注意版本号，看是否支持本机的MySql和PHP），直接放在网站根目录下，在浏览器中输入相应的地址就可以访问，登陆后即可管理
```
## 安装FTP服务
```bash
安装FTP服务是必须的，安装完成后要注意目录权限是否可以读写或执行
使用ls -l命令查看文件权限参考这里
```
```bash
rpm -qa | grep vsftpd # 查看是否安装
yum install vsftpd -y # 安装
service vsftpd start # 启动FTP服务
```
## 使Apache支持伪静态
```bash
如果使用WordPress设置固定链接为非默认后网站内链接不能访问，那么你的网站不支持伪静态
若不是伪静态只能网站还能返回liuzhenbase.com/index.php?p1这种类似结构的地址，而使用了伪静态可以更好的利于搜索引擎搜录排名
找到apache的配置文件httpd.conf
```
```bash
LoadModule rewrite_module libexec/apache2/mod_rewrite.so
#去掉上面这行的#号
AllowOverride All
# 搜索.htaccess，然后找到AllowOverride进行修改
重启Apache服务，在网站根目录下新建文件htaccess.txt，并且ohter用户设置为（rwx）可读可写，然后再使用WordPress设置链接地址就可以了。
```
