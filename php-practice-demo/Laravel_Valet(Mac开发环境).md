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
(确保 ~/.composer/vendor/bin在系统路径中)
```

>配置并安装Valet和DnsMasq，然后注册Valet后台随机启动

```bash
sparsematrix:~ matrix$ valet install
```
