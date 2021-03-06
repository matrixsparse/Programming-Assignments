# evaluation-index

```bash
评估指标用于评价你的机器学习算法，是否得到改善，以及你的总体表现如何
```

* 如何应用评估方法，衡量结果的成效？

## 选择合适的指标

```bash
在构建机器学习模型时，我们首先要选择性能指标，然后测试模型的表现如何

相关的指标有多个，具体取决于我们要尝试解决的问题

机器学习研究的是如何学习根据数据进行预测

将重点关注创建分类或创建预测回归类型的已标记数据
```

```bash
在测试模型的时候，务必要将数据集分解为训练数据和测试数据
```

## 分类和回归

### 分类

根据离散数据进行预测的模型，此类模型确定新实例是否属于给定的一组类别

```bash
分类涉及到根据未见过的样本进行预测，并确定新实例属于哪个类别
```

```bash
根据蓝色或红色或者方形或圆形来组织对象，以便在看到新对象时根据其特征来组织对象
```

>更加关注

```bash
模型隔多久正确或不正确地识别新样本一次
```

### 回归

```bash
根据连续数据来进行预测
```

```bash
例如有包含不同人员的身高、年龄和性别的列表，并想预测他们的体重
```

>更加关注

```bash
更关注模型的预测值与真正值之间差多少
```

>回归指标

回归的默认指标`分数越高越好`

```bash
根据连续数据进行预测的模型，更关注预测的接近程度

例如：对于身高和体重预测，我们不是跟关心模型能否将某人体重100%准确地预测到小于零点几磅

但可能很关心模型，如何能始终进行接近的预测(可能与个人的真实体重相差3~4磅)
```

## 准确率

看特定类的表现，需要看召回率

```bash
准备率实际上是所有被正确标示的数据点除以所有的数据点
```

```bash
准备率【精度】指特定类别中我们正确标记并正确识别为此类别的项目或数据点的数量,除以该类别中全部项目或数据点的数量
```

>准确率的缺陷

```bash

```

## 混淆矩阵[confusion matrices]

```bash
想象有一个分类器
在这条线上方，是红色的X【将红色X称为正例示例】
在这条线下方，是绿色的圈【将绿色圈称为负面示例】
```

```bash
混淆矩阵是一个二乘二的矩阵，对照实际类，它可分为正例或负例，输出值也可为正例或负例
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1flppv8ifsjj20is05ytai.jpg)

```bash
右边点的数量将会增加左边的计数
```

## 精确率[called precision]&召回率[recall]

>精确率

```bash
准确识别的次数比率
```

>召回率

```bash

```

## F1分数

F1分数为精确率和召回率的加权平均值

F1分数的最佳值为1、最差值为0

```bash
F1 = 2 * (精确率 * 召回率) / (精确率 + 召回率)
```

## 平均绝对误差

```bash
在统计学中可以使用绝对误差来测量误差，以找出预测值与真实值之间的差距

平均绝对误差的计算方法：将各个样本的绝对误差汇总，然后根据数据点数量求出平均误差

通过将模型的所有绝对值加起来，可以避免因预测值比真实值过高或过低而抵消误差，并能获得用于评估模型的整体误差指标
```

## 均方误差

```bash
均方误差是一个经常用于测量模型性能的指标，与绝对误差相比，残差(预测值与真实值的差值)
被求平方

对残差求平方的一些好处是，自动将所有误差转换为正数、注重较大的误差而不是较小的误差以及在微积分汇总是可微的(可让我们找到最小值和最大值)
```

## 回归分数函数

```bash
scikit-learn还包括了两个分数指标，范围通产从0到1，值0为坏，而值1位最好的表现

看起来和分类指标类似，都是数字越接近1.0分数就越好
```