from django.db import models
from tinymce.models import HTMLField


class Category(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='upload_images')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='category_set')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/catalog/%i/" % self.id

    def all_categories(self):
        categories = []
        current_category = self.parent
        while current_category is not None:
            categories.append(current_category)
            current_category = current_category.parent
        return categories


class Product(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='upload_images')
    info = HTMLField()
    description = HTMLField()
    category = models.ForeignKey(Category, related_name='product_set')

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/catalog/product/%i/" % self.id

    def all_categories(self):
        categories = []
        current_category = self.category
        while current_category is not None:
            categories.append(current_category)
            current_category = current_category.parent
        return categories


class Property(models.Model):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    product = models.ForeignKey(Product, related_name='property_set')


class TabImg(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    img = models.ImageField(upload_to='upload_images')
    product = models.ForeignKey(Product, related_name='tab_img_set')

    @property
    def image_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    @property
    def get_id(self):
            return "1000%i" % self.id


class TabText(models.Model):
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    product = models.ForeignKey(Product, related_name='tab_text_set')

    @property
    def get_id(self):
            return "2000%i" % self.id