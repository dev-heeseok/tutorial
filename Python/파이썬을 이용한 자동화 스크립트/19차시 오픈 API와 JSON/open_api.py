import requests
import pprint

url = 'https://openapi.naver.com/v1/search/blog.json'
headers = {
    'X-Naver-Client-Id': 'zN2lLI8GYpDdLoVo7wxC',
    'X-Naver-Client-Secret': 'nHgbJL916N'
}
payload = {
    'query': '파이썬',
    'display': 20
}

res = requests.get(url, headers=headers, params=payload)
print(type(res))
pprint.pprint(res.json())
