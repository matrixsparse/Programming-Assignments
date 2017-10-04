# 十分钟pandas入门教程

## 导入pandas、numpy、matplotlib

```bash
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

## 创造对象

Series是一个值的序列，它只有一个列，以及索引，默认整数索引

```bash
a = pd.Series([1,3,5,np.nan,6,8])
print(a)
```

>运行结果

```bash
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
```

DataFrame是有多个列的数据表，每个列拥有一个label

```bash
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(a)
dates = pd.date_range('20170101', periods=6)
print(dates)
```

>运行结果

```bash
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06'],
              dtype='datetime64[ns]', freq='D')
```

```bash
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(a)
dates = pd.date_range('20170101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.rand(6, 4), index=dates, columns=list('ABCD'))
print(df)
```

>运行结果

```bash
A         B         C         D
2017-01-01  0.686463  0.640448  0.321730  0.827738
2017-01-02  0.464855  0.238475  0.309914  0.324678
2017-01-03  0.067551  0.138465  0.481597  0.138893
2017-01-04  0.264497  0.519291  0.654733  0.755564
2017-01-05  0.585134  0.507593  0.073583  0.016813
2017-01-06  0.133052  0.261013  0.441546  0.732402
```
