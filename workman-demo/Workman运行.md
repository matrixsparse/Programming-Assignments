## 源码编译安装（一般是安装PHP自带的扩展，以安装pcntl扩展为例）

### 利用php -v命令查看当前的PHP CLI的版本
```bash
php -v
```
### 根据版本下载PHP源代码
```bash
PHP历史版本下载页面：http://php.net/releases/
```
### 解压源码压缩包
```bash
tar -zxvf php-5.3.29.tar.gz
```
### 进入源码中的ext/pcntl目录
```bash
cd php-5.3.29/ext/pcntl/
```
### 运行phpize命令

>安装phpize

```bash
yum install php-devel -y
```

>查看phpize安装目录

```bash
which phpize
```

>运行phpize命令

```bash
phpize
```

### 运行configure命令

```bash
./configure
```

### 运行make命令

```bash
make
```

>可能报错

```bash
error: 'PHP_FE_END' undeclared here (not in a function)
```

>解决方法：

```bash
源代码有错误，进入php解压缩（本例中是/root/php-5.3.29/）目录
sed -i 's|PHP_FE_END|{NULL,NULL,NULL}|' ./ext/**/*.c
sed -i 's|ZEND_MOD_END|{NULL,NULL,NULL}|' ./ext/**/*.c
```

### 运行make install命令

```bash
make install
```

### 配置ini文件

>查找php.ini文件位置

```bash
php --ini
```

>编辑php.ini文件，在文件中添加extension=pcntl.so

```bash
extension=pcntl.so
```

```bash
说明： 此方法一般用来安装PHP自带的扩展，例如posix扩展和pcntl扩展
除了用phpize编译某个扩展，也可以重新编译整个PHP，在编译时用参数添加扩展，例如在源码根目录运行
```

```bash
./configure --enable-pcntl --enable-posix ...
make && make install
```
