# Vue-Demo

## Vue功能

* 模板渲染
* 模块化
* 拓展功能
  * 路由
  * ajax

## 什么是Vue.js

```bash
轻量级的前端界面框架
实现数据渲染/同步
组件化/模块化
路由
ajax
数据流管理
```

## Vue.js学习资源

* [vuejs中文官网](http://cn.vuejs.org/)
* [vuejs源码](https://github.com/vuejs/vue)
* [vuejs官方工具](https://github.com/vuejs)

## Vue特点

* 响应式 - 双向数据绑定[js里的数据一改变，展现层数据也会跟着改变]
  * Js和html之间会有很多交互，比如js获取html的字段，或者用户通过html输入的一些数据要反映到js里，功能和展现之间会有很多交互，当这些交互变得复杂起来的时候，会非常难以控制，如果没有一个很好的规划，越到开发后面项目会变得非常的杂乱。`前端框架可以将常用的交互操作进行抽象，使用框架提供的功能、属性、js对象来实现展现数据和js之间的交互`
* 组件化 - 模块化
  * 组件与组件之间实现解耦
* 单文件组件 - js，css，html存在于一个文件内
  * Webpack + vue-loader
  * Browserify + vueify

## Webpack简介

```bash
Webpack是当下最热门的前端资源模块化管理和打包工具，它可以将很多松散的模块按照依赖和规则打包成符合生产环境部署的前端资源，还可以将按需加载的模块进行代码分割，等到实际需要的时候再异步加载。
通过loader的转换，任何形式的资源都可以视作模块，比如CommonJs模块、AMD模块、ES6模块、CSS、图片、JSON、Coffeescript、LESS等。

下图是官方对Webpack的简介，通过这幅图也不难看出，一些相互依赖的模块文件，会被打包成一个或多个js文件，可以减少HTTP的请求次数
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjv1u8sn3jj21n40okwhx.jpg)

## -save和save-dev区别

```bash
-save和save-dev可以省掉你手动修改package.json文件的步骤。
npm install module-name -save 自动把模块和版本号添加到dependencies部分
npm install module-name -save-dev 自动把模块和版本号添加到devdependencies部分
```

## 环境准备

```bash
node和git是必备的工具，NPM的版本最好是3.x版本以上，NPM 3.x提供了更有效的包依赖管理。
```

### 安装vue cli

```bash
npm install -g vue-cli
```

```bash
安装vue cli后，就可以基于vue-webpack-simple模板和vue-webpack模板创建项目
```

## 使用vue-webpack-simple模板

>webpack-simple是项目模板的名称，vue-demo是要生成的项目名称

```bash
vue init webpack-simple vue-simple-demo
```

>目录下生成了一个文件夹vue-simple-demo

```bash
sparsematrix:vue-project matrix$ ll
total 16
-rw-r--r--  1 matrix  staff  2644  9 24 23:10 README.md
drwxr-xr-x  9 matrix  staff   306  9 24 23:11 vue-simple-demo
```

### 项目结构说明

>打开vue-simple-demo文件夹，看到以下目录结构

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjv25jrl4zj20g20eowfl.jpg)

```bash
├─.babelrc		// babel配置文件
├─.gitignore	
├─index.html		// 主页
├─package.json		// 项目配置文件
├─README.md  
├─webpack.config.js	// webpack配置文件
├─dist			// 发布目录
│   ├─.gitkeep       
├─src			// 开发目录	
│   ├─App.vue		// App.vue组件
│   ├─main.js		// 预编译入口
```

### 安装项目依赖

```bash
cd vue-simple-demo
npm install
```

### 运行示例

```bash
npm run dev
```

### 发布

>执行以下命令会生成发布时的build.js，并且是经过压缩的

```bash
npm run build
```

## 使用vue-webpack模板

>webpack是项目模板，vue-webpack-demo是项目名称

```bash
vue init webpack vue-webpack-demo
```

### 安装依赖

```bash
cd vue-webpack-demo
npm install
```

### 运行示例

```bash
npm run dev
```

### 发布

```bash
npm run build
```