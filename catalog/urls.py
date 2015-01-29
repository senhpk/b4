from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'catalog.views.catalog_main', name='index'),
                       url(r'^(?P<id>\d+)/$', 'catalog.views.catalog_list', name='category'),
                       url(r'^product/(?P<id>\d+)/$', 'catalog.views.product_view', name='product')
                       )