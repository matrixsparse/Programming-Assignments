#  first neural network

将会从头开始构建一个神经网络，基于真实的数据集来进行预测！

通过从零开始搭建神经网络，你将更好地理解`梯度下降`、`反向传播`等概念

这些都是以后接触更高级工具（如 Tensorflow）前必须掌握的重要概念

在这一项目中，你也将看到，如何运用这些网络来完成实际生活中的预测问题！

## 项目背景

```bash
自行车共享系统是一种新型的自行车租赁服务，从加入会员到租赁再到还回自行车的整个过程都是自动化的

用户可以通过这些系统轻松地从某个位置租赁自行车并在另一个位置还回自行车

目前，全球有超过 500 个自行车共享项目，并投入了超过 500 万辆自行车

如今，这类系统更是受到大量关注，因为它们可以缓解交通、环境和健康问题

除了自行车共享系统在现实生活中的有趣应用之外，这些系统生成的数据也具有独特的特性，吸引了人们去关注研究

与其他交通服务（例如公交或地铁）不同，这些系统会明确地记录行程时长、出发地点和抵达地点

这一特征使得自行车共享系统成为虚拟传感器网络，可以用来移动的感知一座城市的状

。因此，我们通过监控这些数据，一般都能检测到城市的大部分重大事件
```

## 关于数据集

```bash
自行车共享租赁行为与环境和季节之间的关联性很大

例如，天气条件、降水情况、周几、季节、一天的时刻等都会影响到租赁行为

核心数据集采用的是美国华盛顿特区 Capital Bikeshare 系统 2011 至 2012 年的两年间历史记录日志，该数据集可以被公开访问 (http://capitalbikeshare.com/system-data)

按照 2 小时间隔和每日间隔汇总了数据，然后提取并添加了相应的天气和季节性信息，天气信息来自 http://www.freemeteo.com。
```

## 项目任务

* 回归
    * 预测基于环境和季节性信息的每时或每日自行车租赁人数
* 事件和异常情况检测
	* 被租赁的自行车数还与城镇里的一些事件相关联，可以通过搜索引擎轻松地追踪这些事件
	* 例如，在 Google 中查询 "2012-10-30 washington d.c." 就会出现与飓风桑迪相关的结果

## 数据文件

```bash
hour.csv - 按照每小时汇总的共享自行车使用人数。记录数：17379 小时
day.csv - 按照每天汇总的共享自行车使用人数。记录数：731 天
```

## 数据集特征

```bash
hour.csv 和 day.csv 文件都具有以下字段，但是 day.csv 中没有 hr 字段
	- instant：记录索引
	- dteday：日期
	- season：季节（1：春季，2：夏季，3：秋季，4：冬季）
	- yr : 年份（0：2011 年，1：2012 年）
	- mnth：月份（1 到12 月）
	- hr : 小时（0 到 23 时）
	- holiday: 当天是否是假期（数据来自 http://dchr.dc.gov/page/holiday-schedule）
	- weekday: 星期几
	- workingday: 如果不是周末或假期则是 1 ，否则是 0。
	+ weathersit :
		- 1: 晴朗、飘着几朵云、局部多云
		- 2: 薄雾加多云、薄雾加碎云、薄雾加几朵云、薄雾
		- 3: 小雪、小雨加雷暴加散云、小雨加散云
		- 4: 大雨加冰雹加雷暴加薄雾、下雪加雾
	- temp: 标准化温度（摄氏度）。标准化后的值为原数据除以41（最大值）
	- atemp: 标准化体感温度（摄氏度）。标准化后的值为原数据除以50（最大值）
	- hum: 标准化湿度。标准化后的值为原数据除以100（最大值）
	- windspeed: 标准化风速。标准化后的值为原数据除以67（最大值）
	- casual: 临时用户数
	- registered: 注册用户数
	- cnt: 租赁自行车总用户数（包括临时用户和注册用户）
```

## 准备环境

### 创建一个新的 conda 环境

```bash
conda create --name dlnd python=3
```

### 查看所有环境

```bash
conda env list
```

### 进入新环境

```bash
source activate dlnd
```

### 安装 numpy , matplotlib , pandas 和 jupyter notebook

```bash
conda install numpy matplotlib pandas jupyter notebook
```

### 下载项目

```bash
git clone https://github.com/udacity/cn-deep-learning.git
```

### 打开notebook

```bash
jupyter notebook matrix_first_neural_network.ipynb --ip=0.0.0.0
```

### 后台启动notebook

```bash
nohup jupyter notebook matrix_first_neural_network.ipynb --ip=0.0.0.0 >/dev/null 2>&1 &
```

### 在浏览器地址栏访问

```bash
http://服务器ip:8888/notebooks/matrix_first_neural_network.ipynb
```

### 注销环境

```bash
source deactivate
```

## 构建神经网络，用该网络预测每日自行车租客人数

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2018, matrix

import numpy as np

# 实现 S 型激活函数。将 __init__ 中的 self.activation_function 设为你的 S 型函数
# 在 train 方法中实现前向传递
# 在 train 方法中实现反向传播算法，包括计算输出错误
# 在 run 方法中实现前向传递

class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.input_nodes ** -0.5,
                                                        (self.input_nodes, self.hidden_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.hidden_nodes ** -0.5,
                                                         (self.hidden_nodes, self.output_nodes))
        self.lr = learning_rate

        #### TODO: Set self.activation_function to your implemented sigmoid function ####
        #
        # Note: in Python, you can define a function with a lambda expression,
        # as shown below.
        self.activation_function = lambda x: 1 / (1 + np.exp(-x)) # Replace 0 with your sigmoid calculation.

        ### If the lambda code above is not something you're familiar with,
        # You can uncomment out the following three lines and put your
        # implementation there instead.
        #
        # def sigmoid(x):
        #    return 0  # Replace 0 with your sigmoid calculation here
        # self.activation_function = sigmoid

    def train(self, features, targets):
        ''' Train the network on batch of features and targets.

            Arguments
            ---------

            features: 2D array, each row is one data record, each column is a feature
            targets: 1D array of target values

        '''
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        for X, y in zip(features, targets):
            #### Implement the forward pass here ####
            ### Forward pass ###
            # TODO: Hidden layer - Replace these values with your calculations.
            hidden_inputs = np.dot(X, self.weights_input_to_hidden)  # signals into hidden layer
            hidden_outputs = self.activation_function(hidden_inputs)  # signals from hidden layer

            # TODO: Output layer - Replace these values with your calculations.
            final_inputs = np.dot(hidden_outputs, self.weights_hidden_to_output)  # signals into final output layer
            final_outputs = final_inputs  # signals from final output layer

            #### Implement the backward pass here ####
            ### Backward pass ###

            # TODO: Output error - Replace this value with your calculations.
            error = y - final_outputs  # Output layer error is the difference between desired target and actual output.

            # TODO: Calculate the hidden layer's contribution to the error
            hidden_error = np.dot(self.weights_hidden_to_output, error)

            # TODO: Backpropagated error terms - Replace these values with your calculations.
            output_error_term = error
            hidden_error_term = hidden_error * hidden_outputs * (1 - hidden_outputs)

            # Weight step (input to hidden)
            delta_weights_i_h += hidden_error_term * X[:, None]
            # Weight step (hidden to output)
            delta_weights_h_o += output_error_term * hidden_outputs[:, None]

        # TODO: Update the weights - Replace these values with your calculations.
        self.weights_hidden_to_output += self.lr * delta_weights_h_o / n_records  # update hidden-to-output weights with gradient descent step
        self.weights_input_to_hidden += self.lr * delta_weights_i_h / n_records  # update input-to-hidden weights with gradient descent step

    def run(self, features):
        ''' Run a forward pass through the network with input features

            Arguments
            ---------
            features: 1D array of feature values
        '''

        #### Implement the forward pass here ####
        # TODO: Hidden layer - replace these values with the appropriate calculations.
        hidden_inputs = np.dot(features, self.weights_input_to_hidden)  # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)  # signals from hidden layer

        # TODO: Output layer - Replace these values with the appropriate calculations.
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_to_output)  # signals into final output layer
        final_outputs = final_inputs  # signals from final output layer

        return final_outputs
```

训练网络
现在你将设置网络的超参数。策略是设置的超参数使训练集上的错误很小但是数据不会过拟合。如果网络训练时间太长，或者有太多的隐藏节点，可能就会过于针对特定训练集，无法泛化到验证数据集。即当训练集的损失降低时，验证集的损失将开始增大

你还将采用随机梯度下降 (SGD) 方法训练网络。对于每次训练，都获取随机样本数据，而不是整个数据集。与普通梯度下降相比，训练次数要更多，但是每次时间更短。这样的话，网络训练效率更高。稍后你将详细了解 SGD。

选择迭代次数
也就是训练网络时从训练数据中抽样的批次数量。迭代次数越多，模型就与数据越拟合。但是，如果迭代次数太多，模型就无法很好地泛化到其他数据，这叫做过拟合。你需要选择一个使训练损失很低并且验证损失保持中等水平的数字。当你开始过拟合时，你会发现训练损失继续下降，但是验证损失开始上升。

选择学习速率
速率可以调整权重更新幅度。如果速率太大，权重就会太大，导致网络无法与数据相拟合。建议从 0.1 开始。如果网络在与数据拟合时遇到问题，尝试降低学习速率。注意，学习速率越低，权重更新的步长就越小，神经网络收敛的时间就越长

选择隐藏节点数量
隐藏节点越多，模型的预测结果就越准确。尝试不同的隐藏节点的数量，看看对性能有何影响。你可以查看损失字典，寻找网络性能指标。如果隐藏单元的数量太少，那么模型就没有足够的空间进行学习，如果太多，则学习方向就有太多的选择。选择隐藏单元数量的技巧在于找到合适的平衡点
