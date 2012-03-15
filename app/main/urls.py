from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from tastypie.api import Api

from . import views
from . import resources


v1_api = Api(api_name='v1')
v1_api.register(resources.UserResource())
v1_api.register(resources.MonthlyBudgetResource())
v1_api.register(resources.EntryResource())


urlpatterns = patterns('',
    url('^$', views.index, name='index'),
    ('^api/', include(v1_api.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
