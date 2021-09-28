from bs4 import BeautifulSoup
from bs4 import SoupStrainer
def getUrls(html):
    urls = []
    soup = BeautifulSoup(html,"html.parser")
    js = [i.get('src') for i in soup.find_all('script') if i.get('src')]
    css = [i["href"] for i in soup.findAll("link", rel="stylesheet") if i["href"]]
    rest = [link["href"] for link in BeautifulSoup(html,"html.parser", parse_only=SoupStrainer('a')) if link.has_attr('href') and link["href"][0]!="#"]
    urls.extend(js)
    urls.extend(css)
    urls.extend(rest)

    return urls 