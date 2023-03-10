import requests
from bs4 import BeautifulSoup


response = requests.get('https://news.ycombinator.com/newest')

soupObject = BeautifulSoup(response.text, 'html.parser')
links = soupObject.select('.titleline')
votes = soupObject.select('.score')


def create_custom_hackernews(links, votes):
    hackernews = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get('href', None)
        points = int(votes[index].getText().replace(' points', ''))
        hackernews.append({'title': title, 'link': href})
    return hackernews


print(create_custom_hackernews(links, votes))
