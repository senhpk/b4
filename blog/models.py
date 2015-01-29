# -*- coding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/category/%i/" % self.id


class Post(models.Model):
    title = models.CharField(max_length=255)
    datetime = models.DateField(u'Дата публикации')
    short_content = models.TextField(max_length=500)
    content = HTMLField()
    image = models.ImageField(upload_to='upload_images', blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='post_set')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
