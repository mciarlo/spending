import datetime

from django.db import models
from django.contrib.auth.models import User



class MonthlyBudget(models.Model):
    user = models.ForeignKey(User)
    date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)


class Entry(models.Model):
    user = models.ForeignKey(User)
    # Default to now
    date = models.DateField(blank=True)
    name = models.CharField(max_length=256, default='Unknown')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # If we don't provide a date, make it today!
        if self.date is None:
            self.date = datetime.date.today()

        return super(Entry, self).save(*args, **kwargs)
