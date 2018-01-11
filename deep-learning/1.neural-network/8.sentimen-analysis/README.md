# sentiment analysis

深度学习就是一套工具，根据已知的数据，通过使用神经网络，预测我们想要知道的事物

```bash
自然语言处理就是对人类语言的研究，使用一系列工具，如机器学习

将学习情感分类，这种分类能够判断人类生成的一段文字是正面或是负面的

所以在此情况下，我们已知一段人类生成的语言文本，想要预测的是这些正面或负面标签之一
```

神经网络所做的唯一的事情就是搜索两个数据集之间直接或间接的`相关性`

```bash
为了让神经网络来做训练，我们需要给它提供2个有意义的数据集

第一个数据集必须代表我们已知的信息
第二个数据集必须代表我们想要知道的信息
```

* Sentiment_Classification_Projects.ipynb - 这个迷你项目的 notebook，你会用它来练习和完成迷你项目。
* Sentiment_Classification_Solutionss.ipynb - 含有 Andrew 对课程迷你项目解决方案的 notebook，可供你参考
* reviews.txt - 含有 25000 条影评
* labels.txt - 针对 reviews.txt 中的影评的 positive/negative 情感标签

## 激活 python3 conda 环境

```bash
[root@sparsematrix ~]# conda create --name sentiment-analysis python=3.6
```

### 进入新环境

```bash
source activate sentiment-analysis
```

## 安装 numpy、jupyter、notebook、matplotlib、scikit-learn、bokeh

```bash
conda install numpy jupyter notebook matplotlib scikit-learn bokeh
```

## 下载项目

```bash
git clone https://github.com/udacity/cn-deep-learning.git
```

```bash
cd cn-deep-learning/tutorials／sentiment-network
```

## 启动 Jupyter notebook 服务器

```bash
jupyter notebook Sentiment_Classification_Projects.ipynb --ip=0.0.0.0
```

## 打开 Sentiment_Classification_Projects.ipynb

>在浏览器地址栏访问

```bash
http://服务器ip:8888/notebooks/Sentiment_Classification_Projects.ipynb
```

## 退出环境

```bash
source deactivate
```
