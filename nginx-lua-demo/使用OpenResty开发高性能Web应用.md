# 使用OpenResty开发高性能Web应用

>Nginx优点

```bash
Nginx设计为一个主进程多个工作进程的工作模式，每个进程是单线程来处理多个连接，而且每个工作进程采用了非阻塞I/O来处理多个连接，
从而减少了线程上下文切换，实现了公认的高性能、高并发。

因此，在生产环境中会通过把CPU绑定给Nginx工作进程，从而提升其性能

另外，因为单线程工作模式的特点，内存占用就非常少了

Nginx更改配置后重启速度非常快，可以达到毫秒级，而且支持不停止Nginx进行升级Nginx版本、动态重载Nginx配置

Nginx模块也非常多，功能也很强劲，不仅可以作为HTTP负载均衡，Nginx发布1.9.0版本还支持TCP负载均衡，
还可以很容易地实现内存缓存、Web服务器、反向代理、访问控制等
```

>Lua优点

```bash
Lua是一种轻量级，可嵌入式的脚本语言，可以非常容易地嵌入到其他语言中使用

Lua提供协程并发，即以同步调用的方式进行异步执行，从而实现并发，比起回调机制并发来说代码更容易编写和理解

Lua的小巧轻量级，可以在Nginx中嵌入Lua VM，请求的时候创建一个VM，请求结束的时候回收VM
```

```bash
使用OpenResty，其是由Nginx核心加很多第三方模块组成，其最大的亮点是默认集成了Lua开发环境，使得Nginx可以作为一个Web Server使用

借助于Nginx的事件驱动模型和非阻塞IO，可以实现高性能的Web应用程序

而且OpenResty提供了大量组件如Mysql、Redis、Memcached等等，使在Nginx上开发Web应用更方便更简单

目前在京东如实时价格、秒杀、动态服务、单品页、列表页等都在使用Nginx+Lua架构，其他公司如淘宝、去哪儿网等
```

## 创建目录/usr/servers，以后我们把所有软件安装在此目录

```bash
mkdir -p /usr/servers
cd /usr/servers/
```

## 安装依赖

```bash
yum install libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl pcre-devel
```

## 下载ngx_openresty-1.7.7.2.tar.gz并解压

```bash
wget http://openresty.org/download/ngx_openresty-1.7.7.2.tar.gz
tar -xzvf ngx_openresty-1.7.7.2.tar.gz
```

```bash
ngx_openresty-1.7.7.2/bundle目录里存放着nginx核心和很多第三方模块，比如有我们需要的Lua和LuaJIT。
```

## 安装LuaJIT

```bash
cd ngx_openresty-1.7.7.2/bundle/LuaJIT-2.1-20150120/
make clean && make && make install
ln -sf luajit-2.1.0-alpha /usr/local/bin/luajit
```

## 下载ngx_cache_purge模块，该模块用于清理nginx缓存

```bash
cd /usr/servers/ngx_openresty-1.7.7.2/bundle  
wget https://github.com/FRiCKLE/ngx_cache_purge/archive/2.3.tar.gz  
tar -xvf 2.3.tar.gz  
```

## 下载nginx_upstream_check_module模块，该模块用于ustream健康检查

```bash
cd /usr/servers/ngx_openresty-1.7.7.2/bundle  
wget https://github.com/yaoweibin/nginx_upstream_check_module/archive/v0.3.0.tar.gz  
tar -xvf v0.3.0.tar.gz   
```

## 安装ngx_openresty

```bash
cd /usr/servers/ngx_openresty-1.7.7.2
./configure --prefix=/usr/servers --with-http_realip_module  --with-pcre  --with-luajit --add-module=./bundle/ngx_cache_purge-2.3/ --add-module=./bundle/nginx_upstream_check_module-0.3.0/ -j2
make && make install
```

```bash
--with***         安装一些内置/集成的模块
--with-http_realip_module     取用户真实ip模块
-with-pcre        Perl兼容的达式模块
--with-luajit     集成luajit模块
--add-module      添加自定义的第三方模块，如此次的ngx_che_purge
```

## 到/usr/servers目录下

```bash
cd /usr/servers/
ll   
```

```bash
会发现多出来了如下目录，说明安装成功
/usr/servers/luajit ：luajit环境，luajit类似于java的jit，即即时编译，lua是一种解释语言，通过luajit可以即时编译lua代码到机器代码，得到很好的性能；
/usr/servers/lualib：要使用的lua库，里边提供了一些默认的lua库，如redis，json库等，也可以把一些自己开发的或第三方的放在这；
/usr/servers/nginx ：安装的nginx；
通过/usr/servers/nginx/sbin/nginx  -V 查看nginx版本和安装的模块
```

## 启动nginx

### 编辑nginx.conf配置文件

```bash
vim /usr/servers/nginx/conf/nginx.conf
```

### 在http部分添加如下配置

```bash
#lua模块路径，多个之间”;”分隔，其中”;;”表示默认搜索路径，默认到/usr/servers/nginx下找  
lua_package_path "/usr/servers/lualib/?.lua;;";  #lua 模块  
lua_package_cpath "/usr/servers/lualib/?.so;;";  #c模块   
```

### 为了方便开发我们在/usr/servers/nginx/conf目录下创建一个lua.conf

```bash
#lua.conf  
server {  
    listen       80;  
    server_name  _;  
}  
```

### nginx.conf中的http部分添加include lua.conf包含此文件片段

```bash
include lua.conf;
```

### 测试是否正常

```bash
/usr/servers/nginx/sbin/nginx  -t
```

>如果显示如下内容说明配置成功

```bash
nginx: the configuration file /usr/servers/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /usr/servers/nginx/conf/nginx.conf test is successful
```

## HelloWorld

### 在lua.conf中server部分添加如下配置

```bash
location /lua {  
    default_type 'text/html';  
    content_by_lua 'ngx.say("hello world")';  
}
```

### 测试配置是否正确

```bash
/usr/servers/nginx/sbin/nginx  -t
```

### 重启nginx

```bash
/usr/servers/nginx/sbin/nginx -s reload
```

>访问http://192.168.3.242/lua

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkfl885ee0j20kt03w746.jpg)

### lua代码文件

```bash
把lua代码放在nginx配置中会随着lua的代码的增加导致配置文件太长不好维护，因此我们应该把lua代码移到外部文件中存储
```

```bash
vim /usr/servers/nginx/conf/lua/test.lua
```

```bash
ngx.say('hello world');
```

#### 然后lua.conf修改为

```bash
#lua.conf  
server {  
    listen       80;  
    server_name  _;
    location /lua {
  	  default_type 'text/html';
  	  content_by_lua_file conf/lua/test.lua;
    }
}
```

### lua_code_cache

```bash
默认情况下lua_code_cache是开启的，即缓存lua代码
即每次lua代码变更必须reload nginx才生效，如果在开发阶段可以通过lua_code_cache off
关闭缓存，这样调试时，每次修改lua代码不需要reload nginx，但是正式环境一定记得开启缓存
```

```bash
location /lua {
  default_type 'text/html';
  lua_code_cache off;
  content_by_lua_file conf/lua/test.lua;
}
```

>开启后reload nginx会看到如下报警

```bash
nginx: [alert] lua_code_cache is off; this will hurt performance in /usr/servers/nginx/conf/lua.conf:7
```

### 错误日志

>如果运行过程中出现错误，请不要忘记查看错误日志

```bash
tail -f /usr/servers/nginx/logs/error.log
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fkflaqixqbj21gp0bijt6.jpg)

### nginx+lua项目构建

```bash
以后我们的nginx lua开发文件会越来越多，我们应该把其项目化，已方便开发。项目目录结构如下所示：
example
    example.conf     ---该项目的nginx配置文件
    lua              ---我们自己的lua代码
      test.lua
    lualib           ---lua依赖库/第三方依赖
      *.lua
      *.so

其中我们把lualib也放到项目中的好处就是以后部署的时候可以一起部署，防止有的服务器忘记复制依赖而造成缺少依赖的情况。
```

>将项目放到到/usr/example目录下

>/usr/servers/nginx/conf/nginx.conf配置文件如下(此处我们最小化了配置文件)

```bash
#user  nobody;  
worker_processes  2;  
error_log  logs/error.log;  
events {  
    worker_connections  1024;  
}  
http {  
    include       mime.types;  
    default_type  text/html;  

    #lua模块路径，其中”;;”表示默认搜索路径，默认到/usr/servers/nginx下找  
    lua_package_path "/usr/example/lualib/?.lua;;";  #lua 模块  
    lua_package_cpath "/usr/example/lualib/?.so;;";  #c模块  
    include /usr/example/example.conf;  
}
```

>/usr/example/example.conf配置文件如下

```bash
server {  
    listen       80;  
    server_name  _;  

    location /lua {  
        default_type 'text/html';  
        lua_code_cache off;  
        content_by_lua_file /usr/example/lua/test.lua;  
    }  
}
```
