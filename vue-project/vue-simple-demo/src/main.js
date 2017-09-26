import Vue from 'vue'
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
