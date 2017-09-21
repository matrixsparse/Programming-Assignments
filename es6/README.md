# ES6构建web项目

```bash
es6
├─app(放置前端代码)
│  ├─css
│  ├─js
│  │  └─class
│  └─views
├─server(服务器目录)
│  ├─bin
│  ├─public
│  │  ├─images
│  │  ├─javascripts
│  │  └─stylesheets
│  ├─routes
│  └─views
└─tasks(构建工具目录)
    └─util
```

## 基础架构

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjq77l7hq9j20mc08xmx9.jpg)

## 任务自动化(gulp)

>安装node

>安装express包

```bash
npm install -g express
npm install -g express-generator
```

>验证express是否安装正确

```bash
express -V
```

```bash
cd es6/server
express -e .[在当前目录使用ejs模板引擎，express是脚手架的启动命令]
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjq868g1iij20qd0iyjsk.jpg)

```bash
cd es6/tasks
mkdir es6/tasks/util
touch es6/tasks/util/args.js
```

```bash
cd es6
npm init
touch .babelrc
touch gulpfile.babel.js
touch tasks/scripts.js
touch tasks/pages.js
```

>使用npm命令安装依赖包

```bash
cd es6
npm install gulp gulp-if gulp-concat webpack webpack-stream vinyl-named gulp-livere load gulp-plumber gulp-rename gulp-uglify gulp-util yargs --save-dev
```

## 编译工具(babel、webpack)

## 代码实现
