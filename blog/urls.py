from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'blog.views.post_main', name='blog_main'),
                       # url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
                       url(r'^category/(?P<id>\d+)/$', 'blog.views.post_category', name='blog_category'),
                       url(r'^(?P<id>\d+)/$', 'blog.views.post_detail', name='post_detail'),
)
