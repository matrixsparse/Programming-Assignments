# Keras 中的卷积层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu1asqka0j20ah09ata2.jpg)

## Keras 中的卷积层

要在 Keras 中创建卷积层，你首先必须导入必要的模块：

```bash
from keras.layers import Conv2D
```

你可以通过使用以下格式创建卷积层：

```bash
Conv2D(filters, kernel_size, strides, padding, activation='relu', input_shape)
```

## 参数

必须传递以下参数：

* filters - 过滤器数量
* kernel_size - 指定（方形）卷积窗口的高和宽的数字

你可能还需要调整其他可选参数：

* strides - 卷积 stride。如果不指定任何值，则 strides 设为 1
* padding - 选项包括 'valid' 和 'same'。如果不指定任何值，则 padding 设为 'valid'
* activation - 通常为 'relu'。如果未指定任何值，则不应用任何激活函数。强烈建议你向网络中的每个卷积层添加一个 ReLU 激活函数

注意：可以将 kernel_size 和 strides 表示为数字或元组

在模型中将卷积层当做第一层级（出现在输入层之后）时，必须提供另一个 input_shape 参数：

* input_shape - 指定输入的高度、宽度和深度（按此顺序）的元组

注意：如果卷积层不是网络的第一个层级，请勿包含 input_shape 参数

你还可以设置很多其他元组参数，以便更改卷积层的行为。要详细了解这些参数，建议参阅官方文档

## 示例 1

假设我要构建一个 CNN，输入层接受的是 200 x 200 像素（对应于高 200、宽 100、深 1 的三维数组）的灰度图片。然后，假设我希望下一层级是卷积层，具有 16 个过滤器，每个宽和高分别为 2。在进行卷积操作时，我希望过滤器每次跳转 2 个像素。并且，我不希望过滤器超出图片界限之外；也就是说，我不想用 0 填充图片。要构建该卷积层，我将使用下面的代码：

```bash
Conv2D(filters=16, kernel_size=2, strides=2, activation='relu', input_shape=(200, 200, 1))
```

## 示例 2

假设我希望 CNN 的下一层级是卷积层，并将示例 1 中构建的层级作为输入。假设新层级是 32 个过滤器，每个的宽和高都是 3。在进行卷积操作时，我希望过滤器每次移动 1 个像素。我希望卷积层查看上一层级的所有区域，因此不介意过滤器在进行卷积操作时是否超过上一层级的边缘。然后，要构建此层级，我将使用以下代码：

```bash
Conv2D(filters=32, kernel_size=3, padding='same', activation='relu')
```

## 示例 3

如果在线查看代码，经常会在 Keras 中见到以下格式的卷积层：

```bash
Conv2D(64, (2,2), activation='relu')
```

在这种情况下，有 64 个过滤器，每个的大小是 2x2，层级具有 ReLU 激活函数。层级中的其他参数使用默认值，因此卷积的 stride 为 1，填充设为 'valid'
