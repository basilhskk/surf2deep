import requests
from helpers import system


class surf2deep:
    def __init__(self):

        # check if tor is running 
        if system.isServiceStatus("tor",system.findSystem()):

            # init requests session with tor proxy
            self.session = requests.Session()
            self.session.proxies = {'http':  'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}
            
            #create tmp dir
            self.location = ""

            