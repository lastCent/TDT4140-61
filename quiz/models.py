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
    # todo: adding theme

    def get_question(self):
        return self.question

    def get_alternatives(self):
        pass

    def get_answers(self):
        pass
