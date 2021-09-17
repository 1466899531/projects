import requests

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080',
}

response = requests.get('https://foofish.net', proxies=proxies, timeout=5)
print(response.text)


for x, y in [(1, 1), (2, 4), (3, 9)]:
  print(x,y)
