# vue-component

## vue组件简介

```bash
组件系统是Vue.js其中一个重要的概念，它提供了一种抽象，让我们可以使用独立可复用的小组件来构建大型应用，任意类型的应用界面都可以抽象为一个组件树
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvk1axew8j20qe094jrk.jpg)

>什么是组件

```bash
组件可以扩展HTML元素，封装可重用的HTML代码，可以将组件看作自定义的HTML元素。
```

## 组件的创建和注册

### 基本步骤

>Vue.js的组件的使用有3个步骤：创建组件构造器、注册组件和使用组件

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvk4nejf0j208y0ekglu.jpg)

### 示例

>component.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
    </head>
    <body>
      <div id="component-test">
        <!-- 3.#component-test是Vue实例挂载的元素，应该在挂载元素范围内使用组件 -->
        <matrix-component></matrix-component>
      </div>
    </body>
    <script src="/dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// 1.创建一个组件构造器
var myComponent = Vue.extend({
  template: '<div style="font-family:微软雅黑;">This is matrix first component</div>'
})

// 2.注册组件，并指定组件的标签，组件的HTML标签为<my-component>
Vue.component('matrix-component',myComponent)

// 3.创建一个 Vue 实例或 "ViewModel"
// 它连接 View 与 Model
new Vue({
    el: '#component-test',
})
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

```bash
使用组件和使用普通的HTML元素没什么区别
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvm63m3k7j20s703omx3.jpg)

## 理解组件的创建和注册

```bash
1. Vue.extend()是Vue构造器的扩展，调用Vue.extend()创建的是一个组件构造器
2. Vue.extend()构造器有一个选项对象，选项对象的template属性用于定义组件要渲染的HTML
3. 使用Vue.component()注册组件时，需要提供2个参数，第1个参数时组件的标签，第2个参数是组件构造器
4. 组件应该挂载到某个Vue实例下，否则它不会生效
```

### 注意点：以下代码在3个地方使用了<my-component>标签，但只有#component-test1和#component-test2下的<my-component>标签才起到作用

>component.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
    </head>
    <body>
      <div id="component-test1">
        <!-- 3.#component-test是Vue实例挂载的元素，应该在挂载元素范围内使用组件 -->
        <matrix-component></matrix-component>
      </div>

      <div id="component-test2">
        <!-- 3.#component-test是Vue实例挂载的元素，应该在挂载元素范围内使用组件 -->
        <matrix-component></matrix-component>
      </div>

      <!--该组件不会被渲染-->
      <my-component></my-component>
    </body>
    <script src="/dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// 1.创建一个组件构造器
var myComponent = Vue.extend({
  template: '<div style="font-family:微软雅黑;">This is matrix component</div>'
})

// 2.注册组件，并指定组件的标签，组件的HTML标签为<my-component>
Vue.component('matrix-component',myComponent)

// 3.创建一个 Vue 实例或 "ViewModel"
// 它连接 View 与 Model
var component1 = new Vue({
    el: '#component-test1',
})

var component2 = new Vue({
    el: '#component-test2',
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvmbwy1umj20o402w3yg.jpg)

## 全局注册和局部注册

```bash
调用Vue.component()注册组件时，组件的注册是全局的，这意味着该组件可以在任意Vue示例下使用
如果不需要全局注册，或者是让组件使用在其它组件内，可以用选项对象的components属性实现局部注册
```

### 上面的示例可以改为局部注册的方式

>local_component.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="src/assets/logo.png" />
        <title>vue-simple-demo</title>
    </head>
    <body>

      <div id="local_component">
        <!-- #local-component是Vue实例挂载的元素，应该在挂载元素范围内使用组件 -->
        <local-component></local-component>
      </div>

    </body>
    <script src="/dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// 1.创建一个组件构造器
var localComponent = Vue.extend({
  template: '<div style="font-family:微软雅黑;">This is matrix local component</div>'
})

var local_component = new Vue({
    el: '#local_component',
    components: {
      // 2. 将localComponent组件注册到Vue实例下
      'local-component' : localComponent
    }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjvo31275pj20qc039747.jpg)

## 父组件、子组件

>cmd/parent.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <title>父组件、子组件</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
            font-family: "微软雅黑";
          }
          #parent_data{
            width: 50%;
            margin:100px auto;
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="parent_data">
            <parent-component></parent-component>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>注意：vue2.0要求每个template只能有`一个根元素`

>src/main.js

```bash
import Vue from 'vue'

// 父组件、子组件
var Child = Vue.extend({
  template: '<p>This is child component！</p>'
})

var Parent = Vue.extend({
  // 在Parent组件内使用<child-component>标签
  template:'<div><p>This is a Parent component</p><child-component></child-component></div>',
  components: {
    // 局部注册Child组件，该组件只能在Parent里使用
    'child-component': Child
  }
})

// 全局注册Parent组件
Vue.component('parent-component',Parent)

// 注册Vue实例
new Vue({
  el:'#parent_data'
})
```

```bash
var Child = Vue.extend(...)定义了Child组件构造器
var Parent = Vue.extend(...)定义了Parent组件构造器
components: { 'child-component': Child }，将Child组件注册到Parent组件，并将Child组件的标签设置为child-component
template :'<p>This is a Parent component</p><child-component></child-component>'，在Parent组件内以标签的形式使用Child组件
Vue.component('parent-component', Parent) 全局注册Parent组件
在页面中使用<parent-component>标签渲染Parent组件的内容，同时Child组件的内容也被渲染出来
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy88h2c25j20j90ckjrt.jpg)

```bash
Child组件是在Parent组件中注册的，它只能在Parent组件中使用，确切地说：子组件只能在父组件的template中使用
请注意下面两种子组件的使用方式是错误的：
```

>以子标签的形式在父组件中使用

```bash
<div id="app">
    <parent-component>
        <child-component></child-component>
    </parent-component>
</div>
```

```bash
为什么这种方式无效呢？

因为当子组件注册到父组件时，Vue会编译好父组件的模板，模板的内容已经决定了父组件将要渲染的HTML

<parent-component>…</parent-component>相当于运行时，它的一些子标签只会被当作普通的HTML来执行
<child-component></child-component>不是标准的HTML标签，会被浏览器直接忽视掉
```

>在父组件标签外使用子组件

```bash
<div id="app">
    <parent-component>
    </parent-component>
    <child-component>
    </child-component>
</div>
```

```bash
运行这段代码，浏览器会提示错误
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy59std4aj20sb05rjrd.jpg)

## 组件注册语法糖

```bash
以上组件注册的方式有些繁琐，Vue为了简化这个过程，提供了注册语法糖
```

### 使用Vue.component()直接创建和注册组件

```bash
// 全局注册，my-component是标签名称
Vue.component('my-component',{
    template: '<div>This is the first component!</div>'
})

var vm1 = new Vue({
    el: '#app'
})
```

```bash
Vue.component()的第1个参数是标签名称，第2个参数是一个选项对象，

使用选项对象的template属性定义组件模板

使用这种方式，Vue在背后会自动地调用Vue.extend()
```

### 在选项对象的components属性中实现局部注册

```bash
var vm2 = new Vue({
    el: '#app2',
    components: {
        // 局部注册，my-component2是标签名称
        'my-component2': {
            template: '<div>This is the second component!</div>'
        },
        // 局部注册，my-component3是标签名称
        'my-component3': {
            template: '<div>This is the third component!</div>'
        }
    }
})
```

## 使用script或template标签

```bash
尽管语法糖简化了组件注册，但在template选项中拼接HTML元素比较麻烦，这也导致了HTML和JavaScript的高耦合性
庆幸的是，Vue提供了两种方式将定义在JavaScript中的HTML模板分离出来
```

### 使用script标签

>cmd/script.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <title>使用Script标签</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
            font-size: 16px;
            font-family: "微软雅黑";
          }
          #script_data{
            width: 50%;
            margin:100px auto;
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="script_data">
            <content-component></content-component>
        </div>

        <script type="text/x-template" id="contentComponent">
            <div>This is a component！</div>
        </script>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

// 使用script语法，分离在Js中的HTML
// 全局注册组件
Vue.component('content-component',{
  template: '#contentComponent'
})

// 注册Vue实例
new Vue({
  el: '#script_data'
})
```

```bash
template选项现在不再是HTML元素，而是一个id，Vue根据这个id查找对应的元素，然后将这个元素内的HTML作为模板进行编译
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy8yi1vdcj20tj06ajrc.jpg)

## 组件的el和data选项

```bash
传入Vue构造器的多数选项也可以用在 Vue.extend()或Vue.component()中

不过有两个特例：data和el

Vue规定：在定义组件的选项时，data和el选项必须使用函数

下面的代码在执行时，浏览器会提出一个错误
```

```bash
Vue.component('my-component', {
    data: {
        a: 1
    }
})
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy967pmy1j20gz06kmxg.jpg)

```bash
另外，如果data选项指向某个对象，这意味着所有的组件实例共用一个data

我们应当使用一个函数作为 data 选项，让这个函数返回一个新对象
```

```bash
Vue.component('my-component', {
    data: function(){
        return {a : 1}
    }
})
```

## 使用props

```bash
组件实例的作用域是孤立的
这意味着不能并且不应该在子组件的模板内直接引用父组件的数据
可以使用 props 把数据传给子组件
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy9f4lzbnj20i30e1q3d.jpg)
