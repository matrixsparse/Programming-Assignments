# Python编码问题

>demo.py

```bash
# -*- coding: utf-8 -*-

import os

path = '../BOTDATA/HOSP'

if os.path.exists('%s'):
    pass
else:
    os.makedirs('%s')

# 创建with BOM文件
f1 = open('{}/test1.top'.format(path), 'w', encoding='utf-8-sig')
f1.write('测试1')
f1.write('注意，这是测试1\n')
f1.close()

# 创建无BOM文件
f2 = open('{}/test2.top'.format(path), 'w', encoding='utf-8')
f2.write('测试2')
f2.write('注意，这是测试\n')
f2.close()
```

>查看test1.top编码

```bash
file test1.top
```

```bash
test1.top: UTF-8 Unicode (with BOM) text
```

>查看test2.top编码

```bash
file test2.top
```

```bash
test2.top: UTF-8 Unicode text
```