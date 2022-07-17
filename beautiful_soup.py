from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://moringaschool.instructure.com/courses/648/pages/monday-introduction?module_item_id=58804")

bs = BeautifulSoup(html.read(), 'html.parser')

print(bs)