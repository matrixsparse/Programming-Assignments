# Vue-Hello-World

## Vue

```bash
Vue.js是当下很火的一个JavaScript MVVM库，它是以数据驱动和组件化的思想构建的。
相比于Angular.js，Vue.js提供了更加简洁、更易于理解的API，使得我们能够快速地上手并使用Vue.js

如果你之前已经习惯了用jQuery操作DOM，学习Vue.js时请先抛开手动操作DOM的思维
因为Vue.js是数据驱动的，你无需手动操作DOM
它通过一些特殊的HTML语法，将DOM和数据绑定起来
一旦你创建了绑定，DOM将和数据保持同步，每当变更了数据，DOM也会相应地更新。
```

## MVVM模式

```bash
下图不仅概括了MVVM模式（Model-View-View-Model），还描述了在Vue.js中ViewModel是如何和View以及Model进行交互的
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjv3ckvi4tj21gw0rgq6q.jpg)

```bash
ViewModel是Vue.js的核心，它是一个Vue实例。Vue实例是作用于某一个HTML元素上的，这个元素可以是HTML的body元素，也可以是指定了id的某个元素。
```

>当创建了ViewModel后，双向绑定是如何达成的呢？

```bash
首先，我们将上图中的DOM Listeners和Data Bindings看作两个工具，它们是实现双向绑定的关键
从View角度看，ViewModel中的DOM Listeners工具会帮我们监测页面上DOM元素的变化，如果有变化，则更改Model中的数据；
从Model角度看，当我们更新Model中的数据时，Data Bindings工具会帮我们更新页面中的DOM元素
```

## Hello World示例

>index.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
    </head>
    <body>
        <!--View-->
        <div id="hello">
            {{ message }}
        </div>
    </body>
    <script src="/dist/build.js"></script>
    <script>
    </script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// Model
var exampleData = {
    message: 'Hello World!'
}

// 创建一个 Vue 实例或 "ViewModel"
// 它连接 View 与 Model
new Vue({
    el: '#hello',
    data: exampleData
})

```

>使用Vue的过程就是定义MVVM各个组成部分的过程的过程

```bash
1.定义View
2.定义Model
3.创建一个Vue实例或"ViewModel"，它用于连接View和Model

在创建Vue实例时，需要传入一个选项对象，选项对象可以包含数据、挂载元素、方法、模生命周期钩子等等

选项对象的el属性指向View
el: '#app'表示该Vue实例将挂载到<div id="app">...</div>这个元素

data属性指向Model
data: exampleData表示我们的Model是exampleData对象

Vue.js有多种数据绑定的语法，最基础的形式是文本插值，使用一对大括号语法，在运行时{{ message }}会被数据对象的message属性替换，所以页面上会输出"Hello World!"
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

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjv4ljk72yj215g07cgn8.jpg)

## 双向绑定示例

```bash
MVVM模式本身是实现了双向绑定的，在Vue.js中可以使用v-model指令在表单元素上创建双向数据绑定
```

>data.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
    </head>
    <body>
        <!--View-->
        <div id="data">
            <p>{{ message }}</p>
            <input type="text" v-model="message"/>
        </div>
    </body>
    <script src="/dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// Model
var exampleData = {
    message: 'Hello World!'
}

// 创建一个 Vue 实例或 "ViewModel"
// 它连接 View 与 Model
new Vue({
    el: '#data',
    data: exampleData
})
```

```bash
将message绑定到文本框，当更改文本框的值时，<p>{{ message }}</p> 中的内容也会被更新。
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvzr9r3goj20n70323yf.jpg)
