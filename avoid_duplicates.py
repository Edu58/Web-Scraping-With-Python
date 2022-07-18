from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


pages = set()

def getLinks(pageUrl):
    """_summary_
        Avoid cawling duplicate urls while traversing a domain
    Args:
        pageUrl (string): _description_
        To avoid crawling the same page twice, it is extremely important that all internal links
        discovered are formatted consistently, and kept in a running set for easy lookups,
        while the program is running. A set is similar to a list, but elements do not have a
        specific order, and only unique elements will be stored, which is ideal for our needs.
        Only links that are “new” should be crawled and searched for additional links
    """
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')