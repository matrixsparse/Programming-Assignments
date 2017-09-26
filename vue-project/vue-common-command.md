# vue-common-command

## Vue常用指令

```bash
Vue.js的指令是以v-开头的，它们作用于HTML元素，指令提供了一些特殊的特性，将指令绑定在元素上时，指令会为绑定的目标元素添加一些特殊的行为，
我们可以将指令看作特殊的HTML特性（attribute）
```

>Vue.js提供了一些常用的内置指令

* v-if[条件渲染指令，它根据表达式的真假来删除和插入元素]
* v-show
* v-else
* v-for
* v-bind
* v-on
* v-model[在表单元素上创建双向数据绑定]


```bash
v-if="expression"
expression是一个返回bool值的表达式，表达式可以是一个bool属性，也可以是一个返回bool的运算式
```

### v-if示例

>cmd/if.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
          }
          #if_data{
            width: 400px;
            height: 500px;
            margin:100px auto;
          }
          #if_data p{
            font-size: 16px;
            font-family: "微软雅黑";
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="if_data">
            <h1>Hello,Vue.js!</h1>
            <h1 v-if="yes">Yes!</h1>
            <h1 v-if="no">No!</h1>
            <h1 v-if="age >= 25 ">Age：{{ age }}!</h1>
            <h1 v-if="name.indexOf('jack') >= 0">Name：{{ name }}</h1>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var vm = new Vue({
    el: '#if_data',
    data: {
      yes:true,
      no:false,
      age:28,
      name:'matrix'
    }
})
```

```bash
注意：yes, no, age, name这4个变量都来源于Vue实例选项对象的data属性
```

### 运行示例

```bash
npm run dev
```

### 发布

```bash
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjw07ofjsjj20ut08swej.jpg)

## v-show指令

```bash
v-show也是条件渲染指令，和v-if指令不同的是，使用v-show指令的元素始终会被渲染到HTML，它只是简单地为元素设置CSS的style属性
```

>cmd/show.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
          }
          #if_data{
            width: 400px;
            height: 500px;
            margin:100px auto;
          }
          #if_data p{
            font-size: 16px;
            font-family: "微软雅黑";
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="show_data">
          <h1>Hello , Vue.js！</h1>
          <h1 v-show="yes">Yes!</h1>
          <h1 v-show="no">No!</h1>
          <h1 v-show="age >= 25">Age：{{ age }}</h1>
          <h1 v-show="name.indexOf('matrix') >= 0">Name：{{ name }}</h1>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var show_data = new Vue({
    el: '#show_data',
    data: {
      yes:true,
      no:false,
      age:28,
      name:'matrix'
    }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjwuxj6axej20wk0940su.jpg)

## v-else指令

```bash
可以用v-else指令为v-if或v-show添加一个"else块"
v-else元素必须立即跟在v-if或v-show元素的后面——否则它不能被识别
```

>cmd/else.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <title>vue-simple-demo</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
          }
          #else_data{
            width: 400px;
            height: 500px;
            margin:100px auto;
          }
          #else_data p{
            color: #369;
            font-size: 16px;
            font-family: "微软雅黑";
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="else_data">
          <h1 v-if="age >= 25">Age：{{ age }}</h1>
          <h1 v-else>Name：{{ name }}</h1>
          <h1>---------------------</h1>
          <h1 v-show="name.indexOf('jack') >= 0">Name：{{ name }}</h1>
          <h1 v-else>Sex：{{ sex }}</h1>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var else_data = new Vue({
  el:'#else_data',
  data:{
    age:28,
    name:'jack ma',
    sex:'Male'
  }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjwvdwjmkxj20uv07ywei.jpg)
