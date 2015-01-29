from django.contrib import admin
from models import Category, Product, Property, TabImg, TabText


class PropertyInLine(admin.StackedInline):
    model = Property
    extra = 0


class TabImgInLine(admin.StackedInline):
    model = TabImg
    extra = 0


class TabTextInLine(admin.StackedInline):
    model = TabText
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [PropertyInLine, TabImgInLine, TabTextInLine]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)