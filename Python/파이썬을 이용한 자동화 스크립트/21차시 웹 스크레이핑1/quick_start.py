from bs4 import BeautifulSoup
import requests

res = requests.get('https://book.naver.com')
print(type(res))

soup = BeautifulSoup(res.text, 'lxml')
print(soup)

div_tag = soup.div
print(type(div_tag))

print(div_tag)
