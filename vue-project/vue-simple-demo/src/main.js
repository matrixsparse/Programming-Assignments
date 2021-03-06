import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
// import App from './App.vue'

// new Vue({
//   el: '#app',
//   render: h => h(App)
// })

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

new Vue({
    el: '#data',
    data: exampleData
})

var vm = new Vue({
    el: '#if_data',
    data: {
      yes:true,
      no:false,
      age:28,
      name:'matrix'
    }
})

var show_data = new Vue({
    el: '#show_data',
    data: {
      yes:true,
      no:false,
      age:28,
      name:'matrix'
    }
})

var else_data = new Vue({
  el:'#else_data',
  data:{
    age:28,
    name:'jack ma',
    sex:'Male'
  }
})

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

var bind_data = new Vue({
  el: '#bind_data',
  data:{
    activeNumber:1,
    pageCount: 10
  }
})

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

// 使用script语法，分离在Js中的HTML
// 全局注册组件
Vue.component('content-component',{
  template: '#contentComponent'
})

// 注册Vue实例
new Vue({
  el: '#script_data'
})
