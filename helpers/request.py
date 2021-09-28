from tld import get_tld
from helpers import parser
from urllib.parse import urlparse,urljoin
import os


def getTld(url:str)->str:
    try:
        return get_tld(url)
    except:
        raise ValueError("Not a valid url")


def getMimeType(request):
    content_type = request.headers['Content-Type']
    content_type = content_type.split(";")
    if len(content_type)>1:
        charset = content_type[1]
    content_type = content_type[0].strip()

    return content_type 


def getdlFileList(request)->list:
    urls = parser.getUrls(request.text)
    fileurls = []
    fileurlpaths=[]
    for url in urls:
        path = urlparse(url).path
        ext = os.path.splitext(path)[1].strip() 
        if ext.replace(".","") in ["js","css","png","jpeg","jpg","svg"]:
            if request.url not in url and url[0] =="/":
                fileurls.append(urljoin(request.url,url))
                fileurlpaths.append(url)
    #keep unique
    fileurls = list(set(fileurls))
    
    return fileurls,fileurlpaths