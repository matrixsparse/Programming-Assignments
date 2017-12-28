## Anaconda environment preparation

### Anaconda简介

Anaconda是一个包含数据科学常用包的Python发行版本

它基于conda一个包和环境管理器——衍生而来

你可以使用 conda 创建环境，以便分隔使用不同Python版本和不同程序包的项目

你还将使用它在环境中安装、卸载和更新包

通过使用 Anaconda，处理数据的过程将更加愉快

Anaconda能让你在数据科学的工作中轻松安装经常使用的程序包

你还将使用它创建虚拟环境，以便更轻松地处理多个项目

Anaconda简化了工作流程，并且解决了多个包和Python版本之间遇到的大量问题

```bash
包管理器用于在计算机上安装库和其他软件

你可能已经熟悉 pip，它是 Python 库的默认包管理器

conda 与 pip 相似，不同之处是

conda：可用的包以数据科学包为主
pip ：适合一般用途

conda 并非像pip那样专门适用于Python，它也可以安装非Python的包

它是支持任何软件的包管理器。也就是说，虽然并非所有的 Python 库都能通过 Anaconda 发行版和 conda 获得

但同时它也支持非 Python 库的获得

使用 conda 的同时，你仍可以使用 pip 来安装包

Conda 安装了预编译的包。例如，Anaconda 发行版附带了使用 MKL 库编译的 Numpy、Scipy 和 Scikit-learn，从而加快了各种数学运算的速度

这些包由发行版的贡献者维护，这意味着它们通常滞后于最新版本

由于有人需要利用这些包来进行系统构建，因此它们往往更为稳定，而且也更便于你使用
```

```bash
除了管理包之外，conda 还是虚拟环境管理器。它类似于另外两个很流行的环境管理器，即 virtualenv和pyenv。

环境能让你分隔用于不同项目的包

你的代码可能使用了Numpy中的新功能，或者使用了已删除的旧功能

实际上，不可能同时安装两个Numpy版本

你要做的应该是，为每个Numpy版本创建一个环境，然后项目的对应环境中工作

在应对 Python 2 和 Python 3 时，此问题也会常常发生

你可能会使用在 Python 3 中不能运行的旧代码，以及在 Python 2 中不能运行的新代码

同时安装两个版本可能会造成许多混乱和错误，而创建独立的环境会好很多
```

>将环境中的包列表导出为文件，然后将该文件与代码包括在一起，让其他人轻松加载代码的所有依赖项

```
pip提供了类似的功能，即 pip freeze > requirements.txt。
```

### 安装 Anaconda

```bash
Anaconda可用于Windows、Mac OS X 和 Linux

可以在https://www.continuum.io/downloads上找到安装程序和安装说明。
```

```bash
如果计算机上已经安装了 Python，这不会有任何影响。实际上，脚本和程序使用的默认 Python 是 Anaconda 附带的 Python。

选择 Python 3.6 版本（你也可以根据具体的需要选择 Python 2 的版本）

此外，如果是 64 位操作系统，则选择 64 位安装程序，否则选择 32 位安装程序。继续并选择合适的版本，然后安装它。之后，继续进行！
```

>查看安装的内容

```bash
conda list
```

### 环境操作

>保存和加载环境

>列出环境

>删除环境
