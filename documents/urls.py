from django.conf.urls import patterns, url
from documents.views import DocumentListView

urlpatterns = patterns('',


    url(r'^$', DocumentListView.as_view(), name='Faq'),
)