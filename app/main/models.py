from django.db import models
from django.contrib.auth.models import User


class MonthlyBudget(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class SpendingEntry(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=256, default='Unknown')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
