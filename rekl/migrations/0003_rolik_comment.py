# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekl', '0002_rolik_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolik',
            name='comment',
            field=models.CharField(default='', max_length=200),
        ),
    ]
