import requests
from bs4 import BeautifulSoup

url = 'https://www.profesia.sk/en/work/?search_anywhere=python'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find_all('span', class_='title')

for row in results:
    print(row.text)

