import requests
url = 'https://api.pwnedpasswords.com/range/' + 'BAB12'
res = requests.get(url)
print(res)
