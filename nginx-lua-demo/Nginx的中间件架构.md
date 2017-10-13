# Nginx的中间件架构


## 准备

```bash
Cetntos 7
```

### 安装基本库

```bash
yum -y install gcc gcc-c++ autoconf pcre pcre-devel make automake
```

### 安装基本工具

```bash
yum -y install wget httpd-tools vim
```

### 初始化

```bash
cd /data/nginx/
mkdir app download logs work backup
```

* /data/nginx
    * app：代码目录
    * download：源码包
    * logs：自定义日志
    * work：shell脚本
    * backup：默认配置文件

### 查看yum源是否可用

```bash
yum list | grep gcc
```
### 查看是否有iptables规则

```bash
iptables -L
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1filzsal8yfj21ha0ck440.jpg)

```bash
iptables -t nat -L
```

>关闭iptables规则

```bash
iptables -F
iptables -t nat -F
```

### 查看命令

```bash
[root@sparsematrix nginx]# getenforce
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1filzx4mq0aj21ds0323zl.jpg)

## Nginx简述

```bash
Nginx是一个开源且高性能、可靠的HTTP中间件、代理服务
```

### 常见的HTTP服务

* HTTPD - Apache基金会
* IIS - 微软
* GWS - Google

## 为什么选择Nginx

### IO多路复用epoll/并发问题

多个描述符I/O操作都能在一个线程内`并发交替`地顺序完成，这就叫I/O多路复用，这里的"复用"指的是复用同一个线程

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fim07ul04wj21wq0giae5.jpg)

>什么是epoll

```bash
IO多路复用的实现方式select、poll、epoll
```

* select：结账的时候，服务员不告诉老板哪桌要结账，老板一个个去问才知道哪桌要结账
* epoll：结账的时候，服务员告诉老板哪桌要结账


### 轻量级

* 功能模块少
* 代码模块化

### CPU亲和(affinity)

>CPU亲和

是一种把CPU核心和Nginx工作进程绑定的方式，把每个worker进程固定在一个CPU上执行，减少切换CPU的cache miss，获得更好的性能

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fim0j2qutsj21y40iwtd6.jpg)

### 0拷贝

## Nginx安装

* Mainline version：开发版
* Stable version：稳定版

```bash
[root@sparsematrix ~]# vim /etc/yum.repos.d/nginx.repo
```

```bash
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/$basearch/
gpgcheck=0
enabled=1
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimesan0trj21v40rmagh.jpg)

### 查看yum源中nginx相关版本

```bash
[root@sparsematrix ~]# yum list | grep nginx
```

### 使用yum源安装Nginx

```bash
[root@sparsematrix ~]# yum install nginx -y
```

### 查看当前安装nginx版本

```bash
[root@sparsematrix ~]# nginx -v
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimej0moqkj21bo02sjsj.jpg)

### 查看Nginx编译参数

```bash
[root@sparsematrix ~]# nginx -V
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fimekxcei6j21da0w27tc.jpg)

### Nginx安装编译参数详解

```bash
--prefix=/etc/nginx 【安装目的目录或路径】
--sbin-path=/usr/sbin/nginx 【安装目的目录或路径】
--modules-path=/usr/lib64/nginx/modules 【安装目的目录或路径】
--conf-path=/etc/nginx/nginx.conf 【安装目的目录或路径】
--error-log-path=/var/log/nginx/error.log 【安装目的目录或路径】
--http-log-path=/var/log/nginx/access.log 【安装目的目录或路径】
--pid-path=/var/run/nginx.pid 【安装目的目录或路径】
--lock-path=/var/run/nginx.lock 【安装目的目录或路径】
--http-client-body-temp-path=/var/cache/nginx/client_temp【执行对应模块时，Nginx所保留的临时性文件】
--http-proxy-temp-path=/var/cache/nginx/proxy_temp 【执行对应模块时，Nginx所保留的临时性文件】
--http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp 【执行对应模块时，Nginx所保留的临时性文件】
--http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp 【执行对应模块时，Nginx所保留的临时性文件】
--http-scgi-temp-path=/var/cache/nginx/scgi_temp【执行对应模块时，Nginx所保留的临时性文件】
--user=nginx
--group=nginx【设定Nginx进程启动的用户和组用户】
--with-compat
--with-file-aio
--with-threads
--with-http_addition_module
--with-http_auth_request_module
--with-http_dav_module
--with-http_flv_module
--with-http_gunzip_module
--with-http_gzip_static_module
--with-http_mp4_module
--with-http_random_index_module【目录中选择一个随机主页】
    Syntax：random_index on | off
    Default：random_index off
    Context：location
--with-http_realip_module
--with-http_secure_link_module
--with-http_slice_module
--with-http_ssl_module
--with-http_stub_status_module【Nginx的客户端状态】
    Syntax：stub_status
    Default： -
    Context： server，location
--with-http_sub_module
--with-http_v2_module
--with-mail
--with-mail_ssl_module
--with-stream
--with-stream_realip_module
--with-stream_ssl_module
--with-stream_ssl_preread_module
--with-cc-opt='-O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector-strong --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic -fPIC'【设置额外的参数将被添加到CFLAGS变量】
--with-ld-opt='-Wl,-z,relro -Wl,-z,now -pie'【设置附加的参数，链接系统库】
```

### Nginx安装目录解析

```bash
使用yum源安装其实安装的都是一个个rpm包
```

>使用rpm -ql查看nginx的安装目录

```bash
[root@sparsematrix ~]# rpm -ql nginx
```

```bash
/etc/logrotate.d/nginx【配置文件】Nginx日志轮转，用于logrotate服务的日志切割
/etc/nginx【目录、配置文件】Nginx主配置文件
/etc/nginx/conf.d【目录、配置文件】Nginx主配置文件
/etc/nginx/conf.d/default.conf【目录、配置文件】Nginx主配置文件
/etc/nginx/fastcgi_params【配置文件】cgi配置相关，fastcgi配置
/etc/nginx/koi-utf【配置文件】编码转换映射转化文件
/etc/nginx/koi-win【配置文件】编码转换映射转化文件
/etc/nginx/mime.types【配置文件】设置http协议的Content-Type与拓展名对应关系
/etc/nginx/modules【目录】Nginx模块目录
/etc/nginx/nginx.conf【目录、配置文件】Nginx主配置文件
/etc/nginx/scgi_params【配置文件】cgi配置相关，fastcgi配置
/etc/nginx/uwsgi_params【配置文件】cgi配置相关，fastcgi配置
/etc/nginx/win-utf【配置文件】编码转换映射转化文件
/etc/sysconfig/nginx【配置文件】用于配置出系统守护进程管理器管理方式
/etc/sysconfig/nginx-debug【配置文件】用于配置出系统守护进程管理器管理方式
/usr/lib/systemd/system/nginx-debug.service【配置文件】用于配置出系统守护进程管理器管理方式
/usr/lib/systemd/system/nginx.service【配置文件】用于配置出系统守护进程管理器管理方式
/usr/lib64/nginx
/usr/lib64/nginx/modules【目录】Nginx模块目录
/usr/libexec/initscripts/legacy-actions/nginx
/usr/libexec/initscripts/legacy-actions/nginx/check-reload
/usr/libexec/initscripts/legacy-actions/nginx/upgrade
/usr/sbin/nginx【命令】Nginx服务的启动管理的终端命令
/usr/sbin/nginx-debug【命令】Nginx服务的启动管理的终端命令
/usr/share/doc/nginx-1.12.1【文件、目录】Nginx的手册和帮助文件
/usr/share/doc/nginx-1.12.1/COPYRIGHT【文件、目录】Nginx的手册和帮助文件
/usr/share/man/man8/nginx.8.gz【文件、目录】Nginx的手册和帮助文件
/usr/share/nginx
/usr/share/nginx/html
/usr/share/nginx/html/50x.html
/usr/share/nginx/html/index.html
/var/cache/nginx【目录】Nginx的缓存目录
/var/log/nginx【目录】Nginx的日志目录
```

![](http://ww1.sinaimg.cn/large/dc05ba18gy1fimeqpfjgtj21cc104ndm.jpg)

```bash
[root@sparsematrix ~]# yum install -y curl
```

curl可以理解为浏览器

```bash
[root@sparsematrix ~]# curl -v http://www.baidu.com
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzbdobjdj221g14ex6g.jpg)

>启动Nginx

```bash
[root@sparsematrix ~]# /usr/sbin/nginx
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzqmftanj22140ewgou.jpg)

>测试配置是否正确

```bash
/usr/sbin/nginx -t
```

```bash
#如果显示如下内容说明配置成功
nginx: the configuration file /usr/servers/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/servers/nginx/conf/nginx.conf test is successful
```

>重启nginx

```bash
/usr/sbin/nginx -s reload
```

## Nginx默认配置语法

```bash
[root@sparsematrix ~]# cd /etc/nginx/
[root@sparsematrix nginx]# cat nginx.conf

user  nginx;# user【设置Nginx服务的系统使用用户】
worker_processes  1;# worker_processes【工作进程数】

error_log  /var/log/nginx/error.log warn;# error_log【Nginx的错误日志】
pid        /var/run/nginx.pid;# pid【Nginx服务启动时候pid】

# events worker_connections【每个进程允许最大连接数】
# events use【工作进程数】
events {
    worker_connections  1024;
}


http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;

    sendfile        on;
    #tcp_nopush     on;

    keepalive_timeout  65;

    #gzip  on;

    include /etc/nginx/conf.d/*.conf;
}
```

### 查看/etc/nginx/conf.d/default.conf

```bash
[root@sparsematrix nginx]# cd /etc/nginx/conf.d/
[root@sparsematrix conf.d]# ls
default.conf
[root@sparsematrix conf.d]# cat default.conf
server {
    listen       8088;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }

    #error_page  404              /404.html;

    # redirect server error pages to the static page /50x.html
    #
    error_page   500 502 503 504  /50x.html;
    location = /50x.html {
        root   /usr/share/nginx/html;
    }

    # proxy the PHP scripts to Apache listening on 127.0.0.1:80
    #
    #location ~ \.php$ {
    #    proxy_pass   http://127.0.0.1;
    #}

    # pass the PHP scripts to FastCGI server listening on 127.0.0.1:9000
    #
    #location ~ \.php$ {
    #    root           html;
    #    fastcgi_pass   127.0.0.1:9000;
    #    fastcgi_index  index.php;
    #    fastcgi_param  SCRIPT_FILENAME  /scripts$fastcgi_script_name;
    #    include        fastcgi_params;
    #}

    # deny access to .htaccess files, if Apache's document root
    # concurs with nginx's one
    #
    #location ~ /\.ht {
    #    deny  all;
    #}
}
```

### 检查配置文件语法

```bash
[root@sparsematrix ~]# nginx -t -c /etc/nginx/nginx.conf
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqymp2mu6j21o0046tbx.jpg)

### log_format

>查看access_log

```bash
[root@sparsematrix ~]# head /var/log/nginx/access.log
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzvy5a9dj221s07211c.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqyr42ukbj21na0yatjo.jpg)

## Nginx模块

* 官方模块
* 第三方模块


### stub_status

```bash
[root@sparsematrix ~]# vi /etc/nginx/conf.d/default.conf
location /mystatus {
    stub_status;
}
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzyu4djoj21k40xs7fe.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fiqzxzgutbj215808u76l.jpg)

### random_index

```bash
[root@sparsematrix test]# pwd
/data/nginx/test
[root@sparsematrix test]# ll
总用量 12
-rw-r--r--. 1 root root 149 8月  21 08:05 1.html
-rw-r--r--. 1 root root 149 8月  21 08:06 2.html
-rw-r--r--. 1 root root 151 8月  21 08:06 3.html
```

```bash
[root@sparsematrix ~]# vi /etc/nginx/conf.d/default.conf
````

```bash
location / {
    #root   /usr/share/nginx/html;
    root /data/nginx/test;
    random_index on;
    #index  index.html index.htm;
}
```

>不断刷新浏览器

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fir0zx5qtyj21re0dcjso.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fir0zx90l0j215m08qt9k.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fir0zx9ycpj215i0a6756.jpg)

### sub_module

| 编译选项 | 作用 |
| ---------------| --------------- |
| --with-http_sub_module | HTTP内容替换 |

>http_sub_module

```bash
Synta: sub_filter string replacement
Default: -
Context: http,server,location
```

```bash
[root@sparsematrix code]# vi submodule.html
<html>
<html>
<head>
	<meta charset="utf-8">
	<title>submodules</title>
</head>
<body>
	<a>jeson</a>
	<a>atom</a>
	<a>matrix</a>
	<a>jeson</a>
</body>
</html>
```

>修改/etc/nginx/conf.d/default.conf

```bash
location / {
    root /data/nginx/app/code;
    #root /data/nginx/test;
    #root   /usr/share/nginx/html;
    #random_index on;
    #index  index.html index.htm;
}
```

>访问http://115.28.240.96:8088/submodule.html

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkgg6rxmw2j20it046wei.jpg)

>修改/etc/nginx/conf.d/default.conf

```bash
location / {
    root /data/nginx/app/code;
    sub_filter '<a>matrix</a>' '<a>sparsematrix</a>';
    #root /data/nginx/test;
    #root   /usr/share/nginx/html;
    #random_index on;
    #index  index.html index.htm;
}
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkggkrt06oj20f503n3yj.jpg)

### limit_req_zone[请求限制]

```bash
Synta: limit_req_zone key zone=name;size rate=rate;
Default: -
Context: http

Synta: limit_req zone=name [burst=number][nodelay]
Default: -
Context: http,server,location
```
