## style transfer【风格迁移】

>对于OS X 和 Linux，需要安装 TensorFlow 0.11.0、Python 2.7.9、Pillow 3.4.2、scipy 0.18.1 和 numpy 1.11.2.

神经网络按照的几种不同风格进行了训练，并保存在检查点文件中。检查点文件包含了关于已训练神经网络的所有信息，可以将风格应用到新的图片上

### 创建一个新的环境

存储格式迁移代码所需的程序包

```bash
sparsematrix:Desktop matrix$ conda create -n style-transfer python=2.7.9
```

### 进入环境

```bash
sparsematrix:Desktop matrix$ source activate style-transfer
discarding /Users/matrix/anaconda/bin from PATH
prepending /Users/matrix/anaconda/envs/style-transfer/bin to PATH
```

### 安装TensorFlow、Scipy 和 Pillow（一种图像处理库）

```bash
(style-transfer)sparsematrix:Desktop matrix$ pip install tensorflow
```

```bash
(style-transfer)sparsematrix:Desktop matrix$ conda install scipy pillow
```

>下载github项目

```bash
(style-transfer)sparsematrix:Desktop matrix$ git clone https://github.com/lengstrom/fast-style-transfer.git
```

>查看python版本

```bash
(style-transfer)sparsematrix:Desktop matrix$ python -V
Python 2.7.13 :: Continuum Analytics, Inc.
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmw6qfz0uoj210i0vch1b.jpg)

>准备训练的图片

```bash
(style-transfer)sparsematrix:fast-style-transfer matrix$ python evaluate.py --checkpoint ./rain-princess.ckpt --in-path ./dog.jpg --out-path ./output_image.jpg
2017-12-28 08:35:11.264410: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.2 AVX AVX2 FMA【This isn't an error, just warnings saying if you build TensorFlow from source it can be faster on your machine.】
```

>风格迁移到图片上

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmw6qga9plj210o0vk1kx.jpg)
