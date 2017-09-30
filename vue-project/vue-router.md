# vue-router

```bash
vue-router是Vue.js官方的路由插件，它和vue.js是深度集成的，适合用于构建单页面应用
vue的单页面应用是基于路由和组件的，路由用于设定访问路径，并将路径和组件映射起来

传统的页面应用，是用一些超链接来实现页面切换和跳转的
在vue-router单页面应用中，则是路径之间的切换，也就是组件的切换
```

## 单页面应用示例

```bash
这个单页面应用有两个路径
/home
和
/about
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk1cvisv2zj20ea09lq2w.jpg)

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <link rel="stylesheet" href="http://bootswatch.com/flatly/bootstrap.css" type="text/css"/>
        <link rel="stylesheet" href="../src/assets/css/style.css" type="text/css"/>
        <script src="https://unpkg.com/vue/dist/vue.js"></script>
        <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
        <title>vue-router之所有代码耦合在HTML页面</title>
    </head>
    <body>
        <div id="app">
            <div class="row">
              <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header">
                  <h2>Router Basic - 01</h2>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-xs-2 col-xs-offset-2">
                  <div class="list-group">
                    <!-- 使用 router-link 组件来导航. -->
                    <!-- 通过传入 `to` 属性指定链接. -->
                    <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->
                    <router-link class="list-group-item" to="/home">Home</router-link>
                    <router-link class="list-group-item" to="/about">About</router-link>
                  </div>
                </div>
                <div class="col-xs-6">
                  <div class="panel">
                    <div class="panel-body">
                      <!--用于渲染匹配的组件-->
                      <router-view></router-view>
                    </div>
                  </div>
                </div>
            </div>
        </div>
        <template id="home">
    			<div>
    				<h1>Home</h1>
    				<p>{{msg}}</p>
    			</div>
    		</template>
    		<template id="about">
    			<div>
    				<h1>About</h1>
    				<p>This is the tutorial about vue-router.</p>
    			</div>
    		</template>
    </body>
    <script>
        // 0. 如果使用模块化机制编程， 要调用 Vue.use(VueRouter)
        // 如果使用全局的 script 标签，则无须如此（手动安装）

        // 1. 定义（路由）组件。
        // 可以从其他文件 import 进来
        // const home = { template: '#home' }
        // const about = { template: '#about' }

        var home = Vue.extend({
            template:'#home',
            data: function() {
      				return {
      					msg: 'Hello, vue router!'
      				}
      			}
        })

        var about = Vue.extend({
            template:'#about'
        })

        // 2. 定义路由
        // 每个路由应该映射一个组件。 其中"component" 可以是
        // 通过 Vue.extend() 创建的组件构造器，
        // 或者，只是一个组件配置对象。
        // 我们晚点在讨论嵌套路由。
        const routes = [
          { path: '/home', component: home },
          { path: '/about', component: about }
        ]

        // 3. 创建 router 实例，然后传 `routes` 配置
        // 你还可以传别的配置参数, 不过先这么简单着吧。
        const router = new VueRouter({
          routes // （缩写）相当于 routes: routes
        })

        // 4. 创建和挂载根实例。
        // 记得要通过 router 配置参数注入路由，
        // 从而让整个应用都有路由功能
        const app = new Vue({
          router
        }).$mount('#app')

        // 现在，应用已经启动了！
    </script>
</html>
```

### 运行示例

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk1i7ao4jdj217p0920sx.jpg)

## 嵌套路由

```bash
实际生活中的应用界面，通常由多层嵌套的组件组合而成
同样地，URL 中各段动态路径也按某种结构对应嵌套的各层组件
/user/foo/profile                     /user/foo/posts
+------------------+                  +-----------------+
| User             |                  | User            |
| +--------------+ |                  | +-------------+ |
| | Profile      | |  +------------>  | | Posts       | |
| |              | |                  | |             | |
| +--------------+ |                  | +-------------+ |
+------------------+                  +-----------------+
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk1i6ilzf4j20cd0ckaa5.jpg)

```bash
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <link rel="shortcut icon" href="../src/assets/logo.png" />
        <link rel="stylesheet" href="http://bootswatch.com/flatly/bootstrap.css" type="text/css"/>
        <link rel="stylesheet" href="../src/assets/css/style.css" type="text/css"/>
        <script src="https://unpkg.com/vue/dist/vue.js"></script>
        <script src="https://unpkg.com/vue-router/dist/vue-router.js"></script>
        <title>vue-router之嵌套路由</title>
    </head>
    <body>
        <div id="app">
            <div class="row">
              <div class="col-xs-offset-2 col-xs-8">
                <div class="page-header">
                  <h2>Router Basic - 02</h2>
                </div>
              </div>
            </div>
            <div class="row">
                <div class="col-xs-2 col-xs-offset-2">
                  <div class="list-group">
                    <!-- 使用 router-link 组件来导航. -->
                    <!-- 通过传入 `to` 属性指定链接. -->
                    <!-- <router-link> 默认会被渲染成一个 `<a>` 标签 -->
                    <router-link class="list-group-item" to="/home">Home</router-link>
                    <router-link class="list-group-item" to="/about">About</router-link>
                    <router-link class="list-group-item" to="/user/router1">User/router1</router-link>
                    <router-link class="list-group-item" to="/user/router1/profile">User/router1/profile</router-link>
                    <router-link class="list-group-item" to="/user/router1/posts">User/router1/posts</router-link>
                    <router-link class="list-group-item" to="/user/router2">User/router2</router-link>
                    <router-link class="list-group-item" to="/user/router2/profile">User/router2/profile</router-link>
                    <router-link class="list-group-item" to="/user/router2/posts">User/router2/posts</router-link>
                  </div>
                </div>
                <div class="col-xs-6">
                  <div class="panel">
                    <div class="panel-body">
                      <!--用于渲染匹配的组件-->
                      <router-view></router-view>
                    </div>
                  </div>
                </div>
            </div>
        </div>
        <template id="home">
    			<div>
    				<h1>Home</h1>
    				<p>{{msg}}</p>
    			</div>
    		</template>
    		<template id="about">
    			<div>
    				<h1>About</h1>
    				<p>This is the tutorial about vue-router.</p>
    			</div>
    		</template>
        <template id="user">
    			<div>
    				<h1>User {{ $route.params.id }}</h1>
            <!--用于渲染匹配的组件-->
            <router-view></router-view>
    			</div>
    		</template>
    </body>
    <script>
        // 0. 如果使用模块化机制编程， 要调用 Vue.use(VueRouter)
        // 如果使用全局的 script 标签，则无须如此（手动安装）

        // 1. 定义（路由）组件。
        // 可以从其他文件 import 进来
        // const home = { template: '#home' }
        // const about = { template: '#about' }

        var Home = Vue.extend({
            template:'#home',
            data: function() {
      				return {
      					msg: 'Hello, vue router!'
      				}
      			}
        })

        var About = Vue.extend({
            template:'#about'
        })

        var User = Vue.extend({
          template: '#user',
          data: function(){
            return {
              id : '{{ $route.params.id }}'
            }
          }
        })

        const UserHome = { template: '<div>This is Home</div>' }
        const UserProfile = { template: '<div>This is Profile</div>' }
        const UserPosts = { template: '<div>This is Posts</div>' }


        // 2. 定义路由
        // 每个路由应该映射一个组件。 其中"component" 可以是
        // 通过 Vue.extend() 创建的组件构造器，
        // 或者，只是一个组件配置对象。
        // 我们晚点在讨论嵌套路由。
        const routes = [
          { path: '/home', component: Home },
          { path: '/about', component: About },
          { path: '/user/:id', component: User,
          children: [
            // UserHome will be rendered inside User's <router-view>
            // when /user/:id is matched
            { path: '', component: UserHome },

            // UserProfile will be rendered inside User's <router-view>
            // when /user/:id/profile is matched
            { path: 'profile', component: UserProfile },

            // UserPosts will be rendered inside User's <router-view>
            // when /user/:id/posts is matched
            { path: 'posts', component: UserPosts }
          ]
          }
        ]

        // 3. 创建 router 实例，然后传 `routes` 配置
        // 你还可以传别的配置参数, 不过先这么简单着吧。
        const router = new VueRouter({
          routes // （缩写）相当于 routes: routes
        })

        // 4. 创建和挂载根实例。
        // 记得要通过 router 配置参数注入路由，
        // 从而让整个应用都有路由功能
        const app = new Vue({
          router
        }).$mount('#app')

        // 现在，应用已经启动了！
    </script>
</html>
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fk1kgi1m40j213o0f03yv.jpg)

## 编程式导航

```bash
router.push(location)

想要导航到不同的 URL，则使用 router.push 方法。这个方法会向 history 栈添加一个新的记录

所以，当用户点击浏览器后退按钮时，则回到之前的 URL
当你点击 <router-link> 时，这个方法会在内部调用

所以说，点击 <router-link :to="..."> 等同于调用 router.push(...)
```

```bash
// 字符串
router.push('home')

// 对象
router.push({ path: 'home' })

// 命名的路由
router.push({ name: 'user', params: { userId: 123 }})

// 带查询参数，变成 /register?plan=private
router.push({ path: 'register', query: { plan: 'private' }})
```
