import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/newest')

soupObject = BeautifulSoup(response.text, 'html.parser')
print(soupObject.find('a'))
