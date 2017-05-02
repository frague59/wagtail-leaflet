# -*- coding: utf-8 -*-
"""
Blocks definitions for wagtail wagtailleaflet integration

:creationdate: 02/05/17 13:36
:moduleauthor: François GUÉRIN <fguerin@ville-tourcoing.fr>
:modulename: wagtailleaflet.blocks

"""
from __future__ import absolute_import
from __future__ import unicode_literals

import logging

from django.template.loader import render_to_string
from django.templatetags.static import static
from django.utils.translation import ugettext_lazy as _
from djgeojson.fields import GeoJSONFormField
from wagtail.wagtailcore.blocks import StructBlock, CharBlock, FieldBlock

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.blocks')


class GeoJSONBlock(FieldBlock):
    """
    A Geo JSON field in a block !
    """
    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, **kwargs):
        self.field = GeoJSONFormField(required=required,
                                      help_text=help_text,
                                      max_length=max_length,
                                      min_length=min_length,
                                      geom_type='Point'
                                      )
        super(GeoJSONBlock, self).__init__(**kwargs)


class LeafletBlock(StructBlock):
    """
    Displays a location
    """
    title = CharBlock()

    geojson = GeoJSONBlock()

    def render_form(self, value, prefix='', errors=None):
        logger.debug('LeafletBlock::render_form() value = %s', value)
        rendered = super(LeafletBlock, self).render_form(value=value, prefix=prefix, errors=errors)
        return rendered

    def html_declarations(self):
        output = render_to_string('wagtailleaflet/leaflet_forms.html')
        return output

    class Meta:
        icon = 'pick'
        template = 'wagtailleaflet/blocks/wagtailleaflet.html'
        label = _('Map')

    class Media:
        js = static('wagtailleaflet/leaflet.js')
