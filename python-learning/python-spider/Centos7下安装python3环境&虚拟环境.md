# Centos7下安装python3环境&虚拟环境

## 设置防火墙

### 关闭防火墙

```bash
systemctl stop firewalld.service
```

### 禁止防火墙开机启动

```bash
systemctl disable firewalld.service
```

### 开启端口

```bash
/sbin/iptables -I INPUT -p tcp --dport 80 -j ACCEPT
/sbin/iptables -I INPUT -p tcp --dport 8080 -j ACCEPT
/sbin/iptables -I INPUT -p tcp --dport 8088 -j ACCEPT
```

### 查看正在占用的端口

```bash
netstat -ntlp
```

## 编译安装Python3.6

### 准备编译环境

```bash
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel -y
```

### 下载Python3.5代码包

```bash
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
```

### 编译

```bash
tar -zxvf Python-3.6.3.tgz
cd Python-3.6.3
./configure --prefix=/usr/local/python3
make && make install
```

### 设置环境变量

```bash
echo 'export PATH=$PATH:/usr/local/python3/bin' >> ~/.bashrc
```

## 安装virtualenvwrapper虚拟环境管理器

>切换到当前用户主目录

```bash
cd
```

>安装虚拟环境管理器

```bash
pip install virtualenvwrapper
```

>找到对应的virtualenvwrapper.sh文件的路径

```bash
find / -name virtualenvwrapper.sh
```

### 配置环境变量

```bash
vim ~/.bashrc
```

```bash
export WORKON_HOME=~/.virtualenvs
source /usr/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2
```

```bash
source ~/.bashrc
```

### 创建虚拟环境

>创建python3.6虚拟环境

```bash
mkvirtualenv -p /usr/local/python3/bin/python3 pyenv3.6
```

>创建时效果

```bash
Running virtualenv with interpreter /usr/local/python3/bin/python3
Using base prefix '/usr/local/python3'
New python executable in /root/.virtualenvs/pyenv3.6/bin/python3
Also creating executable in /root/.virtualenvs/pyenv3.6/bin/python
Please make sure you remove any previous custom paths from your /root/.pydistutils.cfg file.
Installing setuptools, pip, wheel...
done.
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv3.6/bin/predeactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv3.6/bin/postdeactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv3.6/bin/preactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv3.6/bin/postactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv3.6/bin/get_env_details
```

>创建python2.7虚拟环境

```bash
mkvirtualenv pyenv2.7
```

>创建时效果

```bash
New python executable in /root/.virtualenvs/pyenv2.7/bin/python2
Also creating executable in /root/.virtualenvs/pyenv2.7/bin/python
Please make sure you remove any previous custom paths from your /root/.pydistutils.cfg file.
Installing setuptools, pip, wheel...done.
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv2.7/bin/predeactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv2.7/bin/postdeactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv2.7/bin/preactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv2.7/bin/postactivate
virtualenvwrapper.user_scripts creating /root/.virtualenvs/pyenv2.7/bin/get_env_details
```

### 退出虚拟环境

```bash
deactivate
```

### 删除虚拟环境

```bash
rmvirtualenv pyenv3.6
```

### 查看当前有哪些虚拟环境

```bash
workon
```

>查询结果

```bash
pyenv2.7
pyenv3.6
```

or

```bash
lsvirtualenv
```

### yum安装rz、sz命令工具

```bash
yum install lrzsz -y
```

### 在指定虚拟环境安装包

#### 进入指定虚拟环境

```bash
workon pyenv3.6
```

#### 查看当前虚拟环境中有哪些安装包

```bash
pip list
```

#### 安装包

```bash
pip install requests
```

#### 卸载包

```bash
pip uninstall requests
```

### 显示所有依赖

```bash
pip freeze
```

### 生成requirement.txt文件

```bash
pip freeze > requirement.txt
```

### 根据requirement.txt生成相同的环境

```bash
pip install -r requirement.txt
```

### 非root用户下配置

```bash
[root@sparsematrix ~]# su matrix
[matrix@sparsematrix ~]$ mkdir ~/.virtualenvs
```

```bash
[matrix@sparsematrix ~]$ vi .bashrc
```

```bash
export WORKON_HOME=$HOME/.virtualenvs
export PATH=$PATH:~/python3
source /usr/bin/virtualenvwrapper.sh > $HOME/.virtualenvs/error.log >/dev/null 2>&1
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python2
```

```bash
[matrix@sparsematrix ~]$ source .bashrc
```

>非roor用户下会报如下错误

```bash
mkdir: 无法创建目录"/root": 权限不够
virtualenvwrapper.user_scripts creating /root/.virtualenvs/premkproject
virtualenvwrapper.user_scripts creating /root/.virtualenvs/initialize
```

```bash
[matrix@sparsematrix ~]$ mkvirtualenv -p /usr/local/python3/bin/python3 pyenv3.6
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flgz4hxniyj21pu0fe7is.jpg)

>不使用系统的包

```bash
[matrix@sparsematrix ~]$ mkvirtualenv --no-site-packages pyenv2.7
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flgz4h4sbbj21rw0feqhe.jpg)

```bash
workon
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flgz48f82aj21i60423zr.jpg)

>在matrix用户下，根据requirement.txt生成相同的环境

遇到安装mysqlclient会出现异常，在文件中删除mysqlclienta安装版本即可

```bash
(pyenv3.6) [matrix@sparsematrix ~]$ pip install -r requirement.txt
```