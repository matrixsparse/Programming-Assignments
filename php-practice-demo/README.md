# Php + nginx + Laravel

## 软件版本

```bash
php 7.1
nginx 1.12
Laravel 5.2
```

## 关于Laravel

```bash
Laravel是一个开源的PHP框架，遵循MVC（Model-View-Controller）设计模式

它是由Taylor Otwell于2011年创建的，旨在提供CodeIgniter（CI）框架的高级替代方案

2011年，Laravel项目发布了第1版和第2版

今年5.4版已经推出了诸如Command-Line（CLI）支持命名为"artisan"的许多改进，内置支持更多的数据库类型和改进的路由
```

## 安装EPEL存储库

```bash
用于企业Linux的EPEL或额外软件包是一个额外的软件包存储库，可提供未包含在CentOS官方存储库中的有用的软件包

它可以安装在基于RPM的Linux发行版，如CentOS和Fedora。
```

```bash
yum -y install epel-release
```

## 安装Nginx

我们将在LEMP下运行一个Laravel。 Nginx是LEMP的Web服务器部分，可以从EPEL仓库安装。

```bash
yum -y install nginx
```

>设置开启自动启动

```bash
systemctl start nginx
systemctl enable nginx
```

Nginx在端口80上运行，请使用下面的netstat命令检查。

```bash
netstat -plntu
```

## 安装net-tools
```bash
yum -y install net-tools
```

## 安装和配置PHP-FPM 7.1

```bash
Laravel可以安装在PHP版本> = 5.6.4的服务器上

在CentOS基础存储库中不存在PHP 7.1，需要从名为"webtatic"的第三方存储库安装它。
```

```bash
[root@sparsematrix ~]# rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
Retrieving https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
warning: /var/tmp/rpm-tmp.RIZbLT: Header V4 RSA/SHA1 Signature, key ID 62e74ca5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:webtatic-release-7-3             ################################# [100%]
```

### 使用yum命令来安装PHP-FPM，其中包含Laravel所需的所有扩展

```bash
[root@sparsematrix ~]# yum install -y php71w php71w-curl php71w-common php71w-cli php71w-mysql php71w-mbstring php71w-fpm php71w-xml php71w-pdo php71w-zip
```

### 查看是否安装成功

```bash
[root@sparsematrix ~]# php -v
PHP 7.1.11 (cli) (built: Oct 29 2017 17:26:51) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.1.0, Copyright (c) 1998-2017 Zend Technologies
```

### 编辑php.ini配置文件

```bash
vim /etc/php.ini
```

```bash
取消注释下面的行，并将值更改为0
cgi.fix_pathinfo=0
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmvmg03akhj20o60brgmh.jpg)

### 编辑PHP-FPM文件www.conf

```bash
vim /etc/php-fpm.d/www.conf
```

>PHP-FPM将在用户和组'nginx'下运行

```bash
user = nginx
group = nginx
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmvmif5ieaj20py06qq32.jpg)

>PHP-FPM将在套接字文件下运行，而不是使用服务器端口

将'listen'值更改为路径'/run/php-fpm/php-fpm.sock'

```bash
listen = /run/php-fpm/php-fpm.sock
```

>套接字文件所有者将是"nginx"用户，权限模式为660.取消注释并更改所有值

```bash
listen.owner = nginx
listen.group = nginx
listen.mode  = 0660
```

>关于环境变量，取消注释这些行并进行如下设置

```bash
env[HOSTNAME] = $HOSTNAME
env[PATH] = /usr/local/bin:/usr/bin:/bin
env[TMP] = /tmp
env[TMPDIR] = /tmp
env[TEMP] = /tmp
```

>启动php-fpm

```bash
systemctl start php-fpm
```

>设置开机启动

```bash
systemctl enable php-fpm
```

>查看状态

```bash
systemctl status php-fpm
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmvmscvfryj20u708fgm5.jpg)

>查看PHP-FPM是否在套接字文件下运行

```bash
[root@sparsematrix ~]# netstat -pl | grep php-fpm.sock
unix  2      [ ACC ]     STREAM     LISTENING     2116253  17221/php-fpm: mast  /run/php-fpm/php-fpm.sock
```

## 更换阿里源

### 备份

```bash
mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.backup
```

### 下载新的CentOS-Base.repo到/etc/yum.repos.d/

```bash
wget -O /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo
```

### 生成缓存

```bash
yum makecache
```

## 安装PHP Composer

```bash
PHP composer是PHP编程语言的包管理器

它已经在2011年创建，它的灵感来自于Node.js的"npm"和Ruby的"bundler"安装程序
```

### 使用curl命令安装Composer

```bash
[root@sparsematrix ~]# curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin --filename=composer
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwbsxpgkyj20xa047aa4.jpg)

### 查看Composer是否安装成功

```bash
[root@sparsematrix ~]# composer
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwbsxq3emj20oz0bgaab.jpg)

## 配置Nginx虚拟主机进行Laravel

为这个Laravel安装定义web根目录，将使用'/var/www/laravel'目录作为Web根目录。

>创建目录

```bash
[root@sparsematrix ~]# mkdir -p /var/www/laravel
```

>编辑虚拟主机配置文件

```bash
vim /etc/nginx/conf.d/laravel.conf
```

```bash
server {
        listen 8089;
        # listen [::]:80 ipv6only=on;

        # Log files for Debugging
        access_log /var/log/nginx/laravel-access.log;
        error_log /var/log/nginx/laravel-error.log;

        # Webroot Directory for Laravel project
        root /var/www/laravel/laravel/public;
        index index.php index.html index.htm;

        # Your Domain Name
        # server_name laravel.hakase-labs.co;
        server_name  www.sparsematrix.com;

        location / {
                try_files $uri $uri/ /index.php?$query_string;
        }

        # PHP-FPM Configuration Nginx
        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
                fastcgi_index index.php;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
        }
}
```

### 检查nginx配置文件的语法是否正确

```bash
[root@sparsematrix conf.d]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

## 安装Laravel5.5

### 安装解压缩

```bash
[root@sparsematrix ~]# yum -y install unzip
```

### 去laravel web根目录'/var/www/laravel'

```bash
cd /var/www/laravel
```

```bash
laravel为服务器上的框架安装提供了两种方式：
  1、可以用Laravel安装程序安装Laravel
  2、可以用PHPComposer安装它
```

### 使用composer命令创建一个新项目来安装Laravel

```bash
[root@sparsematrix ~]# cd /var/www/laravel
[root@sparsematrix laravel]# composer create-project laravel/laravel
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwc6qi3xkj20pr0jy76l.jpg)

### 将Laravel Web根目录的所有者更改为"nginx"用户，并使用以下命令将存储目录的权限更改为755

```bash
chown -R nginx:root /var/www/laravel
chmod 755 /var/www/laravel/storage
```

## 配置SELinux

Laravel将运行在SELinux的Enforcing模式下

```bash
[root@sparsematrix ~]# vim /etc/selinux/config
```

```bash
SELINUX=enforcing
```

or

```bash
setenforce 1 设置SELinux 成为enforcing模式
setenforce 0 设置SELinux 成为permissive模式
```

### 重启网卡

```bash
[root@sparsematrix laravel]# /etc/init.d/network restart
```

### 检查SELinux状态

```bash
[root@sparsematrix laravel]# sestatus
```

### CentOS 7安装SELinux管理工具

```bash
[root@sparsematrix laravel]# yum -y install policycoreutils-python
```

### 改变Laravel目录的上下文

```bash
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/public(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/storage(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/app(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/bootstrap(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/config(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/database(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/resources(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/routes(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/vendor(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/tests(/.*)?'
restorecon -Rv '/var/www/laravel/'
```

### 在window上配置hosts

```bash
C:\Windows\System32\drivers\etc
```

```bash
先复制hosts文件到别的地方，修改完了再覆盖回来就搞定了。中间会提示目标文件夹拒绝访问，需要提供管理员权限，点击继续即可
```

### 重启nginx

```bash
[root@sparsematrix ~]# nginx -s reload
```

### 测试Laravel

>在浏览器地址栏中输入：http://www.sparsematrix.com:8089

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwhxdbextj20wm0fp0t3.jpg)

### 查看Laravel版本

```bash
[root@sparsematrix laravel]# php artisan --version
Laravel Framework 5.5.28
```

## 安装Laravel5.2

### 指定安装Laravel5.2

```bash
[root@sparsematrix laravel5.2]# composer create-project --prefer-dist laravel/laravel laravel "5.2.*"
```

### 将Laravel Web根目录的所有者更改为"nginx"用户，并使用以下命令将存储目录的权限更改为755

```bash
[root@sparsematrix laravel]# chown -R nginx:root /var/www/laravel5.2/
[root@sparsematrix laravel]# chmod 755 /var/www/laravel5.2/laravel/storage
```

### 改变Laravel目录的上下文

```bash
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/public(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/storage(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/app(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/bootstrap(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/config(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/database(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/resources(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/routes(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/vendor(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel5.2/laravel/tests(/.*)?'
restorecon -Rv '/var/www/laravel5.2/'
```

### 编辑虚拟主机配置文件

```bash
vim /etc/nginx/conf.d/laravel.conf
```

```bash
server {
        listen 8089;
        # listen [::]:80 ipv6only=on;

        # Log files for Debugging
        access_log /var/log/nginx/laravel5.2-access.log;
        error_log /var/log/nginx/laravel5.2-error.log;

        # Webroot Directory for Laravel project
        root /var/www/laravel5.2/laravel/public;
        index index.php index.html index.htm;

        # Your Domain Name
        # server_name laravel.hakase-labs.co;
        server_name  www.sparsematrix.com;

        location / {
                try_files $uri $uri/ /index.php?$query_string;
        }

        # PHP-FPM Configuration Nginx
        location ~ \.php$ {
                try_files $uri =404;
                fastcgi_split_path_info ^(.+\.php)(/.+)$;
                fastcgi_pass unix:/run/php-fpm/php-fpm.sock;
                fastcgi_index index.php;
                fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
                include fastcgi_params;
        }
}
```

### 检查nginx配置文件的语法是否正确

```bash
[root@sparsematrix conf.d]# nginx -t
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
```

### 重启nginx

```bash
nginx -s reload
```

### 查看Laravel版本

```bash
[root@sparsematrix laravel]# php /var/www/laravel5.2/laravel/artisan --version
Laravel Framework version 5.2.45
```

### 在浏览器地址栏访问：http://www.sparsematrix.com:8089/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwj89wfwsj20wn0ffdfz.jpg)
