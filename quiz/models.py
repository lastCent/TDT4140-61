from django.db import models


# TODO: Replace Person, Student and Administrator with Django User object, and corresponding groups + permissions
class Person(models.Model):
    name = models.CharField(max_length=80)
    mail = models.CharField(max_length=80)
    tlf = models.IntegerField()

    def __str__(self):
        return self.name


class Student(Person):

    def __str__(self):
        return self.name


class Lecturer(Person):

    def __str__(self):
        return self.name


class ReadingMaterial(models.Model):
    title = models.CharField(max_length=40)
    link = models.CharField(max_length=100)  # Langt felt, kan jo være komplisert link


class ThemeTag(models.Model):
    name = models.CharField(max_length=20)
    # Relationships:
    material = models.ManyToManyField(ReadingMaterial)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20)
    # Relationships:
    administrators = models.ManyToManyField(Lecturer)
    content = models.ManyToManyField(ReadingMaterial)  # Lesestoff som faget inneholder

    def __str__(self):
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
    # Relationships:
    themeTags = models.ManyToManyField(ThemeTag)  # Relaterte temaer
    belongsTo = models.ForeignKey(Course)  # Faget spørsmålet hører til

    def __str__(self):
        return self.question

class Exercise(models.Model):
    title = models.CharField(max_length=80)
    course = models.ForeignKey(Course)
    contains = models.ManyToManyField(Question)  # Spørsmålet oppgaven vil tilby

    def __str__(self):
        return self.title


class Result(models.Model):
    resultVal = models.IntegerField()  # Antall poeng
    # Relationships:
    question = models.ForeignKey(Question)
    student = models.ForeignKey(Student)

    def __str__(self):
        return self.resultVal
