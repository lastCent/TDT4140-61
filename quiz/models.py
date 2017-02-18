from django.db import models


class TestModel(models.Model):
    """ Models are the interface to the database """
    name = models.CharField(unique=True, max_length=20)
    number = models.IntegerField()

    def get_name(self):
        return self.name

