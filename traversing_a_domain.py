from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

def traverse_kevin_bacon_wikipedia(url):
    """_summary_
        Six Degrees of Kevin Bacon
    Args:
        url (string): _description_
        Even if you haven’t heard of Six Degrees of Wikipedia, you’ve almost certainly heard
        of its namesake, Six Degrees of Kevin Bacon. In both games, the goal is to link two
        unlikely subjects (in the first case, Wikipedia articles that link to each other, and in
        the second case, actors appearing in the same film) by a chain containing no more
        than six total (including the two original subjects).
    """

    html = urlopen(f'http://en.wikipedia.org{url}')
    bs = BeautifulSoup(html, 'html.parser')

    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

links = traverse_kevin_bacon_wikipedia('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = traverse_kevin_bacon_wikipedia(newArticle)