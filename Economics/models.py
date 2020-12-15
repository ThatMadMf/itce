from django.db import models
from django.utils import timezone


class Expense(models.Model):
    name = models.CharField(max_length=64)
    value = models.DecimalField(decimal_places=4, max_digits=20)
    short_name = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'expenses'


class CurrencyState(models.Model):

    RUB = 'RUB'
    USD = 'USD'

    CURRENCY_CHOICES = [
        (RUB, 'Rubel'),
        (USD, 'Dollar'),
    ]

    name = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=RUB)
    date = models.DateField(default=timezone.now)
    value = models.FloatField()


class Operation(models.Model):
    name = models.CharField(max_length=64)


class AccountAction(models.Model):
    operation = models.ForeignKey(Operation, on_delete=models.DO_NOTHING, related_name='operations', null=False)
    vat = models.BooleanField(default=False)
    revs_tax = models.BooleanField(default=False)
    revenue_tax = models.BooleanField(default=False)
    money = models.BooleanField(default=False)
    currency = models.ForeignKey(CurrencyState, on_delete=models.DO_NOTHING, related_name='operations', null=False)
    money_change = models.FloatField()
    vat_value = models.FloatField()
    tax_value = models.FloatField()
