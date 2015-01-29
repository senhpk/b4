from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'b4.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'main_page.views.show_index', name="home"),
                       url(r'^about/', 'about.views.show_about', name="about"),
                       url(r'^test/', TemplateView.as_view(template_name='contact/thank.html'), name="about"),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^documents/', include('documents.urls')),
                       url(r'^faq/', include('faq.urls')),
                       url(r'^contact/', TemplateView.as_view(template_name='contact/contact.html'), name="contact"),
                       url(r'^send_email/', 'contact.views.send_email',
                           name="send_email"),
                       url(r'^catalog/', include('catalog.urls')),
                       url(r'^tinymce/', include('tinymce.urls')),
)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT}))