from django.db import models


class TestModel(models.Model):
    """ Models are the interface to the database """
    name = models.CharField()
    number = models.IntegerField()

    def get_name(self):
        return self.name
