from django.shortcuts import render
from about.models import About


def show_about(request):
    about = About.objects.get()
    return render(request, 'about/about_detail.html',
                  {
                      'about': about
                  })
