from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import History

from .Lib.nhentaiScript import Nhentai
from .Lib.multidownload import Multidownload

from zipfile import ZipFile
from urllib.request import urlopen
from io import StringIO, BytesIO
from multiprocessing import Queue
import threading

def index(request):
    list_site = ["nhentai"]
    return render(request, 'scdownload/index.html', {"list_site":list_site})

def nhentai(request):
    return render(request, 'scdownload/nhentai.html')

def nhentaiResult(request):
    if request.method == 'POST' and request.POST['link'] != '':
        url = request.POST['link']
        obj = Nhentai(url)
        print(obj.status)
        if obj.status == True:
            obj.genTagIMG()
            link_ary = obj.getData()
            return render(request, 'scdownload/result_nhentai.html', {"links":link_ary,"url":url})
        else:
            return redirect('scdownload:index')
    else:
        return redirect('scdownload:index')

def getLinks(req):
    if(req.POST['filename'] == ""):
        file_name = "noName"
    else:
        file_name = req.POST['filename']
    text = req.POST['site']
    links = text[1:-1].split(',')
    linkR = []
    for i in range(0,len(links)):
        linkR.append((links[i].replace(" ", "")[1:-1])+f" p-{i+1}")

    return linkR, file_name

def downloadIMG(request):
    if request.method == 'POST':
        links, name = getLinks(request)
        obj = Multidownload(links)
        obj.process()
        data = obj.getData()
        in_memory = BytesIO()
        zip = ZipFile(in_memory, 'w')
        for i in range(0,len(data)):
            zip.writestr(f'{i+1}.jpg', data[i])
            
        zip.close()

    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = f"attachment; filename={name}.zip"
    in_memory.seek(0)

    response.write(in_memory.read())
    return response
