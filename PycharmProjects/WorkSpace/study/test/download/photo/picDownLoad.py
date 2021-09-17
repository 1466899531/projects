import os
import time
import requests
from uuid import uuid4


class Konachan(object):
    def __init__(self):
        self.base_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\image\\"

    # 创建目录
    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    # 获取图片列表
    def get_images(self, number):
        url = "https://konachan.net/post.json?tags=holds%3Afalse%20%20limit%3A{}&api_version=2&filter=1&include_tags=1&include_votes=1&include_pools=1".format(
            number)
        try:
            self.create_folder(self.base_path)
            response = requests.get(url=url)
            json_data = response.json()
            data_list = json_data["posts"]
            for data in data_list:
                self.download_image(data["file_url"])
        except:
            pass

    # 下载图片
    def download_image(self, url):
        print("正在下载图片:", url)
        start = time.time()  # 下载开始时间
        # 拼接文件路径
        file_suffix = str(url).split('.')[3]
        file_name = str(uuid4()) + '.' + file_suffix
        file_path = self.base_path + file_name

        # 请求下载
        response = requests.get(url, timeout=10)
        print(response.status_code)

        with open(file_path, mode='wb') as f:
            f.write(response.content)

        end = time.time()  # 下载结束时间
        print('下载完成！耗时: %.2f秒' % (end - start))  # 输出下载用时时间


if __name__ == '__main__':
    print("开始获取图片")
    kc = Konachan()
    kc.get_images(2)