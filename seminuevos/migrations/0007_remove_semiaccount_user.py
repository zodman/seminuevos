# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-06 23:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminuevos', '0006_semiaccount_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semiaccount',
            name='user',
        ),
    ]
