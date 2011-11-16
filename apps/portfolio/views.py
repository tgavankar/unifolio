from django import http
from django.shortcuts import render

import bleach
import commonware
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf


log = commonware.log.getLogger('playdoh')


def view_entry(request, entry_id):
    data = {}
    data['id'] = entry_id
    return render(request, 'portfolio/entry.html', data)


def view_gallery(request, gallery_id):
    data = {}
    data['id'] = gallery_id
    return render(request, 'portfolio/gallery.html', data)
