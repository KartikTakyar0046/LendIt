# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-21 22:31
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='lendituser',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]
