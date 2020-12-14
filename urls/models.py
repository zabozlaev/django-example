from django.db import models

# Create your models here.


class Url(models.Model):
    source_url = models.URLField()
    short_url = models.CharField(max_length=16)
