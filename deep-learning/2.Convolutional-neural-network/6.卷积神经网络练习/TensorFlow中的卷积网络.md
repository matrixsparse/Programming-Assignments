# TensorFlow 中的卷积网络

网络的结构跟经典的 CNNs 结构一样，是卷积层，最大池化层和全链接层的混合。

这里你看到的代码与你在 TensorFlow 深度神经网络的代码类似，我们按 CNN 重新组织了结构

## 数据集

你从之前的课程中见过这节课的代码。这里我们导入 MNIST 数据集，用一个方便的函数完成对数据集的 batch，缩放和独热编码。

```bash
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets(".", one_hot=True, reshape=False)

import tensorflow as tf

# Parameters
# 参数
learning_rate = 0.00001
epochs = 10
batch_size = 128

# Number of samples to calculate validation and accuracy
# Decrease this if you're running out of memory to calculate accuracy
# 用来验证和计算准确率的样本数
# 如果内存不够，可以调小这个数字
test_valid_size = 256

# Network Parameters
# 神经网络参数
n_classes = 10  # MNIST total classes (0-9 digits)
dropout = 0.75  # Dropout, probability to keep units
```

## Weights and Biases

```bash
# Store layers weight & bias
weights = {
    'wc1': tf.Variable(tf.random_normal([5, 5, 1, 32])),
    'wc2': tf.Variable(tf.random_normal([5, 5, 32, 64])),
    'wd1': tf.Variable(tf.random_normal([7*7*64, 1024])),
    'out': tf.Variable(tf.random_normal([1024, n_classes]))}

biases = {
    'bc1': tf.Variable(tf.random_normal([32])),
    'bc2': tf.Variable(tf.random_normal([64])),
    'bd1': tf.Variable(tf.random_normal([1024])),
    'out': tf.Variable(tf.random_normal([n_classes]))}
```

## 卷积

>3*3卷积滤波器

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu0k0mmsuj208q05dt8n.jpg)

这是一个 3x3 的卷积滤波器的示例

以 stride 为 1 应用到一个范围在 0 到 1 之间的数据上

每一个 3x3 的部分与权值 [[1, 0, 1], [0, 1, 0], [1, 0, 1]] 做卷积，把偏置加上后得到右边的卷积特征

这里偏置是 0 。TensorFlow 中这是通过 tf.nn.conv2d() 和 tf.nn.bias_add() 来完成的

```bash
def conv2d(x, W, b, strides=1):
    x = tf.nn.conv2d(x, W, strides=[1, strides, strides, 1], padding='SAME')
    x = tf.nn.bias_add(x, b)
    return tf.nn.relu(x)
```

tf.nn.conv2d() 函数与权值 W 做卷积。

在 TensorFlow 中，strides 是一个4个元素的序列；第一个位置表示 stride 的 batch 参数，最后一个位置表示 stride 的特征(feature)参数。最好的移除 batch 和特征(feature)的方法是你直接在数据集中把他们忽略，而不是使用 stride。要使用所有的 batch 和特征(feature)，你可以把第一个和最后一个元素设成1

中间两个元素指纵向(height)和横向(width)的 stride，之前也提到过 stride 通常是正方形，height = width。当别人说 stride 是 3 的时候，他们意思是 tf.nn.conv2d(x, W, strides=[1, 3, 3, 1])

为了更简洁，这里的代码用了tf.nn.bias_add() 来添加偏置。 tf.add() 这里不能使用，因为 tensors 的维度不同

## 最大池化

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu0lbhzy0j20lv0b3tbx.jpg)

上面是一个最大池化的示例。滤波器大小是 2x2，stride 是 2。左边是输入，右边是输出。 四个 2x2 的颜色代表每一次滤波器应用在左侧来构建右侧的最大结果。例如。[[1, 1], [5, 6]] 变成 6，[[3, 2], [1, 2]] 变成 3

```bash
def maxpool2d(x, k=2):
    return tf.nn.max_pool(
        x,
        ksize=[1, k, k, 1],
        strides=[1, k, k, 1],
        padding='SAME')
```

tf.nn.max_pool() 函数做的与你期望的一样，它通过设定 ksize 参数来设定滤波器大小，从而实现最大池化

## 模型

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu0me7vkdj20lm0c3dld.jpg)

在下面的代码中，我们创建了 3 层来实现卷积，最大池化以及全链接层和输出层。每一层对维度的改变都写在注释里。例如第一层在卷积部分把图片从 28x28x1 变成了 28x28x32。后面应用了最大池化，每个样本变成了 14x14x32。从 conv1 经过多层网络，最后到 output 生成 10 个分类

```bash
def conv_net(x, weights, biases, dropout):
    # Layer 1 - 28*28*1 to 14*14*32
    conv1 = conv2d(x, weights['wc1'], biases['bc1'])
    conv1 = maxpool2d(conv1, k=2)

    # Layer 2 - 14*14*32 to 7*7*64
    conv2 = conv2d(conv1, weights['wc2'], biases['bc2'])
    conv2 = maxpool2d(conv2, k=2)

    # Fully connected layer - 7*7*64 to 1024
    fc1 = tf.reshape(conv2, [-1, weights['wd1'].get_shape().as_list()[0]])
    fc1 = tf.add(tf.matmul(fc1, weights['wd1']), biases['bd1'])
    fc1 = tf.nn.relu(fc1)
    fc1 = tf.nn.dropout(fc1, dropout)

    # Output Layer - class prediction - 1024 to 10
    out = tf.add(tf.matmul(fc1, weights['out']), biases['out'])
    return out
```

## Session

```bash
# tf Graph input
x = tf.placeholder(tf.float32, [None, 28, 28, 1])
y = tf.placeholder(tf.float32, [None, n_classes])
keep_prob = tf.placeholder(tf.float32)

# Model
logits = conv_net(x, weights, biases, keep_prob)

# Define loss and optimizer
cost = tf.reduce_mean(\
    tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)\
    .minimize(cost)

# Accuracy
correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

# Initializing the variables
init = tf. global_variables_initializer()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)

    for epoch in range(epochs):
        for batch in range(mnist.train.num_examples//batch_size):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            sess.run(optimizer, feed_dict={
                x: batch_x,
                y: batch_y,
                keep_prob: dropout})

            # Calculate batch loss and accuracy
            loss = sess.run(cost, feed_dict={
                x: batch_x,
                y: batch_y,
                keep_prob: 1.})
            valid_acc = sess.run(accuracy, feed_dict={
                x: mnist.validation.images[:test_valid_size],
                y: mnist.validation.labels[:test_valid_size],
                keep_prob: 1.})

            print('Epoch {:>2}, Batch {:>3} -'
                  'Loss: {:>10.4f} Validation Accuracy: {:.6f}'.format(
                epoch + 1,
                batch + 1,
                loss,
                valid_acc))

    # Calculate Test Accuracy
    test_acc = sess.run(accuracy, feed_dict={
        x: mnist.test.images[:test_valid_size],
        y: mnist.test.labels[:test_valid_size],
        keep_prob: 1.})
    print('Testing Accuracy: {}'.format(test_acc))
```
