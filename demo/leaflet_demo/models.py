# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore import blocks
from wagtailleaflet.blocks import GeoJSONPointBlock


class DemoPage(Page):
    """
    Simple demo page 
    """
    body = StreamField([('text', blocks.RichTextBlock()),
                        ('map', GeoJSONPointBlock()), ])

    content_panels = Page.content_panels + [StreamFieldPanel('body')]

