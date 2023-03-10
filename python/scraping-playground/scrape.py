import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/newest')

soupObject = BeautifulSoup(response.text, 'html.parser')
links = soupObject.select('.titleline')
votes = soupObject.select('.score')
