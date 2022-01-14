from django.db import models


class FileRef(models.Model):
    id_name = models.CharField(max_length=120)
    pathways = models.JSONField()


class File(models.Model):
    id_name = models.CharField(max_length=120, unique=True)
    latest_index = models.IntegerField(default=0)
    copies = models.IntegerField(default=0)
