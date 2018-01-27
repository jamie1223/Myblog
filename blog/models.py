from django.db import models

# Create your models here.

class Article(models.Model):#用来存储文章
    title = models.CharField(max_length=20)
    index = models.CharField(max_length=120,null=True)
    content = models.TextField()
    create_datatime = models.DateTimeField(null=True)
    create_data = models.DateField(null=True)
    pic_link = models.CharField(max_length=500,null=True)
    top = models.BooleanField(default=False)
    
    def __str__(self):#在Python3中用 __str__ 代替 __unicode__
        return self.title

class Jun(models.Model):#用来存储与君说
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField()
    create_data = models.DateField()
    
    def __str__(self):#在Python3中用 __str__ 代替 __unicode__
        return self.title

class Dream(models.Model):#用来存储梦境
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField()
    create_data = models.DateField()

class Author(models.Model):#用来统一保存作者，以防后续需要改名。
    name = models.CharField(max_length=12)

class Footer(models.Model):#设置页脚的文字
    content = models.CharField(max_length=120,null=True)

class Tag(models.Model):#标签
    content = models.CharField(max_length=8)

class Words(models.Model):#页脚文字
    content = models.CharField(max_length=50)

class Profile(models.Model):#个人资料
    state = models.CharField(max_length=40)
    photo = models.CharField(max_length=500,null=True)

class Comment(models.Model):#评论表
    aid = models.ForeignKey(to='Article',to_field='id')
    name = models.CharField(max_length=10)
    contact = models.CharField(max_length=30)
    content = models.CharField(max_length=144)
    create_time = models.DateTimeField(auto_now_add=True,null=True)

