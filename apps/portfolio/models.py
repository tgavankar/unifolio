from datetime import datetime

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

from portfolio.utils import auto_delete_files
from upload.models import UploadedFile


class Gallery(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    created = models.DateTimeField(default=datetime.now, db_index=True)
    updated_by = models.ForeignKey(User, null=True,
                                   related_name="gallery_updated")
    creator = models.ForeignKey(User, related_name='gallery')
    description = models.TextField(max_length=10000)
    visibility = models.BooleanField(default=True, null=False)

    def __unicode__(self):
        return '%s' % (self.title)

class Media(models.Model):
    """Generic model for media"""
    title = models.CharField(max_length=255, db_index=True)
    created = models.DateTimeField(default=datetime.now, db_index=True)
    updated = models.DateTimeField(default=datetime.now, db_index=True)
    gallery = models.ForeignKey(Gallery, null=True, db_index=True)
    description = models.TextField(max_length=10000)
    visibility = models.BooleanField(default=True, null=False, db_index=True)

    class Meta(object):
        abstract = True
        ordering = ['-created']

    def __unicode__(self):
        return '%s' % (self.title)


@auto_delete_files
class Image(Media):
    creator = models.ForeignKey(User, related_name='gallery_images')
    file = models.ForeignKey(UploadedFile)

    def get_absolute_url(self):
        return reverse('portfolio.entry', args=[self.id])

    def thumbnail_url_if_set(self):
        """Returns self.thumbnail, if set, else self.file"""
        return self.thumbnail.url if self.thumbnail else self.file.url


@auto_delete_files
class Video(Media):
    creator = models.ForeignKey(User, related_name='gallery_videos')
    webm = models.FileField(upload_to=settings.GALLERY_VIDEO_PATH, null=True,
                            max_length=settings.MAX_FILEPATH_LENGTH)
    ogv = models.FileField(upload_to=settings.GALLERY_VIDEO_PATH, null=True,
                           max_length=settings.MAX_FILEPATH_LENGTH)
    flv = models.FileField(upload_to=settings.GALLERY_VIDEO_PATH, null=True,
                           max_length=settings.MAX_FILEPATH_LENGTH)
    poster = models.ImageField(upload_to=settings.GALLERY_VIDEO_THUMBNAIL_PATH,
                               max_length=settings.MAX_FILEPATH_LENGTH,
                               null=True)
    thumbnail = models.ImageField(
        upload_to=settings.GALLERY_VIDEO_THUMBNAIL_PATH, null=True,
        max_length=settings.MAX_FILEPATH_LENGTH)

    def get_absolute_url(self):
        return reverse('portfolio.entry', args=[self.id])

    def thumbnail_url_if_set(self):
        """Returns self.thumbnail.url, if set, else default thumbnail URL"""
        progress_url = settings.GALLERY_VIDEO_THUMBNAIL_PROGRESS_URL
        return self.thumbnail.url if self.thumbnail else progress_url


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'description', 'visibility', )

    def save(self, creator, isedit, **kwargs):
        # Throws a TypeError if somebody passes in a commit kwarg:
        new_gal = super(GalleryForm, self).save(commit=False, **kwargs)

        new_gal.updated_by = creator
        if not isedit:
            new_gal.creator = creator
        new_gal.save()
        return new_gal

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'description', 'gallery', 'created', 'visibility', )

