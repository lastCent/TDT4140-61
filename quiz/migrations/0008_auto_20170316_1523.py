# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20170315_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='resultVal',
            field=models.BooleanField(),
        ),
    ]
