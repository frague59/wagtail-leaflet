from __future__ import absolute_import, unicode_literals

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')4q2m0*&#yyt$qkt($407=jd1&w5526(9l+(u+2q#do8b0nan%'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAILLEAFLET_DEBUG = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {'simple': {'format': u'%(levelname)s::%(name)s::%(message)s'},
                   'verbose': {'format': u'%(asctime)s::%(levelname)s::%(module)s::%(name)s::%(message)s'},
                   'null': {'format': u''}},

    'filters': {'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}},

    'handlers': {'mail_admins': {'level': 'ERROR',
                                 'class': 'django.utils.log.AdminEmailHandler',
                                 'filters': ['require_debug_false'],
                                 },
                 'console': {'level': 'DEBUG',
                             'class': 'logging.StreamHandler',
                             'formatter': 'simple'},
                 'null': {'level': 'DEBUG',
                          'class': 'logging.NullHandler',
                          'formatter': 'null'}},
    'loggers': {'wagtailleaflet.blocks': {'handlers': ['console'],
                                          'level': 'DEBUG',
                                          'propagate': True},
                }
}

try:
    from .local import *
except ImportError:
    pass
