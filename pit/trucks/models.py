from django.db import models


class Truck(models.Model):
    name = models.CharField(max_length=255)