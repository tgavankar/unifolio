# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *


# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'main_css': (
            'css/libs/jquery.fancybox.css',
            'css/main.css',
            'css/libs/style.css',
        ),
        'mobile_css': (
            'css/mobile.css',
        ),
        'upload': (
            'css/libs/jqueryui/1.8.14/themes/base/jquery.ui.all.css',
            'css/libs/jquery.fileupload-ui.css',
            'css/libs/thumbnail-scaling.css',
        ),
    },
    'js': {
        'main_js': (
            'js/libs/jquery-1.6.2.min.js',
            'js/libs/jquery.cookie.js',
            'js/libs/jquery.fancybox/jquery.easing-1.3.pack.js',
            'js/libs/jquery.fancybox/jquery.mousewheel-3.0.6.pack.js',
            'js/libs/jquery.fancybox/jquery.fancybox.pack.js?v=2.0.3',
            'js/libs/hover.js',
            'js/init.js',
        ),
        'upload': (
            'js/libs/jquery-ui-1.8.14.custom.min.js',
            'js/libs/jquery.templates/beta1/jquery.tmpl.min.js',
            'js/libs/jquery.iframe-transport.js',
            'js/libs/jquery.fileupload.js',
            'js/libs/jquery.fileupload-ui.js',
            'js/libs/application.js',
        ),
    }
}


INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Example code. Can (and should) be removed for actual projects.
    'landings',
    'portfolio',
    'accounts',
    'upload',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

# Because Jinja2 is the default template loader, add any non-Jinja templated
# apps here:
JINGO_EXCLUDE_APPS = [
    'admin',
]

# Tells the extract script what files to look for L10n in and what function
# handles the extraction. The Tower library expects this.

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['lhtml'] = [
#    ('**/templates/**.lhtml',
#        'tower.management.commands.extract.extract_tower_template'),
# ]

# # Use this if you have localizable HTML files:
# DOMAIN_METHODS['javascript'] = [
#    # Make sure that this won't pull in strings from external libraries you
#    # may use.
#    ('media/js/**.js', 'javascript'),
# ]

LOGGING = dict(loggers=dict(playdoh = {'level': logging.DEBUG}))

LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/'

GALLERY_IMAGE_PATH = 'uploads/gallery/images/'
GALLERY_IMAGE_THUMBNAIL_PATH = 'uploads/gallery/images/thumbnails/'
GALLERY_VIDEO_PATH = 'uploads/gallery/videos/'
GALLERY_VIDEO_THUMBNAIL_PATH = 'uploads/gallery/videos/thumbnails/'

STATIC_URL = '/media/upload_static/'

MAX_FILENAME_LENGTH = 200
MAX_FILEPATH_LENGTH = 250

DEFAULT_FILE_STORAGE = 'upload.storage.RenameFileStorage'
