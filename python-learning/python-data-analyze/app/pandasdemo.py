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
