from django.db import models
from django.contrib.auth.models import User


class ReadingMaterial(models.Model):
    title = models.CharField(max_length=40, primary_key=True)
    link = models.CharField(max_length=100)  # Langt felt, kan jo være komplisert link


class ThemeTag(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    # Relationships:
    material = models.ManyToManyField(ReadingMaterial)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=100)
    # Relationships:
    administrators = models.ManyToManyField(User)   # Antar dette er greit,
    content = models.ManyToManyField(ReadingMaterial, blank=True)  # Lesestoff som faget inneholder

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    student = models.OneToOneField(User)
    courses = models.ManyToManyField(Course)


class CourseAdmin(models.Model):
    admin = models.OneToOneField(User)
    courses = models.ManyToManyField(Course)


class Question(models.Model):
    answer_choices = (
        (1, 'Alternative 1'),
        (2, 'Alternative 2'),
        (3, 'Alternative 3'),
        (4, 'Alternative 4'),
    )
    title = models.CharField(max_length=30, primary_key=True)
    question = models.CharField(max_length=80)
    alternative_1 = models.CharField(max_length=20)
    alternative_2 = models.CharField(max_length=20)
    alternative_3 = models.CharField(max_length=20)
    alternative_4 = models.CharField(max_length=20)
    correct_alternative = models.IntegerField(default=1, choices=answer_choices)
    is_worth = models.IntegerField()
    # Relationships:
    themeTags = models.ManyToManyField(ThemeTag)  # Relaterte temaer
    belongsTo = models.ForeignKey(Course)  # Faget spørsmålet hører til

    def __str__(self):
        return self.question


class Exercise(models.Model):
    title = models.CharField(max_length=80, primary_key=True)
    course = models.ForeignKey(Course)
    contains = models.ManyToManyField(Question)  # Spørsmålet oppgaven vil tilby

    def __str__(self):
        return self.title


class Result(models.Model):
    resultVal = models.IntegerField()  # Antall poeng
    # Relationships:
    question = models.ForeignKey(Question)
    student = models.ForeignKey(User)

    def __str__(self):
        return self.resultVal
