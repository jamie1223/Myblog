from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    index = models.CharField(max_length=120,null=True)
    content = models.TextField()
    create_datatime = models.DateTimeField(auto_now_add=True,null=True)
    create_data = models.DateField(auto_now_add=True,null=True)


class Jun(models.Model):
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField(auto_now_add=True)
    create_data = models.DateField(auto_now_add=True)

class Dream(models.Model):
    content = models.TextField(max_length=400)
    create_datatime = models.DateTimeField(auto_now_add=True)
    create_data = models.DateField(auto_now_add=True)
