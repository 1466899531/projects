# 导入爬虫的库，不然调用不了爬虫的函数
import requests


# get方法访问
response_GET = requests.get("http://www.baidu.com")
# 设置编码格式
response_GET.encoding = response_GET.apparent_encoding # 解决中文乱码问题
# 打印状态码
print("状态码:"+ str(response_GET.status_code))
# 输出爬取的信息
print(response_GET.text)
print("===================get==========================")
# get传参需要传多个参数只需要用&符号连接即可如下
response_GetWithURLParam = requests.get("http://httpbin.org/get?name=hezhi&age=20")
# Response对象包含request请求，通过r.request.headers查看我们发的request请求的头部是什么内容。
print(response_GetWithURLParam.request.headers)
print(response_GetWithURLParam.status_code)
print(response_GetWithURLParam.text)
print("===================get URL传参============================")

data = {
    "name":"hezhi",
    "age":20
}
response_GetWithDataParam = requests.get("http://httpbin.org/get", params=data)
print(response_GetWithDataParam.status_code)
print(response_GetWithDataParam.text)
print("===================get params传参============================")

# post方法访问
response_POST = requests.post("http://httpbin.org/post")
print(response_POST.status_code)
print(response_POST.text)
print("=====================post (传参和get的params传参一样 , 有可能 params需要改为json)=========================")
# put方法访问
response_PUT = requests.put("http://httpbin.org/put")
print(response_PUT.status_code)
print(response_PUT.text)
print("======================put===========================")

# 绕过反爬机制 . 第一次访问知乎，不设置头部信息
response_ZhiHu = requests.get( "http://www.zhihu.com")  #
print("状态码: "+str(response_ZhiHu.status_code)+"--- 响应内容: "+response_ZhiHu.text)
print("======================开始绕反爬机制===========================")

# 下面是可以正常爬取的区别，更改了User-Agent字段 设置头部信息,伪装浏览器
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
}
# get方法访问,传入headers参数，
response_Headers = requests.get( "http://www.zhihu.com", headers=headers)
print(response_Headers.status_code)
print(response_Headers.text)
print("======================开始爬取一个html并保存===========================")
# 爬取一个html并保存
url = "http://www.baidu.com"
response_Save = requests.get(url)
response_Save.encoding = "utf-8"
print("\n的类型" + str(type(response_Save)))
print("\n状态码是:" + str(response_Save.status_code))
print("\n头部信息:" + str(response_Save.headers))
print("\n响应内容:"+response_Save.text)
# 保存文件,打开一个文件，w是文件不存在则新建一个文件，这里不用wb是因为不用保存成二进制
file = open("D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\catchFile\\baidu.html","w",encoding="utf-8")
file.write(response_Save.text)
file.close()
print("======================开始爬取一个html并保存===========================")
response_Pic = requests.get("https://www.baidu.com/img/baidu_jgylogo3.gif")  # get方法的到图片响应
file_Pic = open("D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\catchFile\\baidu_logo.gif","wb") # 打开一个文件,wb表示以二进制格式打开一个文件只用于写入
# 写入文件  content是bytes
file_Pic.write(response_Pic.content)
# 关闭操作，运行完毕后去你的目录看一眼有没有保存成功
file_Pic.close()

