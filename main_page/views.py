from django.shortcuts import render
from b4 import settings
from main_page.models import Slide, Textblock
from catalog.models import Category
from blog.models import Post
from documents.models import Document


def show_index(request):
    slides = Slide.objects.all()
    textblocks = Textblock.objects.all()
    categories = Category.objects.filter(parent__isnull=True).all()
    posts = list(reversed(Post.objects.all()))[:2]
    docs = Document.objects.filter(main_page=True)
    return render(request, 'index/index_view.html',
                  {
                      'slides': slides,
                      'textblocks': textblocks,
                      'categories': categories,
                      'posts': posts,
                      'docs': docs,
                      'DEFAULT_TITLE': settings.DEFAULT_TITLE,
                      'DEFAULT_DESCRIPTION': settings.DEFAULT_DESCRIPTION,
                      'DEFAULT_KEYWORD': settings.DEFAULT_KEYWORD,
                  }
    )

