# 安装OpenResty(Nginx+Lua)开发环境

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
yum install libreadline-dev libncurses5-dev libpcre3-dev libssl-dev perl  
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
