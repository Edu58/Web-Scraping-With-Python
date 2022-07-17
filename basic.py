from urllib.request import urlopen

html = urlopen("https://moringaschool.instructure.com/courses/648/pages/monday-introduction?module_item_id=58804")
print(html.read())