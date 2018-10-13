from threading import Thread
from urllib.request import urlopen
from queue import Queue
import time, re

class Multidownload:
  
  temp = []
  page = []

  def __init__(self, links):
    self.links = links
   
  def read_url(self,url):
    try:
        pattern = r"(?P<link>.+) p-(?P<page>.+)"
        result = re.match(pattern, url)
        data = urlopen(result['link']).read()
        self.temp.append(data)
        self.page.append(result['page'])
    except:
        print(f"ERRPR {url}")
   
  def worker(self):
    while True:
      item = self.q.get()
      self.read_url(item)
      self.q.task_done()
   
  def process(self):
    self.q = Queue()
    
    for i in range(len(self.links)):
      t = Thread(target=self.worker)
      t.daemon = True
      t.start()

    for item in self.links:
      self.q.put(item)

    self.q.join() 
    
  def getData(self):
    return self.__sortData(self.temp, self.page)
  
  def __sortData(self, data, page):
    dataSort = []
    for i in range(0,len(data)):
      inde = page.index(str(i+1))
      dataSort.append(data[inde])
      
    return dataSort
    
