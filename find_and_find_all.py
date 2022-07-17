from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def get_bold_text(url):
    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, 'html.parser')
    except HTTPError as e:
        print('PAGE NOT FOUND')
    except URLError as e:
        print('URL NOT FOUND')
    else:
        nameList = bs.find_all('span', {'class': 'pre'})
        for name in nameList:
            print(name.get_text())

get_bold_text('https://docs.python.org/3/library/urllib.request.html#module-urllib.request')