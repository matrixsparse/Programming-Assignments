## 下载
```bash
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
```
## 解压压缩文件到指定目录
```bash
tar -xvzf Python-3.6.3.tgz -C /usr/local
```
## 重命名
```bash
mv Python-3.6.3 python3
```
## 编译
```bash
cd python3
./configure --prefix=/usr/local/python3
```
## 安装
```bash
make
```
```bash
make install
```
## 删除软连接
```bash
rm -rf /usr/bin/python
ln -s /usr/local/python3/bin/python3 /usr/bin/python
```
