from django.db import models


class TestModel(models.Model):
    """ Models are the interface to the database """
    some_name = models.CharField()
    number = models.IntegerField()
