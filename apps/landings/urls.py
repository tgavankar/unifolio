from django.conf.urls.defaults import *


urlpatterns = patterns('landings.views',
    url(r'^$', 'home', name='landings.home'),
    url(r'^bleach/?$', 'bleach_test', name='landings.bleach'),
)
