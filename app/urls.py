from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import main



urlpatterns = patterns('',
    ('', include(main.urls)),
)

# Serve static media in development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
