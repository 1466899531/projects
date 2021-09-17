import os
import time
import requests
from bs4 import BeautifulSoup

class DouTu(object):
    def __init__(self):
        self.base_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\image\\"
        self.base_url = "https://www.doutula.com"
        self.headers = {
            "Cookie": "_agep=1617332993; _agfp=394e543fd58b15645b20d85328c7c13a; _agtk=ea484a0f61d912d369bd5765299b9702; Hm_lvt_2fc12699c699441729d4b335ce117f40=1617332992,1618563143; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1618563729",
            "Host": "www.doutula.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        }
        self.create_folder(self.base_path)

    # 创建目录
    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    # 设置cookies
    def set_cookie(self):
        response = requests.get(url=self.base_url, headers=self.headers)
        cookie_list = []
        for key, value in response.cookies.items():
            cookie_list.append(key + "=" + value)
        self.headers["Cookie"] = '; '.join(cookie_list)

    # 生成链接列表
    def get_app_url_list(self, number):
        for i in range(1, number):
            yield f"https://www.doutula.com/photo/list/?page={i}"

    # 获取图片列表
    def get_images(self, url):
        try:
            response = requests.get(url=url, headers=self.headers)
            print(response.status_code)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'lxml')
                a_list = soup.select(".list-group-item > div > div > a")
                for a in a_list:
                    img = a.select('img')[-1]
                    self.download_image(img.attrs["data-backup"])
            else:
                time.sleep(60)
                self.set_cookie()
                self.get_images(url)
        except Exception as e:
            time.sleep(60)
            self.set_cookie()
            self.get_images(url)

    # 下载图片
    def download_image(self, url):
        print("正在下载图片:", url)
        start = time.time()  # 下载开始时间
        file_path = self.base_path + str(url).split('/')[-1]
        response = requests.get(url, timeout=10)
        with open(file_path, mode='wb') as f:
            f.write(response.content)
        end = time.time()  # 下载结束时间
        print('下载完成！耗时: %.2f秒' % (end - start))  # 输出下载用时时间


if __name__ == '__main__':
    dt = DouTu()
    number = int(input("请输入爬取的页数: "))
    url_list = dt.get_app_url_list(number)
    for url in url_list:
        dt.get_images(url)