import os
import time
from urllib import parse
from concurrent.futures import ThreadPoolExecutor, wait

import requests

# 创建了一个线程池（最多5个线程）
pool = ThreadPoolExecutor(5)

class DouYin(object):

    def __init__(self):
        # 默认请求头
        self.headers = {
            "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
        }
        # 获取用户个人信息接口
        self.user_info_url = "https://www.iesdouyin.com/web/api/v2/user/info/"
        # 获取用户作品接口
        self.video_list_url = "https://www.iesdouyin.com/web/api/v2/aweme/post/"
        # 获取用户喜欢作品列表
        self.like_list_url = "https://www.iesdouyin.com/web/api/v2/aweme/like/"
        # 获取用户挑战
        self.challenge_list_url = 'https://www.iesdouyin.com/web/api/v2/challenge/aweme/'
        # 签名
        self.sign = "mIrLFQAA-OUypYuVfKXa6ZiKyw"
        # 定义存储路径
        self.base_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\image\\videos\\"

    # 创建目录
    def create_folder(self):
        if not os.path.exists(self.base_path):
            os.makedirs(self.base_path)
        else:
            pass

    # 获取跳转链接
    def get_link(self, url):
        response = requests.get(url=url, headers=self.headers, allow_redirects=False)
        location = response.headers["location"]
        params = {
            "sec_uid": dict(parse.parse_qsl(parse.urlsplit(location).query))["sec_uid"]
        }
        self.get_user_info(params)

    # 获取用户信息
    def get_user_info(self, params):
        response = requests.get(url=self.user_info_url, params=params)
        response_data = response.json()
        user_info = response_data["user_info"]
        print("用户抖音号:", user_info["unique_id"])
        print("用户排名ID:", user_info["short_id"])
        print("用户昵称:", user_info["nickname"])
        print("用户签名:", user_info["signature"])
        print("用户获赞数:", user_info["total_favorited"])
        print("用户粉丝数:", user_info["follower_count"])
        print("用户作品数:", user_info["aweme_count"])
        self.base_path = self.base_path + user_info["unique_id"] + "/"
        self.create_folder()

        print("开始获取用户作品....")
        self.get_aweme_list(sec_uid=params["sec_uid"])

        # print("开始获取用户喜欢作品....")
        # self.get_like_aweme_list(sec_uid=params["sec_uid"])

        # print("开始获取用户挑战作品....")
        # self.get_challenge_aweme_list(ch_id=params["sec_uid"])

    # 获取用户作品列表
    def get_aweme_list(self, sec_uid, count=10, max_cursor=0, aid=1128, dytk=""):
        params = {
            "sec_uid": sec_uid,
            "count": count,
            "max_cursor": max_cursor,
            "aid": aid,
            "_signature": self.sign,
            "dytk": dytk,
        }
        response = requests.get(url=self.video_list_url, params=params)
        response_data = response.json()

        # 多线程调用下载函数
        tasks = [pool.submit(self.download_video, aweme) for aweme in response_data["aweme_list"]]
        wait(tasks)

        # 获取下一页链接
        next_page = response_data["max_cursor"]
        if next_page:
            # 获取下一页链接
            self.get_aweme_list(sec_uid=sec_uid, max_cursor=next_page)
        else:
            print("下载完成.....")

    # 获取用户喜欢作品列表(暂不支持)
    def get_like_aweme_list(self, sec_uid, count=10, max_cursor=0, aid=1128, dytk=""):
        params = {
            "sec_uid": sec_uid,
            "count": count,
            "max_cursor": max_cursor,
            "aid": aid,
            "_signature": self.sign,
            "dytk": dytk,
        }
        response = requests.get(url=self.like_list_url, params=params)
        response_data = response.json()
        if len(response_data["aweme_list"]) <= 0:
            print("当前用户没有喜欢的作品，或不能查看.....")
        else:
            # 多线程调用下载函数
            tasks = [pool.submit(self.download_video, aweme, type='/likes') for aweme in response_data["aweme_list"]]
            wait(tasks)

            # 获取下一页链接
            next_page = response_data["max_cursor"]
            if next_page:
                # 获取下一页链接
                self.get_aweme_list(sec_uid=sec_uid, max_cursor=next_page)
            else:
                print("下载完成.....")

    # 获取用户挑战作品列表
    def get_challenge_aweme_list(self, ch_id, count=10, cursor=0, aid=1128, screen_limit=3, download_click_limit=0):
        params = {
            "ch_id": ch_id,
            "count": count,
            "cursor": cursor,
            "aid": aid,
            "screen_limit": screen_limit,
            "download_click_limit": download_click_limit,
            "_signature": self.sign
        }
        response = requests.get(url=self.challenge_list_url, params=params)
        response_data = response.json()
        while response_data["has_more"]:
            for aweme in response_data["aweme_list"]:
                try:
                    print("作品ID: ", aweme["aweme_id"])
                    print("分组ID: ", aweme["group_id"])
                    print("作品简介: ", aweme["desc"])
                    print("作者昵称: ", aweme["author"]["nickname"])
                    print("作者签名: ", aweme["author"]["signature"])
                    print("音频链接: ", aweme["music"]["play_url"]["uri"])
                    print("视频链接: ", aweme["video"]["play_addr"]["url_list"][0])
                    print("\n")
                except:
                    pass
            cursor += count
            self.get_challenge_aweme_list(ch_id=ch_id, cursor=cursor)

    # 多线程下载视频
    def download_video(self, aweme):
        url = aweme["video"]["play_addr_lowbr"]["url_list"][0]
        video_name = aweme["aweme_id"]
        response = requests.get(url)
        file_path = self.base_path + str(video_name) + '.mp4'
        with open(file_path, mode='wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    url = input("请输入你要抓取的链接如: https://v.douyin.com/xxxxxxx/ \n : ")
    douyin = DouYin()
    douyin.get_link(url=url)