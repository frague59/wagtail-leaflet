# -*- coding: utf-8 -*-
"""
# COMMENT HERE #

:creationdate: 05/05/17 13:24
:moduleauthor: François GUÉRIN <fguerin@ville-tourcoing.fr>
:modulename: wagtailleaflet.conf

"""
from __future__ import unicode_literals
import logging
from appconf import AppConf

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.conf')


class WagtailAppConf(AppConf):

    DEBUG = False

    class Meta:
        prefix = 'wagtailleaflet'
