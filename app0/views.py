import queue
from django.shortcuts import render
from app0.models import *
from django.db.models import Q

# Create your views here.

def display_topic(request):
    QSTO=Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)






def display_webpage(request):
    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.all().order_by('name')
    QSWO=Webpage.objects.all().order_by('-name')
    QSWO=Webpage.objects.all().exclude(topic_name='cricket')

    QSWO=Webpage.objects.all()
    QSWO=Webpage.objects.filter(name__startswith='v')
    QSWO=Webpage.objects.filter(name__endswith='t')
    QSWO=Webpage.objects.filter(url__endswith='com')
    QSWO=Webpage.objects.filter(topic_name='cricket')
    QSWO=Webpage.objects.filter(Q(url__endswith='com') & Q(name__startswith='v'))
    QSWO=Webpage.objects.all()
    
    d= {'QSWO':QSWO}
    return render(request,'display_webpages.html',d)




def update_webpage(request):
    

   # Webpage.objects.filter(name='virat').update(url='https.cricket.in')
   # Webpage.objects.filter(topic_name='cricket').update(url='https.cric.in')
   # Webpage.objects.filter(name='virat').update(topic_name='rubby')
   # Webpage.objects.filter(name='dhyanchand').update(topic_name='cricket')

   #----updating using upadte or create ----

    CTO=Topic.objects.get(topic_name='football')
    #Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'fakarzaman'})
    #Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'tinku'})
    Webpage.objects.update_or_create(topic_name=CTO,defaults={'name':'pokiri','url':'http.vitu.com'})



    QSWO=Webpage.objects.all()
    d= {'QSWO':QSWO}
    return render(request,'display_webpages.html',d)
    








def display_accessrecord(request):
    QSACR=AccessRecord.objects.all()

    QSACR=AccessRecord.objects.filter(date__year='2001')



    d= {'QSACR':QSACR}
    return render(request,'display_ar.html',d)






def insert_topic(request):
    to=input('enter topic_name: ')
    TO=Topic.objects.get_or_create(topic_name=to)[0]
    TO.save()
    QSTO=Topic.objects.all()
    d = {'QSTO':QSTO}
    return render(request,'display_topic.html',d)




def insert_webpage(request):
    tn=input('enter TOPIC NAME')
    na=input('enter name')
    ur=input('enter url')

    TO=Topic.objects.get(topic_name=tn)

    WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur)[0]

    QSWO=Webpage.objects.all()
    d= {'QSWO':QSWO}
    return render(request,'display_webpages.html',d)



def insert_accessrecord(request):
    pk=input('enter pk value: ')
    da=input('enter the date: ')
    au=input('enter author name: ')
    em=input('enter email: ')
    wo=Webpage.objects.get(pk=pk)
    ao=AccessRecord.objects.get_or_create(name=wo,date=da,author=au,email=em)[0]
    ao.save()
    QSACR=AccessRecord.objects.all()
    d= {'QSACR':QSACR}
    return render(request,'display_ar.html',d)










