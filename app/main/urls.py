from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views


urlpatterns = patterns('',
    url('^$', views.index, name='index'),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
