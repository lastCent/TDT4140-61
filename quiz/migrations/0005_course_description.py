# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-09 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20170308_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
