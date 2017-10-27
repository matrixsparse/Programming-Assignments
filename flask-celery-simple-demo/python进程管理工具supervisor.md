# python进程管理工具supervisor

```bash
supervisord：服务守护进程
supervisorctl：命令行客户端
```

```bash
supervisor管理进程，就是通过fork/exec的方式把这些被管理的进程，当作supervisor的子进程来启动
被管理进程作为supervisor的子进程，当子进程挂掉的时候，父进程可以准确获取子进程挂掉的信息的，可以对挂掉的子进程进行自动重启
```

```bash
Supervisor（http://supervisord.org/）是用Python开发的一个client/server服务，是Linux/Unix系统下的一个进程管理工具，不支持Windows系统
它可以很方便的监听、启动、停止、重启一个或多个进程
用Supervisor管理的进程，当一个进程意外被杀死，supervisort监听到进程死后，会自动将它重新拉起，很方便的做到进程自动恢复的功能，不再需要自己写shell脚本来控制
```

## 安装supervisor

```bash
yum install python-setuptools -y
easy_install supervisor
```

```bash
supervisor安装完成后会生成三个执行程序：supervisortd、supervisorctl、echo_supervisord_conf
分别是supervisor的守护进程服务（用于接收进程管理命令）、客户端（用于和守护进程通信，发送管理进程的指令）、生成初始配置文件程序
```

### 测试是否安装成功

```bash
echo_supervisord_conf
```

## 创建配置文件

### 创建supervisor配置文件目录/etc/supervisor/

```bash
mkdir -m 755 -p /etc/supervisor/
```

### 创建主配文件supervisord.conf

```bash
echo_supervisord_conf > /etc/supervisor/supervisord.conf
```

### 创建项目配置文件目录

```bash
cd /etc/supervisor/
mkdir -m 755 conf.d
```

### 调试

在/etc/supervisor/conf.d目录下创建test.ini

>test.ini

```bash
[group:test]
programs = test.print

[program:test.print]
; 启动命令，可以看出与手动在命令行启动的命令是一样的
command=python /test/wanghaodi/demo/demo.py
numprocs=1
numprocs_start=0
priority=999
; 在 supervisord 启动的时候也自动启动
autostart=true
; 启动 5 秒后没有异常退出，就当作已经正常启动了
startsecs=3
; 启动失败自动重试次数，默认是 3
startretries=3
exitcodes=0,2
stopsignal=QUIT
stopwaitsecs=60
directory=/test/wanghaodi/demo
user=lmb_bi
;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
stopasgroup=false
;默认为false，向进程组发送kill信号，包括子进程
killasgroup=false
redirect_stderr=true
;stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/test/wanghaodi/demo/data.log
stdout_logfile_maxbytes=250MB
stdout_logfile_backups=10
stderr_logfile=/test/wanghaodi/demo/data.err
stderr_logfile_maxbytes=250MB
stderr_logfile_backups=10
; 可以通过 environment 来添加需要的环境变量，一种常见的用法是修改 PYTHONPATH
environment=PYTHONPATH="/test/wanghaodi/demo"
```

>在主配文档中引入test.ini

```bash
;[include]
files = conf.d/*.ini
```

>启动supervisor

```bash
supervisord -c /etc/supervisor/supervisord.conf
```

>查看supervisord.log

## 配置文件参数说明

```bash
[unix_http_server]
file=/tmp/supervisor.sock   ;UNIX socket 文件，supervisorctl 会使用
;chmod=0700                 ;socket文件的mode，默认是0700
;chown=nobody:nogroup       ;socket文件的owner，格式：uid:gid

;[inet_http_server]         ;HTTP服务器，提供web管理界面
;port=127.0.0.1:9001        ;Web管理后台运行的IP和端口，如果开放到公网，需要注意安全性
;username=user              ;登录管理后台的用户名
;password=123               ;登录管理后台的密码

[supervisord]
logfile=/tmp/supervisord.log ;日志文件，默认是 $CWD/supervisord.log
logfile_maxbytes=50MB        ;日志文件大小，超出会rotate，默认 50MB，如果设成0，表示不限制大小
logfile_backups=10           ;日志文件保留备份数量默认10，设为0表示不备份
loglevel=info                ;日志级别，默认info，其它: debug,warn,trace
pidfile=/tmp/supervisord.pid ;pid 文件
nodaemon=false               ;是否在前台启动，默认是false，即以 daemon 的方式启动
minfds=1024                  ;可以打开的文件描述符的最小值，默认 1024
minprocs=200                 ;可以打开的进程数的最小值，默认 200

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ;通过UNIX socket连接supervisord，路径与unix_http_server部分的file一致
;serverurl=http://127.0.0.1:9001 ; 通过HTTP的方式连接supervisord

; [program:xx]是被管理的进程配置参数，xx是进程的名称
[program:xx]
command=/opt/apache-tomcat-8.0.35/bin/catalina.sh run  ; 程序启动命令
autostart=true       ; 在supervisord启动的时候也自动启动
startsecs=10         ; 启动10秒后没有异常退出，就表示进程正常启动了，默认为1秒
autorestart=true     ; 程序退出后自动重启,可选值：[unexpected,true,false]，默认为unexpected，表示进程意外杀死后才重启
startretries=3       ; 启动失败自动重试次数，默认是3
user=tomcat          ; 用哪个用户启动进程，默认是root
priority=999         ; 进程启动优先级，默认999，值小的优先启动
redirect_stderr=true ; 把stderr重定向到stdout，默认false
stdout_logfile_maxbytes=20MB  ; stdout 日志文件大小，默认50MB
stdout_logfile_backups = 20   ; stdout 日志文件备份数，默认是10
; stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/opt/apache-tomcat-8.0.35/logs/catalina.out
stopasgroup=false     ;默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
killasgroup=false     ;默认为false，向进程组发送kill信号，包括子进程

;包含其它配置文件
[include]
files = relative/directory/*.ini    ;可以指定一个或多个以.ini结束的配置文件
```
