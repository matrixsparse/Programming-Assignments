
## Generate a new SSH key 生成新的 SSH 密钥

```bash
ssh-keygen -t rsa -C "sparsemtarix@163.com"
```

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## Test everything out 测试

打开 Git Bash 输入:

```bash
$ ssh -T git@github.com
# Attempts to ssh to github
```

看到如下警告

```bash
The authenticity of host 'github.com (192.30.255.112)' can't be established.
RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)? yes
输入"yes"
```

```bash
Hi matrixsparse! You've successfully authenticated, but GitHub does not provide shell access.
```