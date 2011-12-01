from django import http
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt


import bleach
import commonware
import jingo
from mobility.decorators import mobile_template
from session_csrf import anonymous_csrf

from portfolio.models import Gallery, GalleryForm, Image, ImageForm

log = commonware.log.getLogger('playdoh')


def view_entry(request, entry_id):
    g = get_object_or_404(Image, pk=entry_id)
    if g.creator != request.user:
        g = get_object_or_404(Image, pk=entry_id, visibility=True)

    data = {}
    data['e'] = g
    return render(request, 'portfolio/entry.html', data)


def view_gallery(request, gallery_id):
    g = get_object_or_404(Gallery, pk=gallery_id)
    e = Image.objects.filter(gallery=gallery_id)

    if g.creator != request.user:
        e = e.filter(visibility=True)

    data = {}
    data['g'] = g
    data['entries'] = list(e)
    return render(request, 'portfolio/gallery.html', data)


def view_portfolio(request, username):
    user = get_object_or_404(User, username=username)

    e = Gallery.objects.filter(creator=user)

    if user != request.user:
        e = e.filter(visibility=True)

    data = {}
    data['entries'] = list(e)
    data['user'] = user
    return render(request, 'portfolio/portfolio.html', data)

@login_required
def new_gallery(request):
    """Create a new gallery."""
    if request.method == 'GET':
        gal_form = GalleryForm()
        return jingo.render(request, 'portfolio/new_gallery.html',
                            {'gallery_form': gal_form})

    gal_form = GalleryForm(request.POST)

    if gal_form.is_valid():
        gal = gal_form.save(request.user, False)
        return http.HttpResponseRedirect(reverse('portfolio.viewgallery',
                                    args=[gal.id]))

    return jingo.render(request, 'portfolio/new_gallery.html',
                        {'gallery_form': gal_form})

@login_required
def edit_gallery(request, gallery_id):
    g = get_object_or_404(Gallery, pk=gallery_id)

    if request.user != g.creator:
        return http.HttpResponseForbidden()

    if request.method == 'GET':
        gal_form = GalleryForm(instance=g)
        return jingo.render(request, 'portfolio/edit_gallery.html',
                            {'gallery_form': gal_form,
                             'id': g.id})

    gal_form = GalleryForm(request.POST, instance=g)

    if gal_form.is_valid():
        gal = gal_form.save(request.user, True)
        return http.HttpResponseRedirect(reverse('portfolio.viewgallery',
                                    args=[gal.id]))

    return jingo.render(request, 'portfolio/edit_gallery.html',
                        {'gallery_form': gal_form,
                         'id': g.id})


@login_required
def edit_image(request, image_id):
    g = get_object_or_404(Image, pk=image_id)

    if request.user != g.creator:
        return http.HttpResponseForbidden()

    if request.method == 'GET':
        gal_form = ImageForm(instance=g)
        gal_form.fields['gallery'].queryset = Gallery.objects.filter(creator=request.user)
        return jingo.render(request, 'portfolio/edit_image.html',
                            {'gallery_form': gal_form,
                             'id': g.id,
                             'imgpath': g.file.file})

    gal_form = ImageForm(request.POST, instance=g)
    gal_form.fields['gallery'].queryset = Gallery.objects.filter(creator=request.user)

    if gal_form.is_valid():
        gal = gal_form.save()
        return http.HttpResponseRedirect(reverse('portfolio.viewentry',
                                    args=[gal.id]))

    return jingo.render(request, 'portfolio/edit_image.html',
                        {'gallery_form': gal_form,
                         'id': g.id,
                         'imgpath': g.file.file})


@login_required
def unlinked_images(request):
    e = Image.objects.filter(gallery=None, creator=request.user)

    data = {}
    data['entries'] = list(e)
    return render(request, 'portfolio/unlinked.html', data)


@login_required
@csrf_exempt
def delete_gallery(request, gallery_id):
    g = get_object_or_404(Gallery, pk=gallery_id)

    if request.user != g.creator:
        return http.HttpResponseForbidden()

    g.delete()

    return http.HttpResponse(status=200)

@login_required
@csrf_exempt
def delete_image(request, image_id):
    g = get_object_or_404(Image, pk=image_id)

    if request.user != g.creator:
        return http.HttpResponseForbidden()

    g.delete()

    return http.HttpResponse(status=200)


