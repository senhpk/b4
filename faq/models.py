from django.db import models
from tinymce.models import HTMLField


class Faq(models.Model):
    question = models.CharField(max_length=255)
    content = HTMLField()

    def __unicode__(self):
        return self.question