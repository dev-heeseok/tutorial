import pprint

from requests import Request
from requests import Session

url = 'https://openapi.naver.com/v1/papago/n2mt'
headers = {
    'X-Naver-Client-Id': 'zN2lLI8GYpDdLoVo7wxC',
    'X-Naver-Client-Secret': 'nHgbJL916N'
}

text = 'Yesterday all my troubles seemed so far away.'
parameters = {
    'source': 'en',
    'target': 'ko',
    'text':text
}

req = Request('POST', url, data=parameters, headers=headers)
prepped = req.prepare()

session = Session()
res = session.send(prepped)

pprint.pprint(res.json())
