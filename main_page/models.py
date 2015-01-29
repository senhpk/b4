from django.db import models
from blog.models import Post
from tinymce.models import HTMLField


class Slide(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='upload_images', blank=True, null=True)
    post = models.ForeignKey(Post, related_name='slide_set')

    def __unicode__(self):
        return self.title


class Textblock(models.Model):
    title = models.CharField(max_length=255)
    block = HTMLField()

    def __unicode__(self):
        return self.title

