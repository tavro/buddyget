from django.db import models


class Budget(models.Model):
    title = models.CharField(max_length=256)


class BudgetRow(models.Model):
    date = models.DateField()
    place = models.CharField(max_length=256)
    cost = models.DecimalField(max_digits=256, decimal_places=3)
    budget = models.ForeignKey(to=Budget, related_name="rows", null=True, blank=True, on_delete=models.CASCADE)
