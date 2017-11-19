# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2017, matrix

import os

__all__ = []

# 加载services目录下的所有模块
for filename in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    _module_name, suffix = os.path.splitext(filename)
    if not _module_name.startswith('_') and (suffix == '.py' or suffix == '.pyc'):
        __all__.append(_module_name)

if __name__ == "__main__":
    print(__all__)
