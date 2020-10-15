from django.db import models


class Ore(models.Model):
    name = models.CharField(max_length=255)