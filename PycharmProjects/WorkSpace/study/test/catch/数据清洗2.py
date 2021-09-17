import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tushare as ts


pd.set_option('display.max_columns', 100)  # 设置显示数据的最大列数，防止出现省略号…，导致数据显示不全
pd.set_option('expand_frame_repr', False)  # 当列太多时不自动换行


pro = ts.pro_api()
df = pro.daily(ts_code='600000.SH', start_date='20190401', end_date='20190430')
df.head() # 查看前n行数据，默认值是5
df.tail() # 查看后n行数据，默认值是5
df.shape # 查看数据维数
df.columns # 查看所有列名
df.info() # 查看索引、数据类型和内存信息
df['close'].value_counts(dropna=False) # .value_counts() 查看Series对象的唯一值和计数值
df['close'].plot(kind='hist', rot=0)
plt.show()