from django.db import models
from tinymce.models import HTMLField


class About(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()
    img = models.ImageField(upload_to='upload_images', blank=True, null=True)

    def __unicode__(self):
        return self.title