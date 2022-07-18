from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()

def getLinks(pageUrl):

    """_summary_
        How to collect specific data across an entire website
    Args:
        getLinks (string): _description_

        Web crawlers would be fairly boring if all they did was hop from one page to the
        other. To make them useful, you need to be able to do something on the page while
        you’re there. Let’s look at how to build a scraper that collects the title, the first para‐
        graph of content, and the link to edit the page (if available).
    """

    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0])
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')

    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')