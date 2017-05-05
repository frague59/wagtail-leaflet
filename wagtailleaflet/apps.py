from django.apps import AppConfig


class WagtailLeafletAppConfig(AppConfig):
    name = "wagtailleaflet"

    def ready(self):
        # Load settings

        # noinspection PyUnresolvedReferences
        from wagtailleaflet.conf import WagtailAppConf




