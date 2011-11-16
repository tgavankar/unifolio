# This is your project's main settings file that can be committed to your
# repo. If you need to override a setting locally, use settings_local.py

from funfactory.settings_base import *


# Bundles is a dictionary of two dictionaries, css and js, which list css files
# and js files that can be bundled together by the minify app.
MINIFY_BUNDLES = {
    'css': {
        'main_css': (
            'css/main.css',
        ),
        'mobile_css': (
            'css/mobile.css',
        ),
    },
    'js': {
        'main_js': (
            'js/libs/jquery-1.4.4.min.js',
            'js/libs/jquery.cookie.js',
            'js/init.js',
        ),
    }
}


INSTALLED_APPS = list(INSTALLED_APPS) + [
    # Example code. Can (and should) be removed for actual projects.
    'landings',
    'portfolio',
    'accounts',
    'upload',
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

MAX_FILENAME_LENGTH = 200
MAX_FILEPATH_LENGTH = 250

DEFAULT_FILE_STORAGE = 'upload.storage.RenameFileStorage'
