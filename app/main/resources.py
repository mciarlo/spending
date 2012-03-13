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
        resource_name = 'user'


class MonthlyBudgetResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        queryset = models.MonthlyBudget.objects.all()
        resource_name = 'budget'


class SpendingEntryResource(ModelResource):
    class Meta:
        authentication = Authentication()
        authorization = Authorization()
        queryset = models.SpendingEntry.objects.all()
        resource_name = 'spending_entry'
