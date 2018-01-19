# Mini-batch

Mini-batching 是一个一次训练数据集的一小部分，而不是整个训练集的技术

它可以使内存较小、不能同时训练整个数据集的电脑也可以训练模型

Mini-batching 从运算角度来说是低效的，因为你不能在所有样本中计算 loss

但是这点小代价也比根本不能运行模型要划算

它跟随机梯度下降（SGD）结合在一起用也很有帮助

方法是在每一代训练之前，对数据进行随机混洗

然后创建 mini-batches，对每一个 mini-batch，用梯度下降训练网络权重

因为这些 batches 是随机的，你其实是在对每个 batch 做随机梯度下降（SGD）

让我们看看你的机器能否训练出 MNIST 数据集的权重和偏置项

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2018, matrix

import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf

n_input = 784  # MNIST data input (img shape: 28*28)
n_classes = 10  # MNIST total classes (0-9 digits)

# Import MNIST data
mnist = input_data.read_data_sets('/datasets/ud730/mnist', one_hot=True)

# The features are already scaled and the data is shuffled
train_features = mnist.train.images
test_features = mnist.test.images

train_labels = mnist.train.labels.astype(np.float32)
test_labels = mnist.test.labels.astype(np.float32)

# Weights & bias
weights = tf.Variable(tf.random_normal([n_input, n_classes]))
bias = tf.Variable(tf.random_normal([n_classes]))
```

输入、权重和偏置项总共的内存空间需求是 174MB，并不是太多

你可以在 CPU 和 GPU 上训练整个数据集

但将来你要用到的数据集可能是以 G 来衡量，甚至更多。你可以买更多的内存，但是会很贵。例如一个 12GB 显存容量的 Titan X GPU 会超过 1000 美金。所以，为了在你自己机器上运行大模型，你需要学会用 mini-batching。

让我们看下如何在 TensorFlow 下实现 mini-batching

## TensorFlow Mini-batching

要使用 mini-batching，你首先要把你的数据集分成 batch

不幸的是，有时候不可能把数据完全分割成相同数量的 batch

例如有 1000 个数据点，你想每个 batch 有 128 个数据

但是 1000 无法被 128 整除

你得到的结果是其中 7 个 batch 有 128 个数据点，一个 batch 有 104 个数据点。(7*128 + 1*104 = 1000)

batch 里面的数据点数量会不同的情况下

你需要利用 TensorFlow 的 tf.placeholder() 函数来接收这些不同的 batch

继续上述例子，如果每个样本有 n_input = 784 特征，n_classes = 10 个可能的标签

features 的维度应该是 [None, n_input]，labels 的维度是 [None, n_classes]

```bash
# Features and Labels
features = tf.placeholder(tf.float32, [None, n_input])
labels = tf.placeholder(tf.float32, [None, n_classes])
```

### None 在这里做什么用呢？

None 维度在这里是一个 batch size 的占位符

在运行时，TensorFlow 会接收任何大于 0 的 batch size

回到之前的例子，这个设置可以让你把 features 和 labels 给到模型

无论 batch 中包含 128，还是 104 个数据点


## 对 features 和 labels 实现一个 batches 函数

这个函数返回每个有最大 batch_size 数据点的 batch

```bash
# 4 个特征
example_features = [
    ['F11','F12','F13','F14'],
    ['F21','F22','F23','F24'],
    ['F31','F32','F33','F34'],
    ['F41','F42','F43','F44']]
# 4 个 label
example_labels = [
    ['L11','L12'],
    ['L21','L22'],
    ['L31','L32'],
    ['L41','L42']]

example_batches = batches(3, example_features, example_labels)
```

>example_batches 变量如下

```bash
[
    # 分 2 个 batch:
    #   第一个 batch 的 size 是 3
    #   第二个 batch 的 size 是 1
    [
        # size 为 3 的第一个 Batch
        [
            # 3 个特征样本
            # 每个样本有四个特征
            ['F11', 'F12', 'F13', 'F14'],
            ['F21', 'F22', 'F23', 'F24'],
            ['F31', 'F32', 'F33', 'F34']
        ], [
            # 3 个标签样本
            # 每个标签有两个 label
            ['L11', 'L12'],
            ['L21', 'L22'],
            ['L31', 'L32']
        ]
    ], [
        # size 为 1 的第二个 Batch 
        # 因为 batch size 是 3。所以四个样品中只有一个在这里。
        [
            # 1 一个样本特征
            ['F41', 'F42', 'F43', 'F44']
        ], [
            # 1 个 label
            ['L41', 'L42']
        ]
    ]
]
```