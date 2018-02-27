# CNNs 可视化

让我们看一个 CNN 的例子，了解它如何运作。

我们看到的训练 ImageNet 的 CNN 例子，来自 Zeiler 和 Fergus 的论文

在下图中（同样取自此论文），我们会看到网络中的每一层侦测到什么，看到每一层如何侦测更复杂的概念

## 第一层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvnql3fgj20d5064my8.jpg)

图片来自 Matthew Zeiler 和 Rob Fergus 的 deep visualization toolbox，让我们可以可视化地看到 CNN 每一层的关注的点是什么

上述格子中的每一个图片都代表一个激活神经元的图案。换句话说，这些是第一层认出的图案。左上角的图有一条-45度的直线，上方中间的图有一个+45度的直线。如下所示：

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvocbxtbj207806774i.jpg)

让我们看下引发这些示例图片的图片。下面的图都引发了 -45 度的直线，尽管他们有不同的颜色，渐变和图案

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvowdnf2j205q05cdgi.jpg)

所以 CNN 的第一层很清楚的选择了非常简单的形状、图案，例如直线和色块

## 第二层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvpmawn1j20ml0cs4cy.jpg)

CNN 的第二层捕捉了一些复杂的概念

如上图所示，CNN 的第二层认出了圈（第二行第二栏），条纹（第一行第二栏）和长方形（右下角）

CNN 是自己学着做这些事情的。 我们并没有设定让更深的网络层聚焦于更复杂的事物上。只要把训练数据输入 CNN，自然就会发生这样的事情

## 第三层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvqptyfkj20mz0a0k3h.jpg)

第三层捕捉了第二层特征的复杂组合。包括格子，蜂窝状（左上），轮子（第二行第二列）甚至脸（第三行第三列）

## 第五层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fntvrbf47zj208b0ae43y.jpg)

CNN第五层，也是最后一层的可视化。左边的灰色网络表示CNN的激活（或者说它"看到"了什么）。右边是相对应的原始图片

我们跳过了第四层（这一层同样遵循这个规律），直接跳到 CNN 的第五层，也是最后一层

最后一层选取了我们最关心的，可用作分类的概念，例如狗的脸，鸟的脸，自行车
