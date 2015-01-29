from blog.models import Post, Category
from django.shortcuts import render


def post_main(request):
    post_list = Post.objects.all()
    category_list = Category.objects.all()
    return render(request, 'blog/post_main.html',
                  {
                      'post_list': post_list,
                      'category_list': category_list
                  }
    )


def post_category(request, id):
    post_list = Category.objects.get(id=id)
    category_list = Category.objects.all()
    return render(request, 'blog/post_list.html',
                  {
                      'post_list': post_list,
                      'category_list': category_list
                  }
    )


def post_detail(request, id):
    post = Post.objects.get(id=id)
    category_list = Category.objects.all()
    return render(request, 'blog/post_detail.html',
                  {
                      'post': post,
                      'category_list': category_list
                  }

    )
