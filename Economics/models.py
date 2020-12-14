from django.db import models


class Expense(models.Model):
    name = models.CharField(max_length=64)
    value = models.DecimalField(decimal_places=4, max_digits=20)
    short_name = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'expenses'
