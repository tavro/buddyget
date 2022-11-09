from django.db import models


class Budget(models.Model):
    title = models.CharField(max_length=256)