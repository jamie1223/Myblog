from django.shortcuts import render,HttpResponse,redirect
from blog import models
from django.utils.safestring import mark_safe
from django import forms
from django.forms import widgets
from django.forms import fields
# Create your views here.

def index(request):#主页函数
    article_list = models.Article.objects.all().order_by("-id")#这里进行一下排序
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


def article(request):#文章函数
    article_list = models.Article.objects.all().order_by("-id")#这里进行一下排序
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'article.html', {'a_list': article_list,'author':author,'footer':footer})

def dream(request):#梦境的函数
    dream_list = models.Dream.objects.all().order_by("-id")#这里进行一下排序
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'dream.html', {'d_list': dream_list,'author':author,'footer':footer})

def tojun(request):#与君说处理函数
    mood_list = models.Jun.objects.all().order_by("-id")#这里进行一下排序
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()

    return render(request, 'tojun.html', {'m_list': mood_list,'author':author,'footer':footer})

class AC(forms.Form):#form类用来验证评论表单
    name = fields.CharField(
        max_length=10,
        error_messages={'required':'名字不能为空',"max_length": '名字长度不能超过10'})
    contact = fields.CharField(
        max_length=30,
        error_messages={'required':'联系方式不能为空',"max_length": '长度不能超过30'})
    content = fields.CharField(
        max_length=144,
        error_messages={'required': '评论不能为空', "max_length": '评论长度不能超过144'},
        widget=widgets.Textarea())
    aid_id = fields.CharField()#外键关联相关字段

def article_content(request):#文章详细内容页面
    dict = {
        'name':'名字',
        'contact':'联系方式',
        'content':'请输入评论...'
    }#新建字典用来存放默认值
    author = models.Author.objects.all().first()
    footer = models.Footer.objects.all().first()
    profile = models.Profile.objects.all().first()

    if request.method == 'GET':
        aid = request.GET.get('aid')
        article = models.Article.objects.filter(id=aid).first()
        temp = article.content  # 获取文章内容
        content = temp.replace(" ", "&nbsp;").replace("\r", "<br/>")  # 对文本内容进行处理，使符合html的规则。
        comment = models.Comment.objects.filter(aid_id=aid)
        obj = AC(initial=dict)
        return render(request, 'article_content.html',
                      {'article':article,'content':content,'author':author,'footer':footer,'profile':profile,'obj':obj,'comment':comment})
    elif request.method == 'POST':
        aid = request.POST.get('aid_id')
        article = models.Article.objects.filter(id=aid).first()
        temp = article.content  # 获取文章内容
        content = temp.replace(" ", "&nbsp;").replace("\r", "<br/>")  # 对文本内容进行处理，使符合html的规则。
        comment = models.Comment.objects.filter(aid_id=aid)
        obj = AC(request.POST,initial=dict)
        if obj.is_valid():
            models.Comment.objects.create(**obj.cleaned_data)
            # obj.cleaned_data可以拿到正确的数据。并且是一个字典，我们通过models进行一条新评论的创建。
        else:
            return render(request, 'article_content.html',
                          {'article': article, 'content': content, 'author': author, 'footer': footer,
                           'profile': profile, 'obj': obj,'comment':comment})

        return render(request, 'article_content.html',
                          {'article': article, 'content': content, 'author': author, 'footer': footer,
                           'profile': profile, 'obj': obj,'comment':comment})
