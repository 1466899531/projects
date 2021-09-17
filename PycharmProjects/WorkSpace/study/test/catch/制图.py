import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 0、导入数据集
df = pd.read_excel('first.xlsx', 'Sheet1')
# 直方图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(df['Age'], bins=7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('Employee')
plt.show()

# 5、折线图
var = df.groupby('BMI').Sales.sum()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('BMI')
ax.set_ylabel('Sum of Sales')
ax.set_title('BMI wise Sum of Sales')
var.plot(kind='line')
plt.show()

# 条形图

var = df.groupby('Gender').Sales.sum()
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_xlabel('Gender')
ax1.set_ylabel('Sum of Sales')
ax1.set_title('Gender wise Sum of Sales')
var.plot(kind='bar')
plt.show()

# 9、饼图
var = df.groupby(['Gender']).sum().stack()
temp = var.unstack()
type(temp)
x_list = temp['Sales']
label_list = temp.index
plt.axis('equal')
plt.pie(x_list, labels=label_list, autopct='%1.1f%%')
plt.title('expense')
plt.show()