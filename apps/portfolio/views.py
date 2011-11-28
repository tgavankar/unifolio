from django import http
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render


import bleach
import commonware
import jingo
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf

from portfolio.models import GalleryForm

log = commonware.log.getLogger('playdoh')


def view_entry(request, entry_id):
    data = {}
    data['id'] = entry_id
    return render(request, 'portfolio/entry.html', data)


def view_gallery(request, gallery_id):
    data = {}
    data['id'] = gallery_id
    return render(request, 'portfolio/gallery.html', data)


@login_required
def new_gallery(request):
    """Create a new gallery."""
    if request.method == 'GET':
        gal_form = GalleryForm()
        return jingo.render(request, 'portfolio/new_gallery.html',
                            {'gallery_form': gal_form})

    gal_form = GalleryForm(request.POST)

    if gal_form.is_valid():
        gal = gal_form.save(request.user)
        return http.HttpResponseRedirect(reverse('portfolio.viewgallery',
                                    args=[gal.id]))

    return jingo.render(request, 'portfolio/new_gallery.html',
                        {'gallery_form': gal_form})


