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

## v-for指令

```bash
v-for指令基于一个数组渲染一个列表，它和JavaScript的遍历语法相似
```

```bash
v-for="item in items"
```

```bash
items是一个数组，item是当前被遍历的数组元素。
```

>cmd/for.html

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
          #for_data{
            width: 400px;
            height: 500px;
            margin:100px auto;
          }
          #for_data tr th {
            background: #42b983;
            font-size: 1.2rem;
            font-weight: 400;
            color: #fff;
            cursor: pointer;
          }
          td, th {
              border: 1px solid #bcbcbc;
              padding: 5px 10px;
          }
          table, td, th {
              border-collapse: collapse;
              border-spacing: 0;
          }
          #for_data tr th,#for_data tr td{
            font-size: 16px;
            font-family: "微软雅黑";
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="for_data">
          <table>
            <thread>
              <tr>
                  <th>Name</th>
                  <th>Age</th>
                  <th>Sex</th>
              </tr>
            </thread>
            <tbody>
              <tr v-for="person in people">
                  <td>{{ person.name }}</td>
                  <td>{{ person.age }}</td>
                  <td>{{ person.sex }}</td>
              </tr>
            </tbody>
          </table>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var for_data = new Vue({
  el:'#for_data',
  data:{
    people:[{
      name:'Jack',
      age:30,
      sex:'Male'
    },{
      name:'Bill',
      age:26,
      sex:'Male'
    },{
      name:'Tracy',
      age:22,
      sex:'Female'
    },{
      name:'Chris',
      age:36,
      sex:'Male'
    }]
  }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

```bash
我们在选项对象的data属性中定义了一个people数组，然后在#for_data元素内使用v-for遍历people数组，输出每个person对象的姓名、年龄和性别
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjwxytrq3bj20wk09hmx9.jpg)

## v-bind指令

```bash
v-bind指令可以在其名称后面带一个参数，中间放一个冒号隔开，这个参数通常是HTML元素的特性（attribute），例如：v-bind:class
```

```bash
v-bind:argument="expression"
```

```bash
下面这段代码构建了一个简单的分页条，v-bind指令作用于元素的class特性上
这个指令包含一个表达式，表达式的含义是：高亮当前页
```

>cmd/bind.html

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
            box-sizing: border-box;
          }
          #bind_data{
            width: 50%;
            margin:100px auto;
          }
          #bind_data ul li{
            font-size: 16px;
            font-family: "微软雅黑";
          }
          .pagination .active {
            color: #fff;
            background-color: #009a61;
            border-left: none;
            border-right: none;
          }
          .pagination > li {
            display: inline;
          }
          .pagination > li > a {
            position: relative;
            float: left;
            padding: 6px 12px;
            line-height: 1.5;
            text-decoration: none;
            color: #009a61;
            background-color: #fff;
            border: 1px solid #ddd;
            margin-left: -1px;
            list-style: none;
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="bind_data">
          <ul class="pagination">
                <li v-for="n in pageCount">
                    <a href="javascripit:void(0)" v-bind:class="activeNumber === n ? 'active' : ''">{{ n }}</a>
                </li>
          </ul>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var bind_data = new Vue({
  el: '#bind_data',
  data:{
    activeNumber:1,
    pageCount: 10
  }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

```bash
注意v-for="n in pageCount"这行代码，pageCount是一个整数，遍历时n从0开始，然后遍历到pageCount –1结束
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjwz0lu4s9j20yb06wt8o.jpg)

## v-on指令

```bash
v-on指令用于给监听DOM事件，它的用语法和v-bind是类似的，例如监听<a>元素的点击事件
```

```bash
<a v-on:click="doSomething">
```

```bash
有两种形式调用方法：

绑定一个方法（让事件指向方法的引用），或者使用内联语句
Greet按钮将它的单击事件直接绑定到greet()方法，而Hi按钮则是调用say()方法
```

>cmd/on.html

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
            box-sizing: border-box;
          }
          #on_data{
            width: 50%;
            margin:100px auto;
          }
          #on_data p,#on_data p input[type='text'],#on_data p button{
            font-size: 16px;
            font-family: "微软雅黑";
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="on_data">
          <p><input type="text" v-model="message"><p>
          <p>
              <!-- click事件直接绑定一个方法 -->
              <button v-on:click="greet">Greet</button>
          </p>
          <p>
              <!-- click事件使用内联语句 -->
              <button v-on:click="say('Hi')">Hi</button>
          </p>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
import Vue from 'vue'

var on_data = new Vue({
  el: '#on_data',
  data:{
    message: 'Hello , Vue.js！'
  },
  // 在`methods`对象中定义方法
  methods:{
    greet:function(){
      // 方法内`this`指向vm
      alert(this.message)
    },
    say:function(msg){
      alert(msg)
    }
  }
})
```

### 运行示例&发布

```bash
npm run dev
npm run build
```

### 运行结果

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjx5luhzcmj20ri06d3yh.jpg)

## v-bind和v-on的缩写

```bash
Vue.js为最常用的两个指令v-bind和v-on提供了缩写方式

v-bind指令可以缩写为一个冒号
v-on指令可以缩写为@符号
```

```bash
<!--完整语法-->
<a href="javascripit:void(0)" v-bind:class="activeNumber === n ? 'active' : ''">{{ n }}</a>
<!--缩写语法-->
<a href="javascripit:void(0)" :class="activeNumber=== n ? 'active' : ''">{{ n }}</a>

<!--完整语法-->
<button v-on:click="greet">Greet</button>
<!--缩写语法-->
<button @click="greet">Greet</button>
```

## Vue-demo小案例

>cmd/demo.html

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <title>Vue-demo小案例</title>
        <style type="text/css">
          *{
            margin: 0;
            padding: 0;
            font-size: 14px;
            font-family: "微软雅黑";
            box-sizing: border-box;
          }
          .form-group {
            margin: 10px;
          }
          .form-group > label {
            display: inline-block;
            width: 10rem;
            text-align: right;
          }
          .form-group > input, .form-group > select {
            display: inline-block;
            height: 30px;
            line-height: 30px;
          }
          table {
              width: 100%;
          }
          input[type=text] {
            border: 1px solid #ccc;
            padding: .5rem .3rem;
          }
          thead {
            display: table-header-group;
            vertical-align: middle;
            border-color: inherit;
          }
          tbody {
            display: table-row-group;
            vertical-align: middle;
            border-color: inherit;
          }
          select {
            -webkit-appearance: menulist;
            box-sizing: border-box;
            align-items: center;
            white-space: pre;
            -webkit-rtl-ordering: logical;
            color: black;
            background-color: white;
            cursor: default;
            border-width: 1px;
            border-style: solid;
            border-color: initial;
            border-image: initial;
          }
          #t_data {
            margin: 100px auto;
            max-width: 640px;
          }
          table, td, th {
            border-collapse: collapse;
            border-spacing: 0;
          }
          button {
            outline: none;
            padding: 5px 8px;
            color: #fff;
            border: 1px solid #BCBCBC;
            border-radius: 3px;
            background-color: #009A61;
            cursor: pointer;
          }
          button:hover {
              opacity: 0.8;
          }
          tr {
            display: table-row;
            vertical-align: inherit;
            border-color: inherit;
          }
          .form-group > input, .form-group > select {
            display: inline-block;
            height: 30px;
            line-height: 30px;
          }
          input[type=text] {
            border: 1px solid #ccc;
            padding: .5rem .3rem;
          }
          th {
            background: #42b983;
            font-size: 14px;
            font-weight: 400;
            color: #fff;
            cursor: pointer;
          }
          td, th {
            border: 1px solid #bcbcbc;
            padding: 5px 10px;
          }
        </style>
    </head>
    <body>
        <!--View-->
        <div id="t_data">
           <fieldset>
              <legend>
                 Create New Person
              </legend>
              <div class="form-group">
                  <label>Name：</label>
                  <input type="text" v-model="newPerson.name"/>
              </div>
              <div class="form-group">
                  <label>Age：</label>
                  <input type="text" v-model="newPerson.age"/>
              </div>
              <div class="form-group">
                  <label>Sex：</label>
                  <select v-model="newPerson.sex">
                    <option value="Male">Male</option>
                    <option value="Female">Female</option>
                  </select>
              </div>
              <div class="form-group">
                  <label></label>
                  <button @click="createPerson">Create</button>
              </div>
           </fieldset>
           <table>
             <thead>
                 <tr>
                      <th>index</th>
                      <th>Name</th>
                      <th>Age</th>
                      <th>Sex</th>
                      <th>Delete</th>
                 </tr>
             </thead>
              <tbody>
                  <tr v-for="(person, index) in people">
                      <td>{{ index }}</td>
                      <td>{{ person.name }}</td>
                      <td>{{ person.age }}</td>
                      <td>{{ person.sex }}</td>
                      <td :class="'text-center'"><button @click="deletePerson($index)">Delete</button></td>
                  </tr>
              </tbody>
           </table>
        </div>
    </body>
    <script src="../dist/build.js"></script>
</html>
```

>src/main.js

```bash
var t_data= new Vue({
  el: '#t_data',
  data: {
    newPerson:{
      name: '',
      age: 0,
      sex: 'Male'
    },
    people:[{
      name: 'Jack',
      age: 30,
      sex: 'Male'
    },{
      name: 'Bill',
      age: 26,
      sex: 'Male'
    },{
      name: 'Tracy',
      age: 22,
      sex: 'Female'
    },{
      name: 'Chris',
      age: 36,
      sex: 'Male'
    }]
  },
  methods:{
    createPerson: function(){
      this.people.push(this.newPerson);
      // 添加完newPerson对象后，重置newPerson对象
      this.newPerson = {name:'',age:0,sex:'Male'}
    },
    deletePerson:function(index){
      console.log(index)
      // 删除一个数组元素
      this.people.splice(index,1);
    }
  }
})
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fjxzznfcxyj211a0hlq3c.jpg)
