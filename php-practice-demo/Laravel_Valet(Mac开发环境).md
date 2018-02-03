# Laravel Valet（Mac开发环境）

Valet是为Mac提供的极简主义开发环境，没有Vagrant、Apache、Nginx，也没有/etc/hosts文件，甚至可以使用本地隧道公开共享你的站点

在Mac中，当你启动机器时，Laravel Valet总是在后台运行PHP内置的Web服务器，然后通过使用DnsMasq，Valet将所有请求代理到*.dev域名并指向本地机器安装的站点。这样一个极速的Laravel开发环境只需要占用7M内存。

Valet并不是想要替代Vagrant或者Homestead，只是提供了另外一种选择，更加灵活、极速、以及占用更小的内存空间

Valet为我们提供了以下软件和工具
* Laravel
* Lumen
* Statamic
* Craft
* WordPress
* Jigsaw
* 静态HTML
你还可以通过自定义的驱动扩展Valet

## 安装

>安装ruby

```bash
sparsematrix:~ matrix$ brew install ruby@2.3
```

>安装或更新Homebrew到最新版本

```bash
sparsematrix:~ matrix$ brew update
```

>确保 brew services有效并且能获取到正确的输出，如果无效，则需要添加

```bash
sparsematrix:~ matrix$ brew services list
```

>通过Homebrew安装PHP 7.0

```bash
sparsematrix:~ matrix$ brew install homebrew/php/php70
```

```bash
sparsematrix:~ matrix$ vim ~/.bash_profile
export PATH="$(brew --prefix homebrew/php/php70)/bin:$PATH"
sparsematrix:~ matrix$ source ~/.bash_profile
```

>安装php－version(php版本切换工具)

```bash
sparsematrix:~ matrix$ brew install homebrew/php/php-version
```

```bash
sparsematrix:~ matrix$ vim ~/.bash_profile
source $(brew --prefix php-version)/php-version.sh && php-version 7
sparsematrix:~ matrix$ source ~/.bash_profile
```

>查看已存在的php版本,前面带＊的是当前环境正在使用的php版本,使用php－versiom＋版本号的方式切换php版本

```bash
sparsematrix:~ matrix$ php-version
* 7.0.27
```

```bash
sparsematrix:~ matrix$ php --version
PHP 7.0.27 (cli) (built: Jan  5 2018 12:24:33) ( NTS )
Copyright (c) 1997-2017 The PHP Group
Zend Engine v3.0.0, Copyright (c) 1998-2017 Zend Technologies
```

>安装composer

```bash
sparsematrix:~ matrix$ brew install composer
```

升级composer到最新版本

```bash
sparsematrix:~ matrix$ composer self-update
```

```bash
sparsematrix:~ matrix$ composer self-update --update-keys
```

```bash
sparsematrix:~ matrix$ composer diag
Checking platform settings: OK
Checking git settings: OK
Checking http connectivity to packagist: OK
Checking https connectivity to packagist: OK
Checking github.com rate limit: OK
Checking disk free space: OK
Checking pubkeys:
Tags Public Key Fingerprint: 4AC45767 E5EC2265 2F0C1167 CBBB8A2B  0C708369 153E328C AD90147D AFE50952
Dev Public Key Fingerprint: 4AC45767 E5EC2265 2F0C1167 CBBB8A2B  0C708369 153E328C AD90147D AFE50952
OK
Checking composer version: OK
Composer version: 1.6.3
PHP version: 7.0.27
PHP binary path: /usr/local/Cellar/php70/7.0.27_19/bin/php
```

>通过Composer安装Valet

```bash
sparsematrix:~ matrix$ composer global require laravel/valet
```

>确保 ~/.composer/vendor/bin在系统路径中

```bash
export PATH="$HOME/.composer/vendor/bin:$PATH"
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo1gej8xbrj21rm0zq1kx.jpg)

>配置并安装Valet和DnsMasq，然后注册Valet后台随机启动

```bash
sparsematrix:~ matrix$ valet install
Stopping nginx...
Installing nginx...
[nginx] is not installed, installing it now via Brew... 🍻
Installing nginx configuration...
Installing nginx directory...
Updating PHP configuration...
Restarting php70...
Installing dnsmasq...
[dnsmasq] is not installed, installing it now via Brew... 🍻
Restarting dnsmasq...
Restarting nginx...

Valet installed successfully!
```

安装完Valet后，尝试使用命令如 ping foobar.dev在终端ping一下任意*.dev域名，如果Valet安装正确就会看到来自127.0.0.1的响应

```bash
valet domain dev
```

```bash
ping foobar.dev
```

```bash
sparsematrix:~ matrix$ ping foobar.dev
PING foobar.dev (127.0.0.1): 56 data bytes
64 bytes from 127.0.0.1: icmp_seq=0 ttl=64 time=0.045 ms
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.055 ms
64 bytes from 127.0.0.1: icmp_seq=2 ttl=64 time=0.058 ms
64 bytes from 127.0.0.1: icmp_seq=3 ttl=64 time=0.055 ms
```

每次系统启动的时候Valet后台会自动启动，而不需要再次手动运行valet start或valet install

## 服务站点

Valet安装完成后，就可以启动服务站点，Valet为此提供了两个命令：park和link

### park命令

在Mac中创建一个新目录

```bash
sparsematrix:~ matrix$ mkdir ~/Sites
sparsematrix:~ matrix$ cd Sites
```

进入这个目录并运行

```bash
sparsematrix:Sites matrix$ valet park
This directory has been added to Valet's paths.
```

这个命令会将当前所在目录作为web根目录

>在此目录下创建Laravel项目

```bash
composer create-project laravel/laravel --prefer-dist laravel
```

>在浏览器中访问 http://laravel.dev

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fo1i43bus2j22kc11e77i.jpg)

>停止某个 laravel.dev 的域名

```bash
cd ~/Sites/laravel
Valet stop
```

### link命令

link命令也可以用于本地Laravel站点，这个命令在你想要在目录中提供单个站点时很有用

要使用这个命令，先切换到你的某个项目并运行 valet link app-name，这样Valet会在 ~/.valet/Sites中创建一个符号链接指向当前工作目录

运行完link命令后，可以在浏览器中通过 http://app-name.dev访问

要查看所有的链接目录，可以运行 valet links命令。你也可以通过 valet unlink app-name来删除符号链接

### 使用其它域名

默认情况下，Valet 使用 .test 顶级域名为你的项目提供服务。如果你想使用其他域名，可以使用 valet domain tld-name 命令

例如，如果你要使用 .app 而不是 .test，就运行 valet domain app，Valet 会自动将站点域名改为 *.app

```bash
valet domain dev
```

## 其他Valet命令

```bash
valet forget	从"parked"目录运行该命令以便从parked目录列表中移除该目录
valet paths	查看你的”parked”路径
valet restart	重启Valet
valet start	启动Valet
valet stop	关闭Valet
valet uninstall	卸载Valet
```

## Mac下运行PHP Laravel项目

>进入目录

```bash
cd dms-etl
```

>创建目录，并赋予777权限

```bash
sparsematrix:dms-etl matrix$ mkdir -p storage/framework/sessions
sparsematrix:dms-etl matrix$ mkdir -p storage/framework/views
sparsematrix:dms-etl matrix$ mkdir -p storage/framework/cache
sparsematrix:dms-etl matrix$ sudo chmod 777 storage/*
```

>查看Laravel版本

```bash
sparsematrix:dms-etl matrix$ php artisan -V
Laravel Framework version 5.2.45
```

```bash
[root@sparsematrix dms]# cp .env.example .env
```

```bash
[root@sparsematrix dms]# composer install
```

>安装node相关模块

```bash
sparsematrix:dms-etl matrix$ npm install
```

>安装gulp

```bash
sparsematrix:dms-etl matrix$ npm install -g gulp
sparsematrix:dms-etl matrix$ npm install -g gulp-notify
```

>运行gulp进行压缩

```bash
sparsematrix:dms-etl matrix$ gulp
```
