from django.shortcuts import render
from app.models import *

# Create your views here.

def topicinsert(request):
    if request.method=='POST':
        topicname=request.POST['topic_name']
        TO=Topic.objects.get_or_create(topic_name=topicname)[0]
        TO.save()
    return render(request,'topicinsert.html')

def webpageinsert(request):
    LTO=Topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        topic=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']

        TO=Topic.obejcts.get(topic_name=topic)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
        WO.save()

    return render(request,'webpageinsert.html',d)

def accessinsert(request):
    LOW=Webpage.obejcts.all()
    d={'webpage':LOW}
    if request.method=='POST':
        name=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']

        WO=Webpage.objects.get(name=name)

        ARO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]

        ARO.save()

    return render(request,'accessinsert.html',d)

def retrievedata(request):
    LOW=Webpage.objects.all()
    d={'webpages':LOW}
    if request.method=='POST':
        wd=request.POST.getliist('name')
        print(wd)
        webqueryset=Webpage.objects.none()
        for i in wd:
            webqueryset=webqueryset|Webpage.objects.filter
            (name=i)
        d1={'webpages':webqueryset}
        return render(request,'displaywebpage.html',d1)

    return render(request,'retrievedata.html',d)
    
