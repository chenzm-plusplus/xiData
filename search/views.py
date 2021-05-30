from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from . import search
import time

# Create your views here.

def search_page(request):
    return render(request, 'search.html')

def search_form(request):
    return render_to_response('searchform.html')

def searching(request):
    t0=time.clock()
    request.encoding = 'utf-8'
    filelist=[]
    if 'q' in request.GET:
        m_message = request.GET['q']
        templist=search.searchintext(request.GET['q'])
        for filename in templist:
            if filename=='NoFound':
                return HttpResponse("No result!")
            f = open(filename, 'r')
            t = f.readline()
            keyword = f.readline()
            t = f.readline()
            title = f.readline()
            t = f.readline()
            head = f.readline()
            d={
                'id':filename[0:-4],
                'filename':filename,
                'keyword':keyword,
                'head':head
            }
            filelist.append(d)
        t1=time.clock()
        return render(request, 'infolist.html', {'filelist': filelist, 'searchtext':m_message,'time':t1-t0})
    else:
        content = '你提交了空表单'
        return HttpResponse(content)


def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'search_post.html', ctx)


def infolist(request):
    filelist = []
    for i in range(4076):
        filename=str(i)+'.txt'
        f=open(filename,'r')
        t=f.readline()
        keyword=f.readline()
        t=f.readline()
        title=f.readline()
        t = f.readline()
        head = f.readline()
        d={'id':str(i),
           'filename': str(i)+'.txt',
           'keyword':keyword,
           'head':head
           }
        filelist.append(d)
    return render(request,'infolist.html',{'filelist':filelist})


def info(request,fileid):
    f=open(fileid+".txt",'r')
    text=f.read()
    content=[
        {'text':text}
    ]
    return render(request, 'info.html', {'content':content})
