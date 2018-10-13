from urllib.request import Request, urlopen
import sys
from bs4 import BeautifulSoup
import ssl

class Nhentai:
    data = []
    dataDic = {}
    status = True
    def __init__(self, url):
        self.url = url
        self.setUp(url)
    ### SETUP HTTP REQUEST ####
    def setUp(self, url):
        try:
            ssl._create_default_https_context = ssl._create_unverified_context
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            html = urlopen(req).read()
            self.soup = BeautifulSoup(html)
            self.status = True
        except:
            self.status = False
    
    def getLinkSplit(self, string):
        string = string.split('/')
        last = len(string)
        laststr = string[last-1].replace("t", "")
        if(laststr=='cover.jpg' or laststr=='humb.jpg'):
            return None
        return 'https://i.nhentai.net/{}/{}/{}'.format(string[last-3], string[last-2], laststr)
        
    #### CHECK DOMAIN ####
    def genTagIMG(self, pageAll=0, name =''): 
        self.data = []
        for link in self.soup.find_all('img'):
            # print(link)
            string = link.get('data-src')
            if(string != None):
                linkImg = self.getLinkSplit(string)
                if(linkImg != None):
                    self.data.append(linkImg)

    def getData(self):
        return self.data

