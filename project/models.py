from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    Last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
# Create your models here.
class User_data(models.Model):
    login = models.CharField(max_length=255)
    pas = models.CharField(max_length=255)
