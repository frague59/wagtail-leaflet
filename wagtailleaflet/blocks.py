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

from django import forms
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from wagtail.wagtailcore.blocks import FieldBlock

from wagtailleaflet.forms import BlockGeoJSONFormField

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.blocks')


class GeoJSONBlock(FieldBlock):
    geom_type = None

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, **kwargs):
        if self.geom_type is None:
            raise NotImplemented('You are attempting to use ``GeoJSONBlock`` directly, which *WILL* not work !')

        self.field = BlockGeoJSONFormField(required=required,
                                           help_text=help_text,
                                           max_length=max_length,
                                           min_length=min_length,
                                           geom_type=self.geom_type)
        super(GeoJSONBlock, self).__init__(**kwargs)

    def render_form(self, value, prefix='', errors=None):
        """
        Renders ``edit`` form

        :param value: current value 
        :param prefix: prefix of the form item 
        :param errors: Validations errors
        :returns: HTML Fragment  
        """
        logger.debug('MapBlock::render_form() value = %s', value)
        rendered = super(GeoJSONBlock, self).render_form(value=value, prefix=prefix, errors=errors)
        return rendered

    def render(self, value, context=None):
        """
        Renders the widget in the web site

        :param value: current value 
        :param context: Additional render context 
        :returns: HTML Fragment  
        """
        logger.debug('MapBlock::render() value = %s', value)
        local_context = context or {}
        logger.debug('MapBlock::render() name = %s', self.name)
        local_context['name'] = self.name
        rendered = super(GeoJSONBlock, self).render(value=value, context=local_context)
        return rendered

    @property
    def media(self):
        return forms.Media(
            js=['wagtailleaflet/leaflet_init.js', ]
        )

    def js_initializer(self):
        """
        JS function to launch on start'up
        :returns: JS function name, from ``wagtailleaflet/leaflet_init.js``
        """
        output = 'drawMap'
        logger.debug('MapBlock::js_initializer() output = %s', output)
        return output

    def html_declarations(self):
        output = render_to_string('wagtailleaflet/leaflet_forms.html')
        return output

    class Meta:
        template = 'wagtailleaflet/blocks/wagtailleaflet.html'


class GeoJSONPointBlock(GeoJSONBlock):
    """
    A Geo JSON field into a block !
    
    .. note::
       ``POINT`` item 
    """
    geom_type = 'POINT'

    class Meta:
        icon = 'pick'
        label = _('Point map')


class GeoJSONMultiPointBlock(GeoJSONBlock):
    """
    A Geo JSON field into a block !
    
    .. note::
       ``MultiPoint`` item 
    """
    geom_type = 'MULTIPOINT'
