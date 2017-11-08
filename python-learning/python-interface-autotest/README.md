# Python自动化测试接口

## 使用Fiddler抓取接口

### 在Window下

>在cmd命令行中查询无线局域网适配器的IPv4地址

```bash
ipconfig
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flao4k1o5zj20sz05p3yr.jpg)

>在手机所连接的无线局域网设置HTTP代理

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flao9fsjuxj20hr0vkdhu.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flao9fxkawj20hr0vkdhs.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flao9frkwxj20hr0vkwfl.jpg)

### 在Fiddler中设置

>Fiddler Options->Connections

设置连接端口

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flao59vdgkj20ev09xq39.jpg)

>Fiddler Options->HTTPS

默认只抓取HTTP的接口，所以在Fiddler设置也抓取HTTPS接口

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flaojcmhyuj20ev0a10sz.jpg)

设置完后，重启即可

>在浏览器地址栏中访问 无线局域网适配器的IPv4地址:8888 ，安装HTTPS证书
