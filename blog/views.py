from django.shortcuts import render,HttpResponse,redirect
from blog import models
from django.utils.safestring import mark_safe
# Create your views here.

def index(request):
    article_list = models.Article.objects.all().order_by("-id")
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()
    top = models.Article.objects.filter(top=True)
    tags = models.Tag.objects.all()
    profile = models.Profile.objects.all().first()
    words = models.Words.objects.all()

    res = {'a_list':article_list,
            'author':author,
            'footer':footer,
            'top':top,
            'tags':tags,
            'words':words,
            'profile':profile}

    return render(request,'index.html',res)


def article(request):
    article_list = models.Article.objects.all().order_by("-id")
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'article.html', {'a_list': article_list,'author':author,'footer':footer})

def dream(request):
    dream_list = models.Dream.objects.all().order_by("-id")
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'dream.html', {'d_list': dream_list,'author':author,'footer':footer})

def tojun(request):
    mood_list = models.Jun.objects.all().order_by("-id")
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'tojun.html', {'m_list': mood_list,'author':author,'footer':footer})

def article_content(request):

    aid = request.GET.get('aid')
    article = models.Article.objects.filter(id=aid).first()
    temp = article.content#获取文章内容
    content = temp.replace(" ","&nbsp;").replace("\r","<br/>")#对文本内容进行处理，使符合html的规则。
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()
    profile = models.Profile.objects.all().first()


    return render(request, 'article_content.html', {'article':article,'content':content,'author':author,'footer':footer,'profile':profile})

