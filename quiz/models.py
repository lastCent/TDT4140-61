from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=80)
    # todo: passord
    mail = models.EmailField()
    tlf = models.IntegerField(max_length=8)     # Made for norwegian phone numbers

    def __str__(self):
        return self.name


class Student(Person):

    def __str__(self):
        return self.name


class Administrator(Person):

    def __str__(self):
        return self.name


class CourseMembers(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)


class ReadingMaterial(models.Model):
    info = models.CharField(max_length=500)


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


class CourseThemes(models.Model):
    course = models.ForeignKey(Course)
    theme = models.ForeignKey(ThemeTag)


class CourseExercises(models.Model):
    course = models.ForeignKey(Course)
    exercise = models.ForeignKey(Exercise)


class Exercise(models.Model):
    title = models.CharField(max_length=80)
    course = models.ForeignKey(Course)

    def __str__(self):
        return self.title


class ExerciseQuestions(models.Model):
    exercise = models.ForeignKey(Exercise)
    questions = models.ForeignKey(Question)


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

    def __str__(self):
        return self.question


class Result(models.Model):
    resultVal = models.IntegerField()  # Antall poeng
    # Relationships:
    question = models.ForeignKey(Question)
    student = models.ForeignKey(Student)

    def __str__(self):
        return self.resultVal

