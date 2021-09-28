import requests
from helpers import system as sysHelper
from helpers import  request as requestHelper

class surf2deep:
    def __init__(self):

        # check if tor is running 
        if sysHelper.isServiceStatus("tor",sysHelper.findSystem()):

            # init requests session with tor proxy
            self.session = requests.Session()
            self.session.proxies = {'http':  'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}
            
            #create tmp dir
            self.tmpDir = sysHelper.createTempDir(sysHelper.getTempDir())


    def newSession(self):
        """
        Create a new session
        """
        self.session = requests.Session()


    def get(self,url:str,view=False)->requests.Response:
        """
        Perform a GET request to the onion site
        """
        if requestHelper.getTld(url)!= "onion":
            return self.session.get(url)
        else:
            request = self.session.get(url)
            # print(get_request.content)
            content_type = request.headers["Content-Type"]
            if requestHelper.getMimeType(request) == "text/html":
                dlFiles,dlFilePaths = requestHelper.getdlFileList(request)
                
                # for file in dlFiles:
                #     # dlfile = self.session.get(file)
                #     foldername = "/".join(file.split("://")[1].split("/")[:-1])
                #     filename = file.split("://")[1].split("/")[-1]
                #     if len(filename.split("?"))>1:
                #         filename = filename.split("?")[0]
                #     r = self.session.get(file)
                #     foldername = sysHelper.createFoldersFromPath(self.tmpDir,foldername)
                #     fname =sysHelper.joinPaths(foldername,filename) 
                #     if not sysHelper.fileExists(fname):
                #         with open(fname,"a")as writeFile:
                #             writeFile.write(r.text)
                
                pg_content = request.text
                # for url in dlFilePaths:
                #     tmpPath = sysHelper.joinPaths(self.tmpDir,request.url.split("://")[1])

                #     pg_content =  pg_content.replace(url,sysHelper.joinPaths(tmpPath, url[1:]))

                return pg_content