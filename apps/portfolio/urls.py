from django.conf.urls.defaults import *


urlpatterns = patterns('portfolio.views',
    url(r'^entry/(?P<entry_id>\d+)$', 'view_entry', name='portfolio.viewentry'),
    url(r'^view/(?P<gallery_id>\d+)$', 'view_gallery', name='portfolio.viewgallery'),
    url(r'^list/(?P<username>[^/]+)$', 'view_portfolio', name='portfolio.viewportfolio'),
    url(r'^editgallery/(?P<gallery_id>\d+)$', 'edit_gallery', name='portfolio.editgallery'),
    url(r'^editimage/(?P<image_id>\d+)$', 'edit_image', name='portfolio.editimage'),
    url(r'^newgallery$', 'new_gallery', name='portfolio.newgallery'),
    url(r'^unlinked$', 'unlinked_images', name='portfolio.unlinked'),
)
