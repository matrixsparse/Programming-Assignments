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

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjy59std4aj20sb05rjrd.jpg)
