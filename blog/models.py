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

class Jun(models.Model):#用来存储与君说
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField()
    create_data = models.DateField()

class Dream(models.Model):#用来存储梦境
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField()
    create_data = models.DateField()

class Author(models.Model):#用来统一保存作者，以防后续需要改名。
    name = models.CharField(max_length=12)

class Footer(models.Model):#设置页脚的文字
    content = models.CharField(max_length=120,null=True)

class Tag(models.Model):
    content = models.CharField(max_length=8)

class Words(models.Model):
    content = models.CharField(max_length=50)

class Profile(models.Model):
    state = models.CharField(max_length=40)
    photo = models.CharField(max_length=500,null=True)

