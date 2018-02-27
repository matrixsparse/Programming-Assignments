## keras介绍

Keras是一个高层神经网络API，Keras由纯Python编写而成并基Tensorflow、Theano以及CNTK后端

Keras 为支持快速实验而生，能够把你的idea迅速转换为结果，如果你有如下需求，请选择Keras：

* 简易和快速的原型设计（keras具有高度模块化，极简，和可扩充特性）
* 支持CNN和RNN，或二者的结合
* 无缝CPU和GPU切换

## keras中文文档

```bash
https://keras-cn.readthedocs.io/en/latest/
https://keras-cn.readthedocs.io/en/latest/backend/
```

## 准备环境

### 创建一个新的 conda 环境

```bash
conda create --name keras python=3.6
```

### 查看所有环境

```bash
conda env list
```

### 进入新环境

```bash
source activate keras
```

### 安装numpy、pandas、keras、jupyter notebook

```bash
conda install numpy pandas keras jupyter notebook
```

## Keras后端

### 什么是"后端"

Keras是一个模型级的库，提供了快速构建深度学习网络的模块

Keras并不处理如张量乘法、卷积等底层操作

这些操作依赖于某种特定的、优化良好的张量操作库

Keras依赖于处理张量的库就称为"后端引擎"

Keras提供了三种后端引擎Theano/Tensorflow/CNTK，并将其函数统一封装，使得用户可以以同一个接口调用不同后端引擎的函数
* Theano是一个开源的符号主义张量操作框架，由蒙特利尔大学LISA/MILA实验室开发
* TensorFlow是一个符号主义的张量操作框架，由Google开发
* CNTK是一个由微软开发的商业级工具包。

## keras安装

>源码安装

```bash
git clone https://github.com/fchollet/keras.git
```

```bash
python setup.py install
```
