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

>安装ruby

```bash
brew install ruby@2.3
```

>安装或更新Homebrew到最新版本

```bash
brew update
```

>确保 brew services有效并且能获取到正确的输出，如果无效，则需要添加

```bash
brew services list
```

>通过Homebrew安装PHP 7.0

```bash
brew install php70
```

>通过Composer安装Valet

```bash
composer global require laravel/valet（确保 ~/.composer/vendor/bin在系统路径中）
```

>配置并安装Valet和DnsMasq，然后注册Valet后台随机启动

```bash
valet install
```
