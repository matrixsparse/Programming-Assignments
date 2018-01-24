## 什么是神经网络？

神经网络是一个数学函数图表，例如线性组合 和激活函数。该图表包含节点和边

每层的节点（输入层的节点除外）都会使用上一层的节点中的输入进行数学函数计算。例如，节点可以表示 f(x,y)=x+y，其中 x 和 y 是上一层的节点中的输入值。

类似地，每个节点会创建一个输出值，并且可能会传递给下一层的节点。输出层的输出值不会传递到下一层（最后一层了！）

输入层和输出层之间的层叫做隐藏层

神经网络的工作就是预测对应的输出值 y，神经网络只要你喂给它足够多的数据，关于x和y的数据，给到足够多的x、y训练样本，神经网络非常擅长计算从x到y的精准映射函数

你会发现神经网络在有监督学习的环境下是如此的高效，你只要有一个输入x就可以将它映射成y

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fnb6aufoy6j216m14sncd.jpg)

## 用神经网络进行监督学习

迄今为止所有神经网络创造的经济价值都基于其中一种机器学习

在监督学习中，输入x，习得一个函数，映射成输出y

>神经网络应用领域

* 房屋价格预测（SNN）
* 在线广告预测（SNN）
* 计算机视觉（图像识别）（CNN）
* 语音识别，将音频片段输入神经网络，它可以输出文本（RNN）
* 机器翻译（RNNS）
* 无人驾驶汽车

RNN非常适合处理一维序列数据，其中包含时间成分，机器学习被应用于结构化数据和非结构化数据

## 神经网络基础

### 二分分类

例如：m个样本的训练集，你会习惯地去用一个for循环来遍历这m个样本

如果你要遍历整个数据集，并不需要

在神经网络的计算过程中，通常都有一个正向过程

### Logistic回归

### Logistic回归损失函数

## 前向传播

将值从第一层（输入层）通过每个节点表示的所有数学函数进行传播，网络会输出一个值。这种流程叫做前向传递

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fnb6e5e9y4j20qi0j8gp9.jpg)

节点和边形成了图表结构。虽然上面的示例很简单，但是不难理解，越来越复杂的图表可以计算几乎任何内容

通常，创建神经网络需要两个步骤：

* 定义节点和边图表
* 通过该图表传播值

MiniFlow 的流程也是相同的。你将用一种方法定义网络的节点和边，并用另一个方法在图表中传播值

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fnb6t59f1mj20ww0m40xn.jpg)

## MiniFlow 架构

我们看看如何用 MiniFlow 实现这一图表结构。我们将使用一个 Python 类来表示普通节点

```bash
class Node(object):
    def __init__(self):
        # Properties will go here!
```

我们知道，每个节点可能会从其他多个节点那接收输入

我们还知道，每个节点都会创建一个输出，这些输出有可能会传递给其他节点

我们添加以下两个列表：

* 一个用于存储对传入节点的引用
* 一个用于存储对传出节点的引用

```bash
class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
```

每个节点将最终计算出一个表示输出的值

我们将 value 初始化为 None，表示该值存在，但是尚未设定

```bash
class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        # A calculated value
        self.value = None
```

每个节点都必须能够将值向前传递，并进行反向传播

```bash
class Node(object):
    def __init__(self, inbound_nodes=[]):
        # Node(s) from which this Node receives values
        self.inbound_nodes = inbound_nodes
        # Node(s) to which this Node passes values
        self.outbound_nodes = []
        # For each inbound Node here, add this Node as an outbound Node to _that_ Node.
        for n in self.inbound_nodes:
            n.outbound_nodes.append(self)
        # A calculated value
        self.value = None

    def forward(self):
        """
        Forward propagation.

        Compute the output value based on `inbound_nodes` and
        store the result in self.value.
        """
        raise NotImplemented
```

## 可以进行计算的节点

虽然 Node 定义了每个节点都具有的基本属性，但是只有 Node 的特殊子类会出现在图表中
在本次实验练习中，你将构建可以进行计算和存储值的 Node 子类

```bash
class Input(Node):
    def __init__(self):
        # An Input node has no inbound nodes,
        # so no need to pass anything to the Node instantiator.
        Node.__init__(self)

    # NOTE: Input node is the only node where the value
    # may be passed as an argument to forward().
    #
    # All other node implementations should get the value
    # of the previous node from self.inbound_nodes
    #
    # Example:
    # val0 = self.inbound_nodes[0].value
    def forward(self, value=None):
        # Overwrite the value if one is passed in.
        if value is not None:
            self.value = value
```

与 Node 的其他子类不同，Input 子类实际上并不计算任何内容。Input 子类仅仅存储了一个 value，例如数据特征或模型参数（权重/偏置）

你可以明确地设置 value，或者用 forward() 方法进行设置。该值然后会传递给神经网络的其他节点

## Add 子类

Add 是 Node 的另一个子类，实际上可以进行计算（加法）

```bash
class Add(Node):
    def __init__(self, x, y):
        Node.__init__(self, [x, y])

    def forward(self):
        """
        You'll be writing code here in the next quiz!
        """
```

注意 __init__ 方法 Add.__init__(self, [x, y]) 的不同之处
Input 类没有传入节点，而 Add 类具有 2 个传入节点 x 和 y，并将这两个节点的值相加
