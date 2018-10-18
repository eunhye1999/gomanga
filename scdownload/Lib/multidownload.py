from threading import Thread
from urllib.request import urlopen
from queue import Queue
import time, re

class Multidownload:

  def __init__(self, links):
    self.links = links
    self.temp = []
    self.page = []
   
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
    
    for i in range(10):
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
    for j in range(0,len(page)):
      inde = page.index(str(j+1))
      dataSort.append(data[inde])
    return dataSort
    
