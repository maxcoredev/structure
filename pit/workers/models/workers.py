from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255)