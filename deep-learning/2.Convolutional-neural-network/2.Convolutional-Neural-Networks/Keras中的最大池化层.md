# Keras 中的最大池化层

![All text](http://ww1.sinaimg.cn/large/dc05ba18ly1fnu1hd8czwj20ln0b2n0c.jpg)

## Keras 中的最大池化层

要在 Keras 中创建最大池化层，你必须首先导入必要的模块：

```bash
from keras.layers import MaxPooling2D
```

使用以下格式创建卷积层：

```bash
MaxPooling2D(pool_size, strides, padding)
```

## 参数

* pool_size - 指定池化窗口高度和宽度的数字
* strides - 垂直和水平 stride。如果不指定任何值，则 strides 默认为 pool_size
* padding - 选项包括 'valid' 和 'same'。如果不指定任何值，则 padding 设为 'valid'。
注意：可以将 pool_size 和 strides 表示为数字或元组
