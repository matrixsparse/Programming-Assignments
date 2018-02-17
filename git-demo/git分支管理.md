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

### 查看当前分支情况

```bash
git branch
```

### 查看服务器远程分支情况

```bash
git branch -a  
```

### checkout命令可用于从历史提交（或者暂存区域）中拷贝文件到工作目录，也可用于切换分支

```bash
git checkout -b [remote branch]
```

### 把当前文件放入暂存区域

```bash
git add [files]
```

### 将远程仓库代码同步到本地/取回远程主机某个分支的更新

```bash
git pull origin master
```

### git用暂存区域的文件创建一个新的提交

```bash
git commit -m "update demo code"
```

### git更改一次提交

```bash
git commit --amend -m "use git demo code"
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

## Merge

merge 命令把不同分支合并起来。合并前，索引必须和当前提交相同。如果另一个分支是当前提交的祖父节点，那么合并命令将什么也不做

另一种情况是如果当前提交是另一个分支的祖父节点，就导致fast-forward合并。指向只是简单的移动，并生成一个新的提交

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fojvfrd2pnj21100m640h.jpg)

>切换到master分支

```bash
sparsematrix:infrastructure matrix$ git checkout master
D	README
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
```

>查看当前本地分支

```bash
sparsematrix:infrastructure matrix$ git branch
  develop
* master
```

>合并分支

```bash
sparsematrix:infrastructure matrix$ git merge develop
Updating a574583..c3c038b
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 README.md
```

>将本地代码同步到远程仓库

```bash
sparsematrix:infrastructure matrix$ git push origin master
Total 0 (delta 0), reused 0 (delta 0)
To gitlab.com:clapclap/infrastructure.git
   a574583..c3c038b  master -> master
```
