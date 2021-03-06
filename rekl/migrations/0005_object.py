# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-13 00:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekl', '0004_auto_20161113_0707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pi_address', models.CharField(max_length=100, unique=True)),
                ('pi_id', models.CharField(max_length=10, unique=True)),
                ('pi_ip', models.GenericIPAddressField(default='0.0.0.0', protocol='IPv4')),
                ('pi_alsa', models.IntegerField(default=0)),
                ('pi_mpc', models.IntegerField(default=0)),
                ('pi_mpg', models.IntegerField(default=0)),
                ('pi_tel', models.CharField(default='', max_length=50)),
                ('pi_comment', models.CharField(default='', max_length=200)),
                ('pi_roliks', models.ManyToManyField(to='rekl.Rolik')),
            ],
        ),
    ]
