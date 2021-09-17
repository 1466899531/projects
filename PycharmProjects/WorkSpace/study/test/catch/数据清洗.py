import pandas as pd
import numpy as np
from pandas import DataFrame,Series

#读取文件
datafile = u'E:\\pythondata\\tt.xlsx'#文件所在位置
data = pd.read_excel(datafile)#如果是csv文件则用read_csv
print("显示缺失值，缺失则显示为TRUE：\n", data.isnull())#是缺失值返回True，否则范围False
print("---------------------------------\n显示每一列中有多少个缺失值：\n",data.isnull().sum())#返回每列包含的缺失值的个数

#读取文件
datafile = u'E:\\pythondata\\ttt.xlsx'#文件所在位置
data = pd.read_excel(datafile)#如果是csv文件则用read_csv
print("显示源数据data：\n", data)#是缺失值返回True，否则范围False
print("------------------\n用均值插补后的数据data：\n", data.fillna(data.mean()))
"""
简单的缺失值插补方法：

data.fillna(data.mean()) #均值插补

data.fillna(data.median()) #中位数插补

data.fillna(data.mode()) #众数插补

data.fillna(data.max()) #最大值插补

data.fillna(data.min()) #最小值插补

data.fillna(0) #固定值插补--用0填充

data.fillna(5000) #固定值插补--用已知的行业基本工资填充

data.fillna（method='ffill'）#最近邻插补--用缺失值的前一个值填充

data.fillna（method='pad'） #最近邻插补--用缺失值的前一个值填充
"""

#读取文件
datafile = u'E:\\pythondata\\tt.xlsx'#文件所在位置，u为防止路径中有中文名称，此处没有，可以省略
data = pd.read_excel(datafile)#datafile是excel文件，所以用read_excel,如果是csv文件则用read_csv
examDf = DataFrame(data)

#去重
print(examDf.duplicated())#判断是否有重复行，重复的显示为TRUE，
examDf.drop_duplicates()#去掉重复行

#指定某列判断是否有重复值
print(examDf.duplicated('name'))#判断name列是否有重复行，重复的显示为TRUE，
examDf.drop_duplicates('name')#去掉重复行

#根据多列判断是否有重复值
print(examDf.duplicated(['name','sex','birthday']))#判断name,sex,birthday列是否有重复行，重复的显示为TRUE，
examDf.drop_duplicates(['name','sex','birthday'])#去掉重复行

inputfile = u'E:\\pythondata\\ttt.xlsx'

data= pd.read_excel(inputfile)

#将工资低于1000或者高于10万的异常值清空
data[u'工资'][(data[u'工资']<1000) | (data[u'工资']>100000)] = None

#清空后删除
print(data.dropna())

#将工资低于1000或者高于10万的异常值清空
data[u'工资'][(data[u'工资']<1000) | (data[u'工资']>100000)] = None

#清空后用均值插补
print(data.fillna(data.mean(5000)))