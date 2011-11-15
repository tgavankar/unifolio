import datetime
import json as jsonlib
import re
import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import QueryDict
from django.utils.encoding import smart_str
from django.utils.http import urlencode
from django.utils.tzinfo import LocalTimezone

from jingo import register, env
import jinja2
from tower import ugettext_lazy as _lazy, ungettext


class DateTimeFormatError(Exception):
    """Called by the datetimeformat function when receiving invalid format."""
    pass


def url(viewname, *args, **kwargs):
    """Helper for Django's ``reverse`` in templates.

    Uses sumo's locale-aware reverse."""
    locale = kwargs.pop('locale', None)
    return reverse(viewname, locale=locale, args=args, kwargs=kwargs)


@register.function
def label_with_help(f):
    """Print the label tag for a form field, including the help_text
    value as a title attribute."""
    label = u'<label for="%s" title="%s">%s</label>'
    return jinja2.Markup(label % (f.auto_id, f.help_text, f.label))


@register.filter
def yesno(boolean_value):
    return jinja2.Markup(_lazy(u'Yes') if boolean_value else _lazy(u'No'))


@register.filter
def remove(list_, item):
    """Removes an item from a list."""
    return [i for i in list_ if i != item]
