# php of basic knowledge

## 配置phpstorm

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fn3gaoipuoj20m20ifjs4.jpg)

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fn3gaoi8z2j20m00ib74r.jpg)

## PHP能做什么

* PHP 可以生成动态页面内容
* PHP 可以创建、打开、读取、写入、关闭服务器上的文件
* PHP 可以收集表单数据
* PHP 可以发送和接收 cookies
* PHP 可以添加、删除、修改您的数据库中的数据
* PHP 可以限制用户访问您的网站上的一些页面
* PHP 可以加密数据

## PHP基本语法

* PHP 脚本可以放在文档中的任何位置
* PHP 脚本以 <?php 开始，以 ?> 结束
* PHP 中的每个代码行都必须以分号结束
* 两种在浏览器输出文本的基础指令：echo 和 print

## PHP变量

变量以 $ 符号开始，后面跟着变量的名称
PHP 没有声明变量的命令
变量在您第一次赋值给它的时候被创建：
PHP 是一门弱类型语言【不用声明变量的类型】
PHP 会根据变量的值，自动把变量转换为正确的数据类型

在强类型的编程语言中，我们必须在使用变量前先声明（定义）变量的类型和名称

## PHP变量的作用域

* local
* global
* static
* parameter

### 局部和全局作用域

在所有函数外部定义的变量，拥有全局作用域

除了函数外，全局变量可以被脚本中的任何部分访问，要在一个函数中访问一个全局变量，需要使用 global 关键字

>在 PHP 函数内部声明的变量是局部变量，仅能在函数内部访问

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 12:03
 */

$x = 5;//全局变量

function myTest()
{
    $y = 10;//局部变量
    global $x;
    echo "<p>测试变量在函数内部：</p>";
    echo "变量 x 为：$x";
    echo "<br>";
    echo "变量 y 为：$y";

}

myTest();

echo "<p>测试变量在函数内部：</p>";
echo "变量 x 为：$x";
echo "<br>";
echo "变量 y 为：$y"

?>
```

>运行结果

```bash
测试变量在函数内部：

变量 x 为：5
变量 y 为：10
测试变量在函数内部：

变量 x 为：5
变量 y 为：
```

>在函数内调用函数外定义的全局变量，需要在函数中的变量前加上 global 关键字

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 12:03
 */

$x = 5;
$y = 10;

function myTest()
{
    global $x, $y;
    $y = $x + $y;
}

myTest();
echo $y

?>
```

>运行结果

```bash
15
```

PHP 将所有全局变量存储在一个名为 $GLOBALS[index] 的数组中

index 保存变量的名称

这个数组可以在函数内部访问，也可以直接用来更新全局变量

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 15:16
 */

$x = 25;
$y = 10;

function myTest()
{
    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
}

myTest();
echo $y;

?>
```

>运行结果

```bash
35
```

### Static作用域

```bash
当一个函数完成时，它的所有变量通常都会被删除

有时候您希望某个局部变量不要被删除,可以使用static关键字
```

>static_scope.php

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 15:20
 */

function myTest()
{
    static $x = 0;
    echo "$x<br/>";
    $x++;
}

myTest();
myTest();
myTest();

?>
```

>运行结果

```bash
0
1
2
```

### 参数作用域

```bash
参数是通过调用代码将值传递给函数的局部变量
```

>参数是在参数列表中声明的，作为函数声明的一部分

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 15:26
 */

function myTest($x)
{
    echo $x;
}

myTest(5);
?>
```

>运行结果

```bash
5
```

### PHP echo 和 print 语句

* echo - 可以输出一个或多个字符串
* print - 只允许输出一个字符串，返回值总为 1

>echo 输出的速度比 print 快， echo 没有返回值，print有返回值1

```bash
echo 和 print 都是一个语言结构，使用的时候可以不用加括号

也可以加上括号： echo 或 echo() print print()。
```

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 15:30
 */

echo "<h2>PHP is fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This", " string", " was", " made", " with multiple parameters.";

print "<h2>PHP is fun!</h2>";
print "Hello world!<br>";
print "I'm about to learn PHP!";

?>
```

>运行结果

```bash
PHP is fun!

Hello world!
I'm about to learn PHP!
This string was made with multiple parameters.

PHP is fun!

Hello world!
I'm about to learn PHP!
```

###

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 15:30
 */

$str1 = "Learn PHP";
$str2 = "sparsematrix.cc";

$str_all = array("Tom", "Arry", "Jack");

echo $str1;
echo "<br>";
echo "Study PHP at $str2<br>";//php 双引号内部可包含变量
echo "My car is a {$str_all[0]}<br><br>";// 用大括号 显式的指定这是变量

$str1 = "Learn PHP";
$str2 = "sparsematrix.ccL";
$str_all = array();

print $str1;
print "<br>";
print "Study PHP at $str2<br>";
print "My car is a {$str_all[0]}<br><br>";

?>
```

>运行结果

```bash
Learn PHP
Study PHP at sparsematrix.cc
My car is a Tom

Learn PHP
Study PHP at sparsematrix.ccL
My car is a
```
