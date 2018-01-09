## 什么是神经网络？

神经网络是一个数学函数图表，例如线性组合 和激活函数。该图表包含节点和边

每层的节点（输入层的节点除外）都会使用上一层的节点中的输入进行数学函数计算。例如，节点可以表示 f(x,y)=x+y，其中 x 和 y 是上一层的节点中的输入值。

类似地，每个节点会创建一个输出值，并且可能会传递给下一层的节点。输出层的输出值不会传递到下一层（最后一层了！）

输入层和输出层之间的层叫做隐藏层

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fnb6aufoy6j216m14sncd.jpg)

## 前向传播

将值从第一层（输入层）通过每个节点表示的所有数学函数进行传播，网络会输出一个值。这种流程叫做前向传递

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fnb6e5e9y4j20qi0j8gp9.jpg)

## 图表

节点和边形成了图表结构。虽然上面的示例很简单，但是不难理解，越来越复杂的图表可以计算几乎任何内容

通常，创建神经网络需要两个步骤：

定义节点和边图表。
通过该图表传播值。
MiniFlow 的流程也是相同的。你将用一种方法定义网络的节点和边，并用另一个方法在图表中传播值

## MiniFlow 架构

我们看看如何用 MiniFlow 实现这一图表结构。我们将使用一个 Python 类来表示普通节点

```bash
class Node(object):
    def __init__(self):
        # Properties will go here!
```

我们知道，每个节点可能会从其他多个节点那接收输入。我们还知道，每个节点都会创建一个输出，这些输出有可能会传递给其他节点
我们添加以下两个列表：一个用于存储对传入节点的引用，另一个用于存储对传出节点的引用

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

每个节点将最终计算出一个表示输出的值。我们将 value 初始化为 None，表示该值存在，但是尚未设定

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
