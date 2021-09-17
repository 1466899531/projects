#!/usr/bin/env python
# coding: utf-8

# # 爬虫获取二手房屋网页源码

# In[6]:

import pandas as pd
import requests
import time
import random
from bs4 import BeautifulSoup
page_texts=[]

# 获取网页
url='https://nanning.anjuke.com/sale/'
headers = {
    'cookie':'aQQ_ajkguid=5BC850FA-C29D-60C6-2AB3-41ACDEC92683; id58=e87rkGDMGc9An9wsBQlcAg==; _gid=GA1.2.1941305869.1623988685; _ga=GA1.2.1270274800.1623988685; wmda_new_uuid=1; wmda_uuid=3173deda4ff15943c4281dd44da7e045; wmda_visited_projects=;6289197098934; 58tj_uuid=6f70186c-8ce1-4a3d-8cc0-0cb604e17352; als=0; isp=true; ctid=62; ajk_member_verify=Q/yb519GDjayXqLAfzpNWGRqAuU8lxU/cP/vl6Qruls=; ajk_member_verify2=MjI0NzY3OTYxfDRmc2dFNlV8MQ==; twe=2; sessid=F04FAAC9-213A-A9B5-C9D6-CX0619083033; wmda_session_id_6289197098934=1624062633724-a2ff8a9a-ca93-887a; _gat=1; new_session=1; init_refer=https%3A%2F%2Fwww.baidu.com%2Fother.php%3Fsc.af0000jcQ8Bi5mi_Js-V9RM7f_93bgMGLzc27wh0cGrCUMcMaTRRdbOiJFduYrp8ctjsPgnhl3MA_Wj--858fhMX_ZvCWrfbHBZvvQcCW4oHB_Xl_Mqb2D81rqj-PyPttGPI_CO6O9kIPqMNl3__jNoSr9R8YCtD9hJHpce533cs6U91-ehcf5G08N6RwqB4uQmJKc7NIYw0ygS_M7RfnHY-zZFm.DY_NR2Ar5Od663rj6thm_8jViBjEWXkSUSwMEukmnSrZr1wC4eL_8C5RojPak3S5Zm0.TLFWgv-b5HDkrfK1ThPGujYknHb0THY0IAYq_Q2SYeOP0ZN1ugFxIZ-suHYs0A7bgLw4TARqnsKLULFb5UazEVrO1fKzmLmqnfKdThkxpyfqnHRzP1c4rjDvP0KVINqGujYkPjn1n1RvP6KVgv-b5HDsrHb4rj6z0AdYTAkxpyfqnHczP1n0TZuxpyfqn0KGuAnqiD4a0ZKGujY1nsKWpyfqPjn30APzm1Yznj03P6%26ck%3D6017.1.70.420.162.411.151.609%26dt%3D1624062630%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26tpl%3Dtpl_12273_25457_21675%26l%3D1527298164%26us%3DlinkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%252585%2525A8%2525E6%252588%2525BF%2525E6%2525BA%252590%2525E7%2525BD%252591%2525EF%2525BC%25258C%2525E6%252596%2525B0%2525E6%252588%2525BF%252520%2525E4%2525BA%25258C%2525E6%252589%25258B%2525E6%252588%2525BF%252520%2525E6%25258C%252591%2525E5%2525A5%2525BD%2525E6%252588%2525BF%2525E4%2525B8%25258A%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2525EF%2525BC%252581%2526linkType%253D; new_uv=5; obtain_by=1; ajkAuthTicket=TT=c995dafb851b58ee2d233098ea9e4888&TS=1624062664315&PBODY=D1ca64r6eA7PpA-DhbgY4NhRZttOY5BSKO2bYB5SB_zLQx44fp1mFEbLRsaqsuqaH1S3CAG3WIj_6k_Inlo00GQ0dntuU2Pi0A9zF18i2S3tgX6EOWoxhKZ_Up0fihvlKlh1qBrEMUW_oNyWZ6nfTzVY-HH8jtLKep5f-h0QJY0&VER=2; xxzl_cid=ca4f68b5a8ff4c14bc5d552b8062206b; xzuid=3e3c33e2-0594-4a79-a196-f3e22a1fee51',
    'Referer': url,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
#通过翻页爬取20张房屋信息网页，调用time.sleep()函数防止爬取过快给服务器造成负担
for i in range(1,21):
    if i==0:
        url=url
    else:
        url=url+'p'+str(i+1)+'/'
    page_text = requests.get(url,headers=headers).text
    page_texts.append(page_text)
    headers['Referer']=url
    time.sleep(random.randint(1,3))


# # 通过BeautifulSoup解析网页得到房价数据

# In[7]:


#  解析网页数据
titles,names,locations,types,areas,toprices,avprices,years=[],[],[],[],[],[],[],[]

for page_text in page_texts:
    soup = BeautifulSoup(page_text,'lxml')
    
    #title
    titles_bs=soup.find_all('h3',class_='property-content-title-name')
    for i in titles_bs:
        titles.append(i.text)
    #names
    names_bs=soup.find_all('p',class_='property-content-info-comm-name')
    for i in names_bs:
        names.append(i.text)
    #locations
    locations_bs=soup.find_all('p',class_='property-content-info-comm-address')
    for i in locations_bs:
        locations.append(i.text)
    #types
    types_bs=soup.find_all('p',class_='property-content-info-text property-content-info-attribute')
    for i in types_bs:
        types.append(i.text)
    #areas and years
    a='#__layout > div > section > section.list-main > section.list-left > section:nth-child(4) > div:nth-child('
    b=') > a > div.property-content > div.property-content-detail > section > div:nth-child(1) > p:nth-child(2)'
    c=') > a > div.property-content > div.property-content-detail > section > div:nth-child(1) > p:nth-child(5)'
    for i in range(60):
        selector1=a+str(i+1)+b
        selector2=a+str(i+1)+c
        areas_bs=soup.select(selector1)
        areas.append(areas_bs[0].text)
        years_bs=soup.select(selector2)
        years.append(years_bs[0].text)
    #toprices
    toprices_bs=soup.find_all('span',class_='property-price-total-num')
    for i in toprices_bs:
        toprices.append(i.text)
    #avprices
    avprices_bs=soup.find_all('p',class_='property-price-average')
    for i in avprices_bs:
        avprices.append(i.text)
        
df = pd.DataFrame({'标题':titles,'楼盘':names,'地址':locations,'户型':types,'面积':areas,'总价':toprices,'均价':avprices,'建造年份':years})


# # 房价数据

# In[9]:


df


# # 调取画图类库和模型类库

# In[13]:

import seaborn

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn import linear_model
import matplotlib.pyplot as plt

# # 进行数据清洗，将需要的数字数据类型从str型转为int或float型

# In[10]:


#数据清洗
for i in range(len(df['户型'])):
    df['均价'][i]=int(df['均价'][i][:-3])
    df['面积'][i]=float(df['面积'][i].replace(" ", "")[:-2])
    df['建造年份'][i]=int(df['建造年份'][i].replace(" ", "")[:-4])
    df['户型'][i]=int(df['户型'][i][0])+int(df['户型'][i][4])+int(df['户型'][i][8]) 
X=pd.DataFrame(df,columns=['面积','户型','建造年份'])
y=df['均价']


# # 查看清洗后的数据

# In[11]:


df


# # 四类图表

# In[14]:


#散点图
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus']=False
plt.scatter(df['面积'],y,color='green')
plt.title('aeras with aveprice ')


# In[15]:


#柱状图
df['建造年份'].value_counts().plot(kind='bar',title='build years ')


# In[17]:


#饼图
x_1=list(df['楼盘'].value_counts().index)[:5]
y_1=list(df['楼盘'].value_counts().values)[:5]
plt.pie(x=y_1,labels=x_1,autopct='%1.1f%%',shadow=False,startangle=150)


# In[63]:


#折线图
df['地址'].value_counts().plot()


# # 简单逻辑回归

# In[18]:


#数据归一化
scaler = MinMaxScaler()
X = scaler.fit_transform(X)
y = (y - y.min(axis=0)) / (y.max(axis=0) - y.min(axis=-0))
# 划分训练集、测试集
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=7)
#线性回归模型
reg = linear_model.LinearRegression()
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
loss = mean_squared_error(y_test, y_pred)
print("多元线性回归模型的均方误差为:",loss)


# In[ ]:




