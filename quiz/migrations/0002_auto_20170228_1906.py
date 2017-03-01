# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='belongsToExercises',
        ),
        migrations.RemoveField(
            model_name='readingmaterial',
            name='infoReference',
        ),
        migrations.AddField(
            model_name='course',
            name='content',
            field=models.ManyToManyField(to='quiz.ReadingMaterial'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='contains',
            field=models.ManyToManyField(to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='person',
            name='mail',
            field=models.CharField(default=80, max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='tlf',
            field=models.IntegerField(default=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='belongsTo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='quiz.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readingmaterial',
            name='link',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='readingmaterial',
            name='title',
            field=models.CharField(default='title', max_length=40),
            preserve_default=False,
        ),
    ]
