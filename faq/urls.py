from django.conf.urls import patterns, url
from faq.views import FaqListView

urlpatterns = patterns('',


    url(r'^$', FaqListView.as_view(), name='Faq'),
)