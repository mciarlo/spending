from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization

from . import models



class UserResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        queryset = User.objects.all()
        list_allowed_methods = ['get', 'put']


    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)
        


class MonthlyBudgetResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        queryset = models.MonthlyBudget.objects.all()

    def obj_create(self, bundle, request=None, **kwargs):
        return super(MonthlyBudgetResource, self).obj_create(
            bundle, request, user=request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)


class EntryResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        queryset = models.Entry.objects.all()

    def obj_create(self, bundle, request=None, **kwargs):
        return super(MonthlyBudgetResource, self).obj_create(
            bundle, request, user=request.user)

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)
