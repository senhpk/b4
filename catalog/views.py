from django.shortcuts import render
from b4 import settings
from catalog.models import Category, Product


def catalog_main(request):
    categories = Category.objects.filter(parent__isnull=True).all()
    return render(request, 'catalog/catalog_main.html',
                  {'categories': categories}
    )


def catalog_list(request, id):
    category = Category.objects.get(id=id)
    categories = Category.objects.filter(parent__isnull=True).all()
    return render(request, 'catalog/catalog_list.html',
                  {
                      'category': category,
                      'categories': categories
                  }
    )


def product_view(request, id):
    product = Product.objects.get(id=id)
    categories = Category.objects.filter(parent__isnull=True).all()
    return render(request, 'catalog/product_detail.html',
                  {
                      'product': product,
                      'categories': categories,
                      'DEFAULT_TITLE': settings.DEFAULT_TITLE,
                      'DEFAULT_DESCRIPTION': settings.DEFAULT_DESCRIPTION,
                      'DEFAULT_KEYWORD': settings.DEFAULT_KEYWORD,
                  }
    )