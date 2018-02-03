## 生成SSH密钥

### 查看远程仓库版本

```bash
[root@sparsematrix dms-etl]# git remote -v
origin	git@52.221.152.145:server/dms-etl.git (fetch)
origin	git@52.221.152.145:server/dms-etl.git (push)
```

### 查看所有分支

```bash
[root@sparsematrix dms-etl]# git branch -a
* develop
  master
  tmp
  remotes/origin/HEAD -> origin/master
  remotes/origin/develop
  remotes/origin/master
```

### 查看本地分支

```bash
[root@sparsematrix dms-etl]# git branch
```

### 切换分支到develop

```bash
[root@sparsematrix dms-etl]# git checkout --track remotes/origin/develop
```

>提交文件

```bash
[root@sparsematrix dms-etl]# git add app/Console/Commands/DataWarehouse.php
```

```bash
[root@sparsematrix dms-etl]# git commit -m "数据仓库处理增量数据脚本"
```

>分支推到远程分支

```bash
[root@sparsematrix dms-etl]# git push origin develop
```

### Generate a new SSH key 生成新的 SSH 密钥

```bash
ssh-keygen -t rsa -C "sparsemtarix@163.com"
```

```bash
git config --global user.email 'sparsemtarix@163.com'
or
git config --global user.name "Your Name"
```

### 测试ssh是否配置成功

>测试github ssh是否配置成功

```bash
sparsematrix:~ matrix$ ssh -T git@github.com
```

```bash
The authenticity of host 'github.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
Hi matrixsparse! You've successfully authenticated, but GitHub does not provide shell access.
```

>测试gitlab ssh是否配置成功

```bash
sparsematrix:~ matrix$ ssh -T git@gitlab.com
```

```bash
The authenticity of host 'gitlab.com (52.167.219.168)' can't be established.
ECDSA key fingerprint is SHA256:HbW3g8zUjNSksFbqTiUWPWg2Bq1x8xdGUrliXFzSnUw.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'gitlab.com,52.167.219.168' (ECDSA) to the list of known hosts.
Welcome to GitLab, sparsematrix!
```

## 管理多个SSH秘钥

### 生成一个公司用的SSH-Key

```bash
ssh-keygen -t rsa -C "youremail@your.com" -f ~/.ssh/company-rsa
```

```bash
ssh-add -K ~/.ssh/company-rsa
```

>查看添加结果

```bash
ssh-add -l
```

这里为什么加上了一个-K参数呢？因为在Mac上，当系统重启后会“忘记”这个密钥，所以通过指定-K把SSH key导入到密钥链中

```bash
sparsematrix:~ matrix$ ssh -T matrix.gitlab.com
```
~/.ssh/config
Host 52.221.152.145:88
    HostName 52.221.152.145:88
    User matrix.wang@patpat.com
    PreferredAuthentications publickey
    IdentityFile ~/.ssh/company-rsa

git config --local user.email "matrix.wang@patpat.com"

## Git基本命令

>查看different

```bash
git diff
```
