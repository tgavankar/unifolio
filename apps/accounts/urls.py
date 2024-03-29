import django
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.auth.views import login, logout

from session_csrf import anonymous_csrf

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    url(r'login/$', anonymous_csrf(login), {'template_name': 'accounts/login.html'}, name='accounts.login'),
    url(r'logout/$', logout, {'template_name': 'accounts/logout.html'}, name='accounts.logout'),
    url(r'register/$', 'accounts.views.register', name='accounts.register'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)



