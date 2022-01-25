import requests
import json

def getlocation(url):
    domain = 'http://ip-api.com/json/' + url
    req = requests.get(domain)
    dic = json.loads(req.text)

    return dic

url = input('input :')
dic = getlocation(url)
for i in dic.keys():
    print(i, ' : ', dic[i])
