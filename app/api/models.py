from django.db import models


class Block(models.Model):
    name = models.CharField(max_length=50)
    code = models.IntegerField()
    status = models.CharField(max_length=25)
