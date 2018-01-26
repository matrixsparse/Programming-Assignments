# TensorFlow 最大池化

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu0h2rnt5j20f70a0jrp.jpg)

这是一个最大池化的例子max pooling 用了 2x2 的滤波器 stride 为 2。四个 2x2 的颜色代表滤波器移动每个步长所产出的最大值

例如 [[1, 0], [4, 6]] 生成 6，因为 6 是这4个数字中最大的。同理 [[2, 3], [6, 8]] 生成 8

理论上，最大池化操作的好处是减小输入大小，使得神经网络能够专注于最重要的元素。最大池化只取覆盖区域中的最大值，其它的值都丢弃

TensorFlow 提供了 tf.nn.max_pool() 函数，用于对卷积层实现 最大池化

```bash
conv_layer = tf.nn.conv2d(input, weight, strides=[1, 2, 2, 1], padding='SAME')
conv_layer = tf.nn.bias_add(conv_layer, bias)
conv_layer = tf.nn.relu(conv_layer)
# Apply Max Pooling
conv_layer = tf.nn.max_pool(
    conv_layer,
    ksize=[1, 2, 2, 1],
    strides=[1, 2, 2, 1],
    padding='SAME')
```

tf.nn.max_pool() 函数实现最大池化时， ksize参数是滤波器大小，strides参数是步长。2x2 的滤波器配合 2x2 的步长是常用设定

ksize 和 strides 参数也被构建为四个元素的列表，每个元素对应 input tensor 的一个维度 ([batch, height, width, channels])

对 ksize 和 strides 来说，batch 和 channel 通常都设置成 1
