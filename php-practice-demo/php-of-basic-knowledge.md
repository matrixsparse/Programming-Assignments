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

## PHP数据类型

* String (字符串)
* Integer (整型)
* Float (浮点型)
* Boolean (布尔型)
* Array (数组)
* Object (对象)
* NULL (空值)

### 整型

var_dump()函数返回变量的数据类型和值

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:27
 */

$x = 5985;
var_dump($x);
echo "<br>";

$x = -345;// 负数
var_dump($x);
echo "<br>";

$x = 0x8C;// 十六进制数
var_dump($x);
echo "<br>";

$x = 047;// 八进制数
var_dump($x);
```

>运行结果

```bash
int(5985)
int(-345)
int(140)
int(39)
```

### 浮点型

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:24
 */

$x = 10.365;
var_dump($x);
echo "<br>";

$x = 2.4e3;
var_dump($x);
echo "<br>";

$x = 8E-5;
var_dump($x);

?>
```

>运行结果

```bash
float(10.365)
float(2400)
float(8.0E-5)
```

### 布尔型

```bash
布尔型可以是TRUE或FALSE
```

### 数组

数组可以在一个变量中存储多个值

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:22
 */

$cars = array("Volvo", "BMW", "Toyota");
var_dump($cars);

?>
```

>运行结果

```bash
array(3) { [0]=> string(5) "Volvo" [1]=> string(3) "BMW" [2]=> string(6) "Toyota" }
```

### 对象

在PHP中，对象必须声明

必须使用class关键字关键字声明类对象

类是可以包含属性和方法的结构

在类中定义数据类型，然后在实例化的类中使用数据类型

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:34
 */

class Car
{
    var $color;

    function Car($color = "green")
    {
        $this->color = $color;
    }

    function what_color()
    {
        return $this->color;
    }
}

function print_vars($obj)
{
    foreach (get_object_vars($obj) as $prop => $val) {
        echo "\t$prop = $val\n";
    }
}

// instantiate one object
$herbie = new Car("white");

// show herbie properties
echo "\herbie：Properties\n";
print_vars($herbie);
?>
```

>运行结果

```bash
\herbie：Properties color = white
```

### NULL值

NULL值表示变量没有值，NULL是数据类型为NULL的值

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:40
 */

$x = "Hello Wolrd!";
$x = null;

var_dump($x);

?>
```

>运行结果

```bash
NULL
```

### 常量

```bash
常量是一个简单值的标识符，该值在脚本中不能改变(常量名不需要加 $ 修饰符)

注意： 常量在整个脚本中都可以使用

设置常量，使用 define() 函数，函数语法如下：

define(string constant_name, mixed value, case_sensitive = true)
```

>该函数有三个参数:

* constant_name：必选参数，常量名称，即标志符
* value：必选参数，常量的值
* case_sensitive：可选参数，指定是否大小写敏感，设定为 true 表示不敏感

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:55
 */

define("GREETING", "Welcome to sparsematrix.cc!");
echo GREETING;
?>
```

>运行结果

```bash
Welcome to sparsematrix.cc!
```

### 字符串函数和字符串连接

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 16:58
 */

$str1 = "Hello World!";
$str2 = "What a nice day!";
echo $str1 . " " . $str2;// 字符串连接运算符

echo "<br>";
echo strlen("Hello World!"); // 获取字符串长度
echo "<br>";
echo strpos("Hello World！","World！");// 获取子串位置
// 字符串中第一个字符的位置是 0
?>
```

>运行结果

```bash
Hello World! What a nice day!
12
6
```

### 运算符

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 17:15
 */

// 其他运算符
// 逻辑运算符！ && || and or xor
// 数组运算符 合并：+ 比较：== != === !==
// 在php中 != 与 <> 作用一样


$x = array("a" => "red", "b" => "green");
$y = array("c" => "blue", "d" => "yellow");
$z = $x + $y; // $x 和 $y 数组合并
var_dump($z);
echo "<br>";
var_dump($x == $y);
echo "<br>";
var_dump($x != $y);
echo "<br>";
var_dump($x <> $y);
echo "<br>";
var_dump($x != $y);
?>
```

>运行结果

```bash
array(4) { ["a"]=> string(3) "red" ["b"]=> string(5) "green" ["c"]=> string(4) "blue" ["d"]=> string(6) "yellow" }
bool(false)
bool(true)
bool(true)
bool(true)
```

### 数组

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 17:33
 */

$cars = array("Volvo", "BMW", "Toyota");
echo "I like " . $cars[0] . " , " . $cars[1] . " and " . $cars[2] . ".";//访问数组元素

// 数组长度count()
$cars = array("Volvo", "BMW", "Toyota");
$arrlength = count($cars);


// 遍历数值数组
$cars = array("Volvo", "BMW", "Toyota");
$arrlength = count($cars);

for ($x = 0; $x < $arrlength; $x++) {
    echo $cars[$x];
    echo "<br>";
}

$age = array("Peter" => "35", "Ben" => "37", "Joe" => "43");// 定义关联数组
echo "Peter is " . $age['Peter'] . " years old.";
echo "<br>";

foreach ($age as $x => $x_value) {
    echo "Key=" . $x . " , Value=" . $x_value;
    echo "<br>";
}
?>
```

>运行结果

```bash
I like Volvo , BMW and Toyota.Volvo
BMW
Toyota
Peter is 35 years old.
Key=Peter , Value=35
Key=Ben , Value=37
Key=Joe , Value=43
```

### 数组排序

* sort() - 对数组进行升序排列
* rsort() - 对数组进行降序排列
* asort() - 根据关联数组的值，对数组进行升序排列
* ksort() - 根据关联数组的键，对数组进行升序排列
* arsort() - 根据关联数组的值，对数组进行降序排列
* krsort() - 根据关联数组的键，对数组进行降序排列

```bash
<?php
/**
 * Created by PhpStorm.
 * User: Administrator
 * Date: 2018/1/3
 * Time: 17:56
 */

// sort() - 对数组进行升序排列
// rsort() - 对数组进行降序排列
// asort() - 根据关联数组的值，对数组进行升序排列
// ksort() - 根据关联数组的键，对数组进行升序排列
// arsort() - 根据关联数组的值，对数组进行降序排列
// krsort() - 根据关联数组的键，对数组进行降序排列

$cars = array("Volvo", "BMW", "Toyota");
sort($cars);

$clength = count($cars);

for ($x = 0; $x < $clength; $x++) {
    echo $cars[$x];
    echo "<br>";
}

// rsort()
$cars = array("Volvo", "BMW", "Toyota");
rsort($cars);

// asort() 关联数组排序 value
$age = array("Peter" => "35", "Ben" => "37", "Joe" => 43);
asort($age);
arsort($age);


// ksort() 关联数组排序 key
$age = array("Peter" => "35", "Ben" => "37", "Joe" => "43");
ksort($age);
krsort($age);
?>
```

>运行结果

```bash
BMW
Toyota
Volvo
```
