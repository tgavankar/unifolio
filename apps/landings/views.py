from django import http
from django.shortcuts import render

import bleach
import commonware
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf

from portfolio.models import Image

log = commonware.log.getLogger('playdoh')


@mobile_template('landings/{mobile/}home.html')
def home(request, template=None):
    """Main example view."""
    data = {}  # You'd add data here that you're sending to the template.
    r = Image.objects.filter(gallery__isnull=False, visibility=True).order_by('-updated')[:3]
    data['recent'] = []
    for e in r:
        data['recent'].append(e)
    return render(request, template, data)


@anonymous_csrf
def bleach_test(request):
    """A view outlining bleach's HTML sanitization."""
    allowed_tags = ('strong', 'em')

    data = {}

    if request.method == 'POST':
        bleachme = request.POST.get('bleachme', None)
        data['bleachme'] = bleachme
        if bleachme:
            data['bleached'] = bleach.clean(bleachme, tags=allowed_tags)

    return render(request, 'landings/bleach.html', data)

