
## 使用virtualenv来管理环境
```bash
virtualenv是一个能把你的应用隔离在一个虚拟环境中的工具
一个虚拟环境是一个包含了你的应用依赖的软件的文件夹
一个虚拟环境同时也封存了你在开发时的环境变量

与其把依赖包，比如Flask，下载到你的系统包管理文件夹，或用户包管理文件夹，我们可以把它下载到对应当前应用的一个隔离的文件夹之下
这使得你可以指定一个特定的Python二进制版本，取决于当前开发的项目

virtualenv也可以让你给不同的项目指定同样的依赖包的不同版本。 当你在一个老旧的包含众多不同项目的平台上开发时，这种灵活性十分重要

用了virtualenv，你将只会把少数几个Python模块安装到系统的全局空间中。其中一个会是virtualenv本身
```
### 安装virtualenv
```bash
pip install virtualenv
```
### 创建虚拟环境
```bash
切换到你的项目文件夹，运行virtualenv命令。这个命令接受一个参数，作为虚拟环境的名字
```
```bash
virtualenv -p /usr/local/python3/bin/python3 py3.6
```
### 安装虚拟环境管理器
>安装virtualenvwrapper
```bash
pip install virtualenvwrapper
```
```bash
为了wrapper可以正常在环境中工作，因此需要一个隐藏文件夹.virtualenv
vw可以进行环境的管理，把创建的环境记录下来，并进行管理
```
>创建目录存放虚拟环境
```bash
cd
mkdir ~/.virtualenvs
```
>在.bashrc中末尾添加
```bash
export WORKON_HOME=~/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```
>让配置生效
```bash
source ~/.bashrc
```
