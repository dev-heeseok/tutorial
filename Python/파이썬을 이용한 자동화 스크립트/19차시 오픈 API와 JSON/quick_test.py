import requests
import pprint

res = requests.get('https://openapi.naver.com/v1/papago/n2mt')
print(type(res))
# pprint.pprint(res.text)
pprint.pprint(res.json())