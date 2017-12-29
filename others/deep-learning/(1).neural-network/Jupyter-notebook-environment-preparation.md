## Jupyter-notebook-environment-preparation

### Jupyter notebook

```bahs
Jupyter notebook 是一种Web文档，能让你将文本、图像和代码全部组合到一个文档中

它事实上已经成为数据分析的标准环境

Jupyter notebook源自2011年的IPython项目，之后迅速流行起来
```

### notebook 如何工作

```bash
Jupyter notebook源自Fernando Perez发起的IPython项目

IPython是一种交互式shell，与普通的Python shell相似，但具有一些很好的功能

最初，notebook 的工作方式是，将来自 Web 应用（你在浏览器中看到的 notebook）的消息发送给 IPython 内核（在后台运行的 IPython 应用程序）
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmwxlz17rzj212k0iudj7.jpg)

```bash
核心是 notebook 的服务器。你通过浏览器连接到该服务器，而 notebook 呈现为 Web 应用
你在 Web 应用中编写的代码通过该服务器发送给内核，内核运行代码，并将结果发送回该服务器。之后，任何输出都会返回到浏览器中
保存 notebook 时，它将作为 JSON 文件（文件扩展名为 .ipynb）写入到该服务器中。

此架构的一个优点是，内核无需运行 Python。由于 notebook 和内核分开，因此可以在两者之间发送任何语言的代码

例如，早期的两个非 Python 内核分别是 R 语言和 Julia 语言
使用 R 内核时，用 R 编写的代码将发送给执行该代码的 R 内核，这与在 Python 内核上运行 Python 代码完全一样

IPython notebook 已被改名，因为 notebook 变得与编程语言无关。新的名称 Jupyter 由 Julia、Python 和 R 组合而成。如果有兴趣，不妨看看可用内核的列表

另一个优点是，你可以在任何地方运行 notebook 服务器，并且可通过互联网访问服务器。通常，你会在存储所有数据和 notebook 文件的自有计算机上运行服务器。但是，你也可以在远程计算机或云实例（如 Amazon 的 EC2）上设置服务器。之后，你就可以在世界上任何地方通过浏览器访问 notebook
```

```bash
核心是 notebook 的服务器。在Web应用中编写的代码通过该服务器发送给内核，内核运行代码，并将结果发送回该服务器
之后，任何输出都会返回到浏览器中

保存 notebook 时，它将作为 JSON 文件（文件扩展名为 .ipynb）写入到该服务器中。

此架构的一个优点是，内核无需运行 Python。由于 notebook 和内核分开，因此可以在两者之间发送任何语言的代码。例如，早期的两个非 Python 内核分别是 R 语言和 Julia 语言。使用 R 内核时，用 R 编写的代码将发送给执行该代码的 R 内核，这与在 Python 内核上运行 Python 代码完全一样。IPython notebook 已被改名，因为 notebook 变得与编程语言无关。新的名称 Jupyter 由 Julia、Python 和 R 组合而成。如果有兴趣，不妨看看可用内核的列表。

另一个优点是，你可以在任何地方运行 notebook 服务器，并且可通过互联网访问服务器。通常，你会在存储所有数据和 notebook 文件的自有计算机上运行服务器。但是，你也可以在远程计算机或云实例（如 Amazon 的 EC2）上设置服务器。之后，你就可以在世界上任何地方通过浏览器访问 notebook
```

### 配置环境

```bash
[root@sparsematrix ~]# conda create -n siraj-regression python=2.7
```

### 激活环境

```bash
[root@sparsematrix ~]# source activate siraj-regression
```

### 安装Jupyter notebook

```bash
[root@sparsematrix ~]# conda install jupyter notebook
```

### 启动notebook服务器

```bash
[root@sparsematrix ~]# jupyter notebook
```

```bash
在浏览器地址栏中访问：http://localhost:8888
```

![All text](http://ww1.sinaimg.cn/large/dc05ba18gy1fmxan23r24j21vo0i8ap6.jpg)
