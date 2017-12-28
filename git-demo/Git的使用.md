
## git拉取github上的项目

### 配置本地仓库的账号和邮箱

```bash
git config --global user.email "email@github.com"
```

```bash
cd C:\Users\Administrator
ssh-keygen -t rsa -C "youremail@github.com"
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjke6fjiylj20tp0f5wg0.jpg)

### 在Github上设置ssh秘钥

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjkeas0x3xj20nt0c0ab3.jpg)

### 克隆项目

```bash
git clone git@github.com:matrixsparse/Practice-Demo.git
```

### 与origin master建立连接

```bash
git remote add origin git@github.com:matrixsparse/Practice-Demo.git
```

### 查看本地分支文件信息，确保更新时不产生冲突

```bash
git status
```

### 若文件有修改，可以还原到最初状态; 若文件需要更新到服务器上，应该先merge到服务器，再更新到本地

```bash
git checkout -- [file name]
```

### 查看当前分支情况

```bash
git branch
```

### 若分支为本地分支，则需切换到服务器的远程分支

```bash
git checkout [remote branch]
```

### 将远程仓库代码同步到本地/取回远程主机某个分支的更新

```bash
git pull origin master
```

### 将本地代码同步到远程仓库

```bash
git push -u origin master
```

### 本地删除文件夹、文件同步更新远程仓库

```bash
rm alipay
```

>只会处理已修改或者已删除的文件，但不会处理新建的文件

```bash
git add -u
```

```bash
git commit -m "delete test"
```

```bash
git push -u origin master
```