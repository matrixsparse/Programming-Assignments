# Python Websocket实现

```bash
websocket是一个浏览器和服务器通信的新的协议

一般而言，浏览器和服务器通信最常用的是http协议，

但是http协议是无状态的，每次浏览器请求信息，服务器返回信息后这个浏览器和服务器通信的信道就被关闭了

这样使得服务器如果想主动给浏览器发送信息变得不可能了，

服务器推技术在http时代的解决方案一个是客户端去轮询，或是使用comet技术

而websocket则和一般的socket一样，使得浏览器和服务器建立了一个双工的通道、

具体的websocket协议在rfc6455里面有，这里简要说明一下

websocket通信需要先有个握手的过程，使得协议由http转变为webscoket协议，然后浏览器和服务器就可以利用这个socket来通信了
```

## 安装websocket-client包

```bash
pip install websocket-client
```
