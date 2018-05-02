# Python生成日期

## 循环生成日期

```bash
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Copyright (C), 2018, matrix.wang
import datetime


def main():
    begin = datetime.date(2017, 12, 1)
    end = datetime.date(2018, 5, 2)

    for i in range((end - begin).days + 1):
        day = begin + datetime.timedelta(days=i)
        print 'python init.py '+ ''.join(str(day).split('-'))
        # os.system('python init.py '+ ''.join(str(day).split('-')))


if __name__ == '__main__':
    main()
```
