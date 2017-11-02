# 基于Python Flask开发的自用框架

## 项目结构

```bash
tree
.
├── library # 公共配置文件存放目录
│   └── config
│       └── development.py
├── logs # 日志文件存放目录
│   └── service_.2017-11-02.log
├── manage.py # 主运行文件
├── README.md # 项目介绍文件
├── service
│   └── application
│       ├── controllers
│       │   ├── data # 数据功能目录
│       │   │   ├── __init__.py
│       │   │   └── views.py # 数据视图配置文件
│       │   ├── main.py # main功能目录
│       │   └── spider # spider功能目录
│       │       ├── __init__.py
│       │       └── views.py # spider视图配置文件
│       └── __init__.py
├── static
│   └── README.md
└── templates # 静态页面存放目录
    ├── data # data模块页面存放目录
    │   └── index.html
    ├── index.html # 首页
    └── spider # spider模块页面存放目录
        └── index.html
```