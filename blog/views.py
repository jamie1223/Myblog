from django.shortcuts import render,HttpResponse,redirect
from blog import models
from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    article_list = models.Article.objects.all()

    return render(request,'index.html',{'a_list':article_list})

def test(request):
    if request.method == 'GET':
        article_list = models.Article.objects.all()
        print(article_list)
        return render(request, 'test.html', {'a_list':article_list})

def article(request):
    article_list = models.Article.objects.all()

    return render(request, 'article.html', {'a_list': article_list})

def dream(request):
    article_list = models.Article.objects.all()

    return render(request, 'dream.html', {'a_list': article_list})

def tojun(request):
    mood_list = models.Jun.objects.all()

    return render(request, 'tojun.html', {'m_list': mood_list})

def article_content(request):

    aid = request.GET.get('aid')
    article = models.Article.objects.filter(id=aid).first()
    temp = article.content

    content = temp.replace(" ","&nbsp;").replace("\r","<br/>")

    return render(request, 'article_content.html', {'article':article,'content':content})

