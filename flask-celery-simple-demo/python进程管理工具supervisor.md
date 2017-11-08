# Python进程管理工具Supervisor

## Linux下安装pip

```bash
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip -V　　#查看pip版本
```

```bash
Supervisor是基于Python的进程管理工具，可以更简单的监听、启停、重启服务器上的一个或多个后台进程，是Linux服务器管理的高效工具

Supervisor管理的进程，当一个进程意外被杀死，supervisort监听到进程挂掉后，会自动将它重新拉起
其进程自动恢复的功能，不再需要自己写shell脚本来控制
```

>Supervisor 有两个主要的组成部分：

* supervisord，运行Supervisor时会启动一个进程supervisord，它负责启动所管理的进程，并将所管理的进程作为自己的子进程来启动，而且可以在所管理的进程出现崩溃时自动重启

* supervisorctl，是命令行管理工具，可以用来执行stop、start、restart等命令，来对这些子进程进行管理

## 安装setuptools

```bash
wget --no-check-certificate https://pypi.python.org/packages/source/s/setuptools/setuptools-12.0.3.tar.gz#md5=f07e4b0f4c1c9368fcd980d888b29a65
tar -zxvf setuptools-12.0.3.tar.gz
cd setuptools-12.0.3
python setup.py install
```

## 安装pip

```bash
easy_install pip
```

## 安装supervisor

```bash
easy_install supervisor
```

## 测试是否安装成功

```bash
echo_supervisord_conf
```

## 创建配置文件

```bash
echo_supervisord_conf > /etc/supervisord.conf
```

>如果出现没有权限的问题，可以使用这条命令

```bash
sudo su - root -c "echo_supervisord_conf > /etc/supervisord.conf"
```

> supervisor安装完成后会生成三个执行程序：
* supervisortd【supervisor的守护进程服务（用于接收进程管理命令）】
* supervisorctl【客户端（用于和守护进程通信，发送管理进程的指令）】
* echo_supervisord_conf【生成初始配置文件程序】

## 配置文件说明

```bash
想要了解怎么配置需要管理的进程，只要打开 supervisord.conf 就可以了，里面有很详细的注释信息
```

打开配置文件

```bash
vim /etc/supervisord.conf
```

```bash
默认的配置文件是下面这样的，但是这里有个坑需要注意，supervisord.pid 以及 supervisor.sock 是放在 /tmp 目录下

但是 /tmp 目录是存放临时文件，里面的文件是会被 Linux 系统删除的

一旦这些文件丢失，就无法再通过 supervisorctl 来执行 restart 和 stop 命令了，

将只会得到 unix:///tmp/supervisor.sock 不存在的错误
```

```bash
因此可以单独建一个文件夹，来存放这些文件，比如放在 /etc/supervisord.d/
```

```bash
默认情况下，进程的日志文件达到50MB时，将进行分割，最多保留10个文件，当然这些配置也可以对每个进程单独配置
```

>创建文件夹

```bash
mkdir -p /etc/supervisord.d
```

>创建日志目录

```bash
mkdir -p /var/log/supervisor/
```

>supervisord.conf

```bash
; Sample supervisor config file.
;
; For more information on the config file, please see:
; http://supervisord.org/configuration.html
;
; Notes:
;  - Shell expansion ("~" or "$HOME") is not supported.  Environment
;    variables can be expanded using this syntax: "%(ENV_HOME)s".
;  - Quotes around values are not supported, except in the case of
;    the environment= options as shown below.
;  - Comments must have a leading space: "a=b ;comment" not "a=b;comment".
;  - Command will be truncated if it looks like a config file comment, e.g.
;    "command=bash -c 'foo ; bar'" will truncate to "command=bash -c 'foo ".

[unix_http_server]
; 修改为/etc/supervisord.d目录，避免被系统删除
file=/etc/supervisord.d/supervisor.sock   ; the path to the socket file
;chmod=0700                 ; socket file mode (default 0700)
;chown=nobody:nogroup       ; socket file uid:gid owner
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)

;[inet_http_server]         ; inet (TCP) server disabled by default
;port=127.0.0.1:9001        ; ip_address:port specifier, *:port for all iface
;username=user              ; default is no username (open server)
;password=123               ; default is no password (open server)

[supervisord]
; logfile=/tmp/supervisord.log ; main log file; default $CWD/supervisord.log
; 修改为 /var/log 目录，避免被系统删除
logfile=/var/log/supervisor/supervisord.log ;
; 日志文件多大时进行分割
logfile_maxbytes=50MB        ; max main logfile bytes b4 rotation; default 50MB
; 最多保留多少份日志文件
logfile_backups=10           ; # of main logfile backups; 0 means none, default 10
loglevel=info                ; log level; default info; others: debug,warn,trace
; 修改为/etc/supervisord.d目录，避免被系统删除
pidfile=/etc/supervisord.d/supervisord.pid ; supervisord pidfile; default supervisord.pid
nodaemon=false               ; start in foreground if true; default false
minfds=1024                  ; min. avail startup file descriptors; default 1024
minprocs=200                 ; min. avail process descriptors;default 200
;umask=022                   ; process file creation umask; default 022
; 设置启动supervisord的用户，一般情况下不要轻易用root用户来启动，除非你真的确定要这么做
user=root                 ; default is current user, required if root
;identifier=supervisor       ; supervisord identifier, default is 'supervisor'
;directory=/tmp              ; default is not to cd during start
;nocleanup=true              ; don't clean up tempfiles at start; default false
;childlogdir=/tmp            ; 'AUTO' child log dir, default $TEMP
;environment=KEY="value"     ; key value pairs to add to environment
;strip_ansi=false            ; strip ansi escape codes in logs; def. false

; The rpcinterface:supervisor section must remain in the config file for
; RPC (supervisorctl/web interface) to work.  Additional interfaces may be
; added by defining them in separate [rpcinterface:x] sections.

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

; The supervisorctl section configures how supervisorctl will connect to
; supervisord.  configure it match the settings in either the unix_http_server
; or inet_http_server section.

[supervisorctl]
; 必须和'unix_http_server'里面的设定匹配
; 修改为/etc/supervisor目录，避免被系统删除
;serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
serverurl=unix:///etc/supervisord.d/supervisor.sock ;
;serverurl=http://127.0.0.1:9001 ; use an http:// url to specify an inet socket
;username=chris              ; should be same as in [*_http_server] if set
;password=123                ; should be same as in [*_http_server] if set
;prompt=mysupervisor         ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history  ; use readline history if available

; The sample program section below shows all possible program subsection values.
; Create one or more 'real' program: sections to be able to control them under
; supervisor.

;[program:theprogramname]
;command=/bin/cat              ; the program (relative uses PATH, can take args)
;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
;numprocs=1                    ; number of processes copies to start (def 1)
;directory=/tmp                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=999                  ; the relative start priority (default 999)
;autostart=true                ; start at supervisord start (default: true)
;startsecs=1                   ; # of secs prog must stay up to be running (def. 1)
;startretries=3                ; max # of serial start failures when starting (default 3)
;autorestart=unexpected        ; when to restart if exited after running (def: unexpected)
;exitcodes=0,2                 ; 'expected' exit codes used with autorestart (default 0,2)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; setuid to this UNIX account to run the program
;redirect_stderr=true          ; redirect proc stderr to stdout (default false)
;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stdout_logfile_backups=10     ; # of stdout logfile backups (0 means none, default 10)
;stdout_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (0 means none, default 10)
;stderr_capture_maxbytes=1MB   ; number of bytes in 'capturemode' (default 0)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;environment=A="1",B="2"       ; process environment additions (def no adds)
;serverurl=AUTO                ; override serverurl computation (childutils)

; The sample eventlistener section below shows all possible eventlistener
; subsection values.  Create one or more 'real' eventlistener: sections to be
; able to handle event notifications sent by supervisord.

;[eventlistener:theeventlistenername]
;command=/bin/eventlistener    ; the program (relative uses PATH, can take args)
;process_name=%(program_name)s ; process_name expr (default %(program_name)s)
;numprocs=1                    ; number of processes copies to start (def 1)
;events=EVENT                  ; event notif. types to subscribe to (req'd)
;buffer_size=10                ; event buffer queue size (default 10)
;directory=/tmp                ; directory to cwd to before exec (def no cwd)
;umask=022                     ; umask for process (default None)
;priority=-1                   ; the relative start priority (default -1)
;autostart=true                ; start at supervisord start (default: true)
;startsecs=1                   ; # of secs prog must stay up to be running (def. 1)
;startretries=3                ; max # of serial start failures when starting (default 3)
;autorestart=unexpected        ; autorestart if exited after running (def: unexpected)
;exitcodes=0,2                 ; 'expected' exit codes used with autorestart (default 0,2)
;stopsignal=QUIT               ; signal used to kill process (default TERM)
;stopwaitsecs=10               ; max num secs to wait b4 SIGKILL (default 10)
;stopasgroup=false             ; send stop signal to the UNIX process group (default false)
;killasgroup=false             ; SIGKILL the UNIX process group (def false)
;user=chrism                   ; setuid to this UNIX account to run the program
;redirect_stderr=false         ; redirect_stderr=true is not allowed for eventlisteners
;stdout_logfile=/a/path        ; stdout log path, NONE for none; default AUTO
;stdout_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stdout_logfile_backups=10     ; # of stdout logfile backups (0 means none, default 10)
;stdout_events_enabled=false   ; emit events on stdout writes (default false)
;stderr_logfile=/a/path        ; stderr log path, NONE for none; default AUTO
;stderr_logfile_maxbytes=1MB   ; max # logfile bytes b4 rotation (default 50MB)
;stderr_logfile_backups=10     ; # of stderr logfile backups (0 means none, default 10)
;stderr_events_enabled=false   ; emit events on stderr writes (default false)
;environment=A="1",B="2"       ; process environment additions
;serverurl=AUTO                ; override serverurl computation (childutils)

; The sample group section below shows all possible group values.  Create one
; or more 'real' group: sections to create "heterogeneous" process groups.

;[group:thegroupname]
;programs=progname1,progname2  ; each refers to 'x' in [program:x] definitions
;priority=999                  ; the relative start priority (default 999)

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

[include]
files = /etc/supervisord.d/config/*.ini
```

### 使用include

```bash
在配置文件的最后，有一个 [include] 的配置项，跟 Nginx 一样，可以 include 某个文件夹下的所有配置文件，这样我们就可以为每个进程或相关的几个进程的配置单独写成一个文件
```

```bash
[include]
files = /etc/supervisord.d/config/*.ini
```

### 创建进程的配置文件

>编辑/etc/supervisord.d/config/matrix.ini

```bash
[group:matrix]
programs = matrix.print

[program:matrix.print]
; 启动命令，可以看出与手动在命令行启动的命令是一样的
command=python /data/demo/demo.py
numprocs=1
numprocs_start=0
priority=999
; 在supervisord启动的时候也自动启动
autostart=true
; 启动3秒后没有异常退出，就当作已经正常启动了
startsecs=3
; 启动失败自动重试次数，默认是3
startretries=3
exitcodes=0,2
stopsignal=QUIT
stopwaitsecs=60
directory=/data/demo
user=root
; 默认为false,进程被杀死时，是否向这个进程组发送stop信号，包括子进程
stopasgroup=false
; 默认为false，向进程组发送kill信号，包括子进程
killasgroup=false
redirect_stderr=true
;stdout 日志文件，需要注意当指定目录不存在时无法正常启动，所以需要手动创建目录（supervisord 会自动创建日志文件）
stdout_logfile=/data/demo/data.log
; 日志文件多大时进行分割
stdout_logfile_maxbytes=250MB
; 最多保留多少份日志文件
stdout_logfile_backups=10
stderr_logfile=/data/demo/data.err
stderr_logfile_maxbytes=250MB
stderr_logfile_backups=10
; 可以通过 environment 来添加需要的环境变量，一种常见的用法是修改 PYTHONPATH
environment=PYTHONPATH="/data/demo"
```

>创建测试脚本&日志目录

```bash
mkdir -p /data/demo
```

>/data/demo/demo.py

```bash
vi /data/demo/demo.py
```

```bash
# -*- coding: utf-8 -*-
import os
import time

while 1:
   f = open('data.log', 'a+')
   time.sleep(5)
   f.write('This is a Test!')
```

## 启动supervisor

```bash
supervisord -c /etc/supervisord.conf
```

### 查看supervisor是否启动成功

```bash
ps -ef | grep '/etc/supervisord.conf'
```

```bash
root     23542     1  0 17:46 ?        00:00:00 /usr/bin/python /usr/bin/supervisord -c /etc/supervisord.conf
root     23566 23079  0 17:54 pts/0    00:00:00 grep /etc/supervisord.conf
```

### 查看supervisord.log

```bash
tail -f /var/log/supervisor/supervisord.log
```

```bash
2017-10-31 17:46:18,672 CRIT Set uid to user 0
2017-10-31 17:46:18,678 INFO RPC interface 'supervisor' initialized
2017-10-31 17:46:18,678 CRIT Server 'unix_http_server' running without any HTTP authentication checking
2017-10-31 17:46:18,679 INFO daemonizing the supervisord process
2017-10-31 17:46:18,679 INFO supervisord started with pid 23542
2017-10-31 17:48:14,042 INFO spawned: 'matrix.print' with pid 23555
2017-10-31 17:48:17,047 INFO success: matrix.print entered RUNNING state, process has stayed up for > than 3 seconds (startsecs)
```

## supervisord.conf配置文件参数说明

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

## supervisorctl命令介绍

```bash
# 停止某一个进程，program_name 为 [program:x] 里的 x
supervisorctl stop program_name
# 启动某个进程
supervisorctl start program_name
# 重启某个进程
supervisorctl restart program_name
# 结束所有属于名为 groupworker 这个分组的进程 (start，restart 同理)
supervisorctl stop groupworker:
# 结束 groupworker:name1 这个进程 (start，restart 同理)
supervisorctl stop groupworker:name1
# 停止全部进程，注：start、restart、stop 都不会载入最新的配置文件
supervisorctl stop all
# 载入最新的配置文件，停止原有进程并按新的配置启动、管理所有进程
supervisorctl reload
# 根据最新的配置文件，启动新配置或有改动的进程，配置没有改动的进程不会受影响而重启
supervisorctl update
# 查看进程的状态
supervisorctl status
```

>查看进程状态

```bash
supervisorctl status
```

```bash
matrix:matrix.print              RUNNING   pid 23555, uptime 0:10:00
```

## 查看supervisord所在路径

```bash
which supervisord
```

## 使用浏览器来管理

```bash
supervisor 同时提供了通过浏览器来管理进程的方法，只需要注释掉如下几行就可以了
```

```bash
;[inet_http_server]         ; inet (TCP) server disabled by default
;port=192.168.3.244:9001        ; (ip_address:port specifier, *:port for ;all iface)
;username=user              ; (default is no username (open server))
;password=123               ; (default is no password (open server))
[supervisorctl]
...
;serverurl=http://192.168.3.244:9001 ; use an http:// url to specify an inet socket
;username=chris              ; should be same as http_username if set
;password=123                ; should be same as http_password if set
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flajqtxissj20ot037glm.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flajqtbr0bj20qg06yaak.jpg)

>访问浏览器地址栏：http://192.168.3.244:9001/

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fl1lvrh2stj20ws07mt98.jpg)

## 开机自动启动Supervisord

```bash
Linux在启动的时候会执行/etc/rc.local里面的脚本，所以在这里添加执行命令就可以
```

```bash
# 如果是 Ubuntu 添加以下内容
/usr/local/bin/supervisord -c /etc/supervisord.conf
```

```bash
# 如果是 Centos 添加以下内容
/usr/bin/supervisord -c /etc/supervisord.conf
```

### 启用rc.local服务

```bash
sudo systemctl enable rc-local.service
```
