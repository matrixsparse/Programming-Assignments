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

>if.html

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
