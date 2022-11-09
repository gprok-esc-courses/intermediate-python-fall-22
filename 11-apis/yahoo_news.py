import requests
from xml.etree.ElementTree import fromstring
# INSTALL pip install elementpath

rss_feed = requests.get('https://www.yahoo.com/news/rss/world')

content = rss_feed.content

root = fromstring(content)

for news_item in root.iter('item'):
    title = news_item.find('title')
    print(title.text)
