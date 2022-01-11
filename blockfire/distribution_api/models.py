from django.db import models


class Node(models.Model):
    data_address = models.TextField()
    earnings = models.FloatField()
    utilised_storage_mb = models.FloatField()
    email = models.EmailField(unique=True)
    password = models.TextField()
    status = models.TextField()

