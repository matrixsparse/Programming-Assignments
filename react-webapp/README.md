# React-WebApp

## Vue和React对比

```bash
Angular提供的更多是一整套解决方案，后者更像是一个生态
Vue和React目前都使用了Virtual Dom
```

## Vue框架对比

>Vue

```bash
模板和渲染函数的弹性选择
简单的语法及项目创建
更快的渲染速度和更小的体积
```

>React

```bash
更适用于大型应用和更好的可测试性
同时适用于Web端和原生App
更大的生态圈带来更多支持和工具
```

## Vue和React相同点

* 利用虚拟DOM[在内存中操作快]实现快速渲染
* 轻量级
* 响应式组件
* 服务器端渲染
* 易于集成路由工具，打包工具以及状态管理工具
* 优秀的支持和社区

## 安装node.js

```bash
npm -v
3.10.10
```

## 创建项目

```bash
mkdir react-demo
```

## npm初始化

```bash
cd react-demo
npm init
```

```bash
vi package.json
{
  "name": "react-demo",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```

## 安装插件

>安装webpack相关插件

```bash
npm install webpack webpack-dev-server --save-dev
```

>安装react相关插件

```bash
npm install react react-dom --save
```

```bash
安装完成后，查看package.json，发现多了devDependencies和dependencies两项，根目录也多了一个node_modules文件夹
```

## --save和--save-dev的区别

```bash
npm i 时 --save
```