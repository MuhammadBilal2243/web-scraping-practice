from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        return "sdf"
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscrping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)