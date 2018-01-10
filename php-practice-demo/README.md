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

它可以安装在基于RPM的Linux发行版，如CentOS和Fedora
```

```bash
yum -y install epel-release
```

## 安装mysql

```bash
rpm -ivh http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
```

### 更新yum软件包

```bash
yum check-update  
```

### 更新系统

```bash
yum update
```

### 安装mysql

``` bash
yum install mysql mysql-server -y
```

## 启动

```bash
systemctl start mysqld
mysql -u root
```

### 修改密码

```bash
set password for 'root'@'localhost'=password('123456');
```

### 授权远程访问

```bash
use mysql;
grant all privileges  on *.* to root@'%' identified by "root";
flush privileges;
```

## 源码安装nginx

```bash
wget http://nginx.org/download/nginx-1.11.2.tar.gz
tar -xzvf nginx-1.11.2.tar.gz -C /data/server
# 安装依赖
yum install gcc libpcre3 libpcre3-dev openssl libssl-dev libssl0.9.8 perl libperl-dev pcre-devel openssl openssl-devel perl-ExtUtils-Embed -y
mv /data/server/nginx-1.11.2 /data/server/nginx
cd /data/server/nginx
# 以下是一行。。用于生成makefile。如果需要添加第三方模块，使用--add-module=/path/module1的方法编译
./configure --prefix=/etc/nginx --with-ipv6 --with-http_ssl_module --with-http_realip_module --with-http_addition_module --with-http_dav_module --with-http_flv_module --with-http_mp4_module --with-http_gzip_static_module --with-http_perl_module --with-mail --with-mail_ssl_module
# make是生成在objs目录中，make install则安装到prefix所示的目录中
make && make install
# 没有错误出现的话，就可以进入nginx安装目录(/usr/local/nginx)配置。
```

>创建软连接

```bash
[root@sparsematrix ~]# ln -fs /etc/nginx/sbin/nginx /usr/sbin/nginx
```

### 安装Nginx时报错

```bash
./configure: error: the HTTP rewrite module requires the PCRE library.
```

>安装pcre-devel解决问题

```bash
yum -y install pcre-devel openssl openssl-devel perl-ExtUtils-Embed
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

>重启nginx

```bash
systemctl restart nginx.service
```

>查看nginx安装路径

```bash
rpm -ql nginx
```

>查看nginx进程

```bash
[root@sparsematrix ~]# ps -aux | grep nginx
root      38359  0.0  0.4  60320  4704 ?        Ss   16:22   0:00 nginx: master process nginx
nobody    38902  0.0  0.3  60728  3784 ?        S    16:49   0:00 nginx: worker process
root      39393  0.0  0.0 112664   968 pts/4    R+   17:09   0:00 grep --color=auto nginx
```

## 安装net-tools

```bash
yum -y install net-tools
```

## 安装git

```bash
yum install -y git
```

## 安装和配置PHP-FPM 7.1

```bash
Laravel可以安装在PHP版本> = 5.6.4的服务器上

在CentOS基础存储库中不存在PHP 7.1，需要从名为"webtatic"的第三方存储库安装它。
```

```bash
[root@sparsematrix ~]# pm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
[root@sparsematrix ~]# rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
Retrieving https://mirror.webtatic.com/yum/el7/webtatic-release.rpm
warning: /var/tmp/rpm-tmp.RIZbLT: Header V4 RSA/SHA1 Signature, key ID 62e74ca5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:webtatic-release-7-3             ################################# [100%]
```

### 使用yum命令来安装PHP-FPM，其中包含Laravel所需的所有扩展

```bash
[root@sparsematrix ~]# yum install -y php71w php71w-curl php71w-common php71w-cli php71w-mysql php71w-mbstring php71w-fpm php71w-xml php71w-pdo php71w-zip php71w-gd php71w-intl php71w-xsl
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

>PHP-FPM将在用户和组'nobody'下运行

```bash
user = nobody
group = nobody
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmvmif5ieaj20py06qq32.jpg)

>PHP-FPM将在套接字文件下运行，而不是使用服务器端口

将'listen'值更改为路径'/run/php-fpm/php-fpm.sock'

```bash
listen = /run/php-fpm/php-fpm.sock
```

>套接字文件所有者将是"nobody"用户，权限模式为660.取消注释并更改所有值

```bash
listen.owner = nobody
listen.group = nobody
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
        listen 80;
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

### 将Laravel Web根目录的所有者更改为"nobody"用户，并使用以下命令将存储目录的权限更改为755

```bash
chown -R nobody:root /var/www/laravel
chmod 755 /var/www/laravel/storage
```

## 配置SELinux

Laravel将运行在SELinux的permissive模式下[这样就不会限制端口访问] -> 如果这边不进行设置，后面运行Laravel项目的时候就会出现，无法访问MySQL数据库的情况

```bash
[root@sparsematrix ~]# vim /etc/selinux/config
```

```bash
SELINUX=permissive
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

### 改变Laravel目录的上下文【这步作废】

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

### 使用semanage命令查看端口

```bash
semanage port -l | grep http_port_t                # fine allow port
semanage port -a -t http_port_t -p tcp 9000        # add
semanage port -d -t http_port_t -p tcp 9090        # del
semanage port -m -t http_port_t -p tcp 3306        # add user define port
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
[root@sparsematrix laravel]# chown -R nginx:root /var/www/laravel/
[root@sparsematrix laravel]# chmod 755 /var/www/laravel/laravel/storage
```

### 改变Laravel目录的上下文【这步作废】

```bash
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/public(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/storage(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/app(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/bootstrap(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/config(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/database(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/resources(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/routes(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/vendor(/.*)?'
semanage fcontext -a -t httpd_sys_rw_content_t '/var/www/laravel/laravel/tests(/.*)?'
restorecon -Rv '/var/www/laravel/'
```

### 编辑虚拟主机配置文件

```bash
vim /etc/nginx/conf.d/laravel.conf
```

```bash
server {
        listen 80;
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

### 在浏览器地址栏访问：http://www.sparsematrix.com

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwj89wfwsj20wn0ffdfz.jpg)

## Centos7安装node

### 使用yum源安装nodejs

```bash
yum install nodejs -y
```

### 查看node版本

```bash
[root@sparsematrix ~]# node -v
v6.12.0
```

## 运行dms项目【基于Laravel开发】

```bash
将代码上传到远程服务器
```

>注意

```bash
vendor是使用composer安装后才会出现的目录
```

### 安装Laravel

```bash
[root@sparsematrix dms]# cp .env.example .env
```

```bash
[root@sparsematrix dms]# composer install
```

### 查看Laravel版本

```bash
[root@sparsematrix dms]# php /var/www/laravel/dms/artisan --version
Laravel Framework version 5.2.45
```

### 安装gulp

```bash
[root@sparsematrix dms]# npm install -g gulp
[root@sparsematrix dms]# npm install -g gulp-notify
```

>安装node相关模块

```bash
[root@sparsematrix dms]# npm install
```

```bash
yum install libnotify
```

### 运行gulp进行压缩

```bash
[root@sparsematrix dms]# gulp
```

### 将Laravel Web根目录的所有者更改为"nobody"用户，并使用以下命令将存储目录的权限更改为755

```bash
[root@sparsematrix laravel]# chown -R nobody:root /var/www/laravel/
[root@sparsematrix laravel]# chmod 755 /var/www/laravel/dms/storage
```

### 编辑虚拟主机配置文件

```bash
vim /etc/nginx/conf.d/dms.conf
```

```bash
server {
        listen 80;
        # listen [::]:80 ipv6only=on;

        # Log files for Debugging
        access_log /var/log/nginx/laravel-dms-access.log;
        error_log /var/log/nginx/laravel-dms-error.log;

        # Webroot Directory for Laravel project
        root /var/www/laravel/dms/public;
        index index.php index.html index.htm;

        # Your Domain Name
        # server_name laravel.hakase-labs.co;
        server_name dms.if.cc;

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

### 重启nginx

```bash
[root@sparsematrix dms]# nginx -s reload
```

### 编辑.env文件，配置SESSION_DOMAIN【域名】，这个配置错误的话，就会无法访问

```bash
APP_ENV=local
APP_DEBUG=true
APP_KEY=8abBPNT9NleoYksUadTeP07niOpPiITa
SESSION_DOMAIN=dms.if.cc

DB_CONNECTION=mysql
DB_HOST=192.168.11.119
DB_DATABASE=dms
DB_USERNAME=root
DB_PASSWORD=patpat

CACHE_DRIVER=file
SESSION_DRIVER=file
QUEUE_DRIVER=sync

;Mail
MAIL_HOST=smtp.mailgun.org
MAIL_PORT=587
MAIL_FROM_ADDRESS=wms@service.patpat.com
MAIL_ENCRYPTION=tls
MAIL_USERNAME=wms@service.patpat.com
MAIL_PASSWORD=2058286a6794rw9581d8

;API Configure
API_SIGNCODE=2CE868847F16BB105B41E2B92AAC7A5B

;STA API SIGNCODE
STA_API_URL=http://oms.patpat.com/api/sta/
STA_API_SIGNCODE=2CE868847F16BB105B41E2B92EWC7AFF
```

>在window上配置hosts

```bash
192.168.5.180 dms.if.cc
```

>在地址栏访问：dms.if.cc

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fn2iylf9zoj214j0j7aoo.jpg)

## 运行dms-etc项目【基于Laravel项目】

>在window上配置hosts

```bash
192.168.5.180 dms-etl.if.cc
```

```bash
[root@sparsematrix dms]# composer install
```

### 查看Laravel版本

```bash
[root@sparsematrix ~]# php /var/www/laravel/dms-etl/artisan --version
Laravel Framework version 5.2.45
```

### 安装gulp

```bash
[root@sparsematrix dms]# npm install -g gulp
[root@sparsematrix dms]# npm install -g gulp-notify
```

```bash
[root@sparsematrix dms]# npm install
```

### 运行gulp进行压缩

```bash
[root@sparsematrix dms]# gulp
```

### 将Laravel Web根目录的所有者更改为"nobody"用户，并使用以下命令将存储目录的权限更改为755

```bash
[root@sparsematrix laravel]# chown -R nobody:root /var/www/laravel/
[root@sparsematrix laravel]# chmod 755 /var/www/laravel/dms/storage
```

### 编辑/var/www/laravel/dms-etl/.env配置文件

```bash
vim /var/www/laravel/dms-etl/.env
```

```bash
APP_ENV=local
APP_DEBUG=true
APP_KEY=8abBPNT9NleoYksUadTeP07niOpPiITa
APP_URL=http://dms-etl.if.cc

 ;dms db
 DB_HOST=192.168.11.119
 DB_PORT=3306
 DB_DATABASE=dms
 DB_USERNAME=root
 DB_PASSWORD=patpat

 ;patpat slave
 DB_HOST1=192.168.11.119
 DB_PORT1=3306
 DB_DATABASE1=patpat
 DB_USERNAME1=root
 DB_PASSWORD1=patpat

 ;rds log master
 DB_HOST2=192.168.11.119
 DB_PORT2=3306
 DB_DATABASE2=log
 DB_USERNAME2=root
 DB_PASSWORD2=patpat

 ;rds log slave
 DB_HOST3=192.168.11.119
 DB_PORT3=3306
 DB_DATABASE3=log
 DB_USERNAME3=root
 DB_PASSWORD3=patpat

 ;dw db
 DB_HOST4=192.168.11.119
 DB_PORT4=3306
 DB_DATABASE4=patpat
 DB_USERNAME4=root
 DB_PASSWORD4=patpat

CACHE_DRIVER=file
SESSION_DRIVER=file
QUEUE_DRIVER=sync

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

MAIL_DRIVER=smtp
MAIL_HOST=mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=null
MAIL_PASSWORD=null
MAIL_ENCRYPTION=null

;Amazon Cloudfront CDN
SOURCE_CND_URL=img.patpat.com
ASSET_CND_URL=img.patpat.com

;log info, default LOG_PATH/LOG_NAME.log
LOG_PATH=/var/log/laravel/dms-etl
LOG_NAME=laravel
```

### 进入dms-etl项目目录

```bash
cd /var/www/laravel/dms-etl
```

### 创建目录并给与777权限

```bash
chmod 777 /var/www/laravel/dms-etl/storage
mkdir -p /var/www/laravel/dms-etl/storage/app
mkdir -p /var/www/laravel/dms-etl/storage/logs
mkdir -p /var/www/laravel/dms-etl/storage/framework/sessions
mkdir -p /var/www/laravel/dms-etl/storage/framework/views
mkdir -p /var/www/laravel/dms-etl/storage/framework/cache
```

### 编辑nginx的dms-ctl.conf配置文件

```bash
vim /etc/nginx/conf.d/dms-ctl.conf
```

```bash
server {
        listen 80;
        # listen [::]:80 ipv6only=on;

        # Log files for Debugging
        access_log /var/log/nginx/laravel-dms-etl-access.log;
        error_log /var/log/nginx/laravel-dms-etl-error.log;

        # Webroot Directory for Laravel project
        root /var/www/laravel/dms-etl/public;
        index index.php index.html index.htm;

        # Your Domain Name
        # server_name laravel.hakase-labs.co;
        server_name dms-etl.if.cc;

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

### 在浏览器地址栏中访问：http://dms-etl.if.cc/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fn38cn4xg2j21gt0fcdgw.jpg)
