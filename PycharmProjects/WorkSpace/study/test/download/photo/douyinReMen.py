import requests


class DouYin(object):
    def __init__(self):
        # 热门搜索
        self.HOT_SEARCH_URL = 'https://aweme.snssdk.com/aweme/v1/hot/search/list/'
        # 热门明星
        self.HOT_STAR_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/star/billboard/'
        # 热门
        self.HOT_LIVE_URL = 'https://webcast.amemv.com/webcast/ranklist/hot/'

        self.BRAND_CATEGORY_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/category/'

        self.HOT_BRAND_URL = 'https://aweme.snssdk.com/aweme/v1/hotsearch/brand/billboard/'

        self.HOT_MUSIC_URL = 'https://aweme.snssdk.com/aweme/v1/chart/music/list/'

        self.HEADERS = {
            'user-agent': 'okhttp3'
        }

        self.QUERIES = {
            'device_platform': 'android',
            'version_name': '13.2.0',
            'version_code': '130200',
            'aid': '1128'
        }

    def get_hot_search(self):
        """
        热点
        """
        response = requests.get(self.HOT_SEARCH_URL, params=self.QUERIES)
        response_data = response.json()
        items = [item for item in response_data["data"]["word_list"]]
        return items

    def get_hot_star(self):
        """
        明星
        """
        response = requests.get(self.HOT_STAR_URL, params=self.QUERIES)
        response_data = response.json()
        items = [item for item in response_data["user_list"]]
        return items

    def get_hot_live(self):
        """
        直播
        """
        response = requests.get(self.HOT_LIVE_URL, params=self.QUERIES)
        response_data = response.json()
        items = [item for item in response_data["data"]["ranks"]]
        return items

    def get_brand_category(self):
        """
        品牌分类
        """
        response = requests.get(self.BRAND_CATEGORY_URL, params=self.QUERIES)
        response_data = response.json()
        items = [item for item in response_data["category_list"]]
        return items

    def get_hot_brand(self, category: int):
        """
        品牌榜
        """
        params = self.QUERIES.copy()
        params.update({'category_id': str(category)})
        response = requests.get(self.HOT_BRAND_URL, params=params)
        response_data = response.json()
        items = [item for item in response_data["brand_list"]]
        return items

    def get_hot_music(self):
        """
        音乐
        """
        params = self.QUERIES.copy()
        params.update({'chart_id': '6853972723954146568', 'count': '100'})
        response = requests.get(self.HOT_MUSIC_URL, params=params)
        response_data = response.json()
        items = [item for item in response_data["music_list"]]
        return items


def run():
    douyin = DouYin()

    # # 调用热点函数
    # items = douyin.get_hot_search()
    # for item in items:
    #     print(item)


    # # 获取热点明星
    # items = douyin.get_hot_star()
    # for item in items:
    #     print(item)


    # # 获取热点直播
    # items = douyin.get_hot_live()
    # for item in items:
    #     print(item)


    # # 获取热点分类
    # items = douyin.get_brand_category()
    # for item in items:
    #     print(item)


    # # 获取热点品牌榜
    # items = douyin.get_hot_brand(1)
    # for item in items:
    #     print(item)

    # 获取热点音乐
    items = douyin.get_hot_music()
    for item in items:
        print("歌曲ID: ", item["music_info"]["id"])
        print("歌曲名称: ", item["music_info"]["title"])
        print("歌曲作者: ", item["music_info"]["author"])
        print("歌曲链接: ", item["music_info"]["play_url"]["uri"])
        print('\n')

if __name__ == '__main__':
    run()