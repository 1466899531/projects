import os
import time
import aiohttp
import asyncio
from uuid import uuid4


class Konachan(object):
    def __init__(self):
        self.base_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\image\\"

    # 创建目录
    async def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    # 获取图片列表
    async def get_images(self, number):
        url = "https://konachan.net/post.json?tags=holds%3Afalse%20%20limit%3A{}&api_version=2&filter=1&include_tags=1&include_votes=1&include_pools=1".format(
            number)
        try:
            await self.create_folder(self.base_path)
            # 异步请求
            async with aiohttp.ClientSession() as session:
                async with session.get(url, verify_ssl=False) as response:
                    json_data = await response.json()
                    data_list = json_data["posts"]

                    tasks = [asyncio.create_task(self.download_image(session, data["file_url"])) for data in data_list]
                    await asyncio.wait(tasks)
        except:
            pass

    # 下载图片
    async def download_image(self, session, url):
        print("正在下载图片:", url)
        # 拼接文件路径
        file_suffix = str(url).split('.')[-1]
        file_name = str(uuid4()) + '.' + file_suffix
        file_path = self.base_path + file_name

        # 请求下载
        async with session.get(url, verify_ssl=False) as response:
            content = await response.content.read()
            with open(file_path, mode='wb') as file_object:
                file_object.write(content)


if __name__ == '__main__':
    start = time.time()  # 下载开始时间

    print("开始获取图片")
    kc = Konachan()
    asyncio.run(kc.get_images(5))

    end = time.time()  # 下载结束时间
    print('下载完成！耗时: %.2f秒' % (end - start))  # 输出下载用时时间