from django.conf.urls.defaults import *


urlpatterns = patterns('portfolio.views',
    url(r'^entry/(?P<entry_id>\d+)$', 'view_entry', name='portfolio.viewentry'),
    url(r'^view/(?P<gallery_id>\d+)$', 'view_gallery', name='portfolio.viewgallery'),
    url(r'^newgallery$', 'new_gallery', name='portfolio.newgallery'),
)
