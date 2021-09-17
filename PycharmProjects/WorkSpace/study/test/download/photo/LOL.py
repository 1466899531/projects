import os
import requests


class LOL(object):
    def __init__(self):
        self.base_path = "D:\\02-Test\\pythonProject\\SeleniumDemo\\demo\\file\\image\\"
        self.hero_list_url = "http://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js"
        self.hero_url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js"

    # 创建目录
    def create_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            pass

    def get_hero_list(self):
        response = requests.get(url=self.hero_list_url)
        res_json = response.json()
        hero_list = res_json.get("hero")
        for hero in hero_list[27:]:
            heroId = hero.get("heroId")
            self.get_hero(heroId)
            print("----------------------------------------------------------------------------------------------")

    def get_hero(self, heroId):
        response = requests.get(url=self.hero_url.format(heroId))
        json_data = response.json()
        # 英雄基本信息
        hero = json_data.get("hero")
        heroId = hero["heroId"]
        name = hero["name"]
        alias = hero["alias"]
        title = hero["title"]
        shortBio = hero["shortBio"]
        print(f"{heroId} - {name} - {alias} - {title} - {shortBio}")

        download_path = self.base_path + name
        self.create_folder(download_path)

        # 英雄皮肤信息
        skins = json_data.get("skins")
        for skin in skins:
            skin_name = skin["name"]
            skin_image = skin["mainImg"]
            description = skin["description"]
            if skin_image:
                print("\t", f"{skin_name} - {skin_image} - {description}")
                self.download_image(skin_image, download_path, skin_name)

    # 下载图片
    def download_image(self, url, path, filename):
        filename = filename.replace('/','')
        response = requests.get(url)
        file_path = f"{path}/{filename}.jpg"
        with open(file_path, mode='wb') as f:
            f.write(response.content)


if __name__ == '__main__':
    lol = LOL()
    lol.get_hero_list()