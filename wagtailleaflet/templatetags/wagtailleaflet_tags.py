# -*- coding: utf-8 -*-
"""
Template tags for wagtailleaflet display in pages 

:creationdate: 05/05/17 13:20
:moduleauthor: François GUÉRIN <fguerin@ville-tourcoing.fr>
:modulename: wagtailleaflet.templatetags.wagtailleaflet_tags

"""
from __future__ import unicode_literals
import logging
from django import template
from django.conf import settings

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.templatetags.wagtailleaflet_tags')
register = template.Library()


@register.inclusion_tag('wagtailleaflet/wagtailleaflet.html', takes_context=False)
def wagtailleaflet(data):
    debug = settings.WAGTAILLEAFLET_DEBUG
    return {'data': data}
