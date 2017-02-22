from django.db import models


class TestModel(models.Model):
    """ Models are the interface to the database """
    name = models.CharField(unique=True, max_length=20)
    number = models.IntegerField()

    def get_name(self):
        return self.name


class Question(models.Model):
    """ OBS: If atributes are changed, QuestionForm in forms must be updateted """
    answer_choices = (
        (1, 'Alternative 1'),
        (2, 'Alternative 2'),
        (3, 'Alternative 3'),
        (4, 'Alternative 4'),
    )
    question = models.CharField(max_length=80)
    alternative_1 = models.CharField(max_length=20)
    alternative_2 = models.CharField(max_length=20)
    alternative_3 = models.CharField(max_length=20)
    alternative_4 = models.CharField(max_length=20)
    correct_alternative = models.IntegerField(default=1, choices=answer_choices)
    # todo: add theme

    def __str__(self):
        return self.question


# todo: vertify the model lists
class Quiz(models.Model):
    name = models.CharField(max_length=20)
    questions = models.TextField(max_length=1000)   # List of questions

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=20)
    resources = models.TextField()      # List of resource links

    def __str__(self):
        return self.name

