import requests
from bs4 import BeautifulSoup

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def businessDailyAfrica(url):
    bs = getPage(url)
    article_list = bs.find_all('h3', {'class': 'article-list-featured-title'})

    if article_list:
        for s in article_list:
            title = s.find('a')['title']
            article_url = s.find('a')['href']

            print(f'Title: {title}')
            print(f'url: https://www.businessdailyafrica.com{article_url}')
            print('-' * 100)

businessDailyAfrica('https://www.businessdailyafrica.com/')
