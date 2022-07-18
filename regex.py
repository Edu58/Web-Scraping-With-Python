from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def using_regex(url):
    """Regex to identify emails

    Args:
        url (string):
        e.g. [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)
    """
    html = urlopen(url)
    bs = BeautifulSoup(html, 'html.parser')

    images = bs.find_all('img', {'src':re.compile('\.\.\/img/gifts/img.*\.jpg')})

    for image in images:
        print(image['src'])

using_regex('http://www.pythonscraping.com/pages/page3.html')