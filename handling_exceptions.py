from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

try:
    html = urlopen("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")
    bs = BeautifulSoup(html, 'html.parser')

    title = bs.body.h1

except AttributeError as e:
    pass
except HTTPError as e:
    print('PAGE NOT FOUND')
except URLError as e:
    print('URL NOT FOUND')
else:
    if title == None:
        print('TITLE NOT FOUND')
    else:
        print(title)