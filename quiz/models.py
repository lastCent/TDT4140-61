from django.db import models


class TestModel(models.Model):
    """ Models are the interface to the database """
    name = models.CharField(unique=True, max_length=20)
    number = models.IntegerField()

    def get_name(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Student(Person):

    def __str__(self):
        return self.name


class Administrator(Person):

    def __str__(self):
        return self.name

class ReadingMaterial(models.Model):
    infoReference = models.IntegerField()  # Må sikkert endres


class ThemeTag(models.Model):
    name = models.CharField(max_length=20)
    # Relationships:
    material = models.ManyToManyField(ReadingMaterial)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    # Relationships:
    administrators = models.ManyToManyField(Administrator)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    title = models.CharField(max_length=80)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.title


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
    # Relationships:
    themeTags = models.ManyToManyField(ThemeTag)
    belongsToExercises = models.ManyToManyField(Exercise)  # Sjekk onDelete og update options en gang

    def __str__(self):
        return self.question


class Result(models.Model):
    resultVal = models.IntegerField()  # Antall poeng
    # Relationships:
    question = models.ForeignKey(Question)
    student = models.ForeignKey(Student)

    def __str__(self):
        return self.resultVal

