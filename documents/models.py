from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='upload_documents', blank=True, null=True)
    main_page = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title