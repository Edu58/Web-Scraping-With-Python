from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


def get_bold_text(url):

    """_summary_

    find_all(tag, attributes, recursive, text, limit, keywords)
    find(tag, attributes, recursive, text, keywords)

    The recursive argument is a boolean. How deeply into the document do you want to
    go? If recursive is set to True , the find_all function looks into children, 
    and children’s children, for tags that match your parameters. If it is False , it will look only at
    the top-level tags in your document. By default, find_all works recursively ( recursive is set to True )

    The text argument matches based on the text content of the tags, rather than properties of the tags themselves
    
    The limit argument might be set this if you’re interested only in retrieving the first x items from the page
    
    The keyword argument allows you to select tags that contain a particular attribute or set of attributes
    """

    try:
        html = urlopen(url)
        bs = BeautifulSoup(html, "html.parser")
    except HTTPError as e:
        print("PAGE NOT FOUND")
    except URLError as e:
        print("URL NOT FOUND")
    else:
        # Also Valid: .find_all(['h1','h2','h3','h4','h5','h6'])
        # Also Valid: .find_all('span', {'class':{'green', 'red'}}) -> return both the green and red span tags in the HTML document
        nameList = bs.find_all("span", {"class": "pre"})
        for name in nameList:
            #.get_text() strips all tags and returns a Unicode string containing the text only.
            print(name.get_text())


get_bold_text(
    "https://docs.python.org/3/library/urllib.request.html#module-urllib.request"
)
