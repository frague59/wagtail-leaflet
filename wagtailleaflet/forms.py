# -*- coding: utf-8 -*-
"""
Form fields for wagtail leaflet 

:creationdate: 04/05/17 16:59
:moduleauthor: François GUÉRIN <fguerin@ville-tourcoing.fr>
:modulename: wagtailleaflet.forms

"""
from __future__ import unicode_literals
import logging

from django.forms import HiddenInput
from djgeojson.fields import GeoJSONFormField, HAS_LEAFLET
from wagtailleaflet.widgets import LeafletWidget

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.forms')


# noinspection PyClassHasNoInit
class BlockGeoJSONFormField(GeoJSONFormField):
    widget = LeafletWidget if HAS_LEAFLET else HiddenInput
