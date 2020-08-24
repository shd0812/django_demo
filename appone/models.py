from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=100)
    # publisher_id = models.ForeignKey(Publisher)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE) #默认是级联删除
    """ 2.0 版本必填
    model.CASCADE 级联删除
    model.PROTECT 保护 
    model.SET(v) 删除后设置为某个值 
    model.SETDEFAULT 删除后设置为默认值 
    model.SET_NULL 删除后设置为null 
    """
    # authors = models.ManyToManyField('Author')

class Author(models.Model):
    author_name = models.CharField(max_length=32)
    books = models.ManyToManyField('Book')     #不再Author表中新增字段，会创建第三张表

