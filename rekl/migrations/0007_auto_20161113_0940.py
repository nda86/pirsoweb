# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekl', '0006_auto_20161113_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='pi_comment',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AlterField(
            model_name='object',
            name='pi_tel',
            field=models.CharField(default='-', max_length=50),
        ),
        migrations.AlterField(
            model_name='rolik',
            name='comment',
            field=models.CharField(default='-', max_length=200),
        ),
    ]
