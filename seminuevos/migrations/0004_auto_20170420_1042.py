# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminuevos', '0003_remove_semiaccount_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='semiaccount',
            name='dealer_id',
            field=models.CharField(default=0, max_length=150, verbose_name='ID Dealer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='semiaccount',
            name='dealer_user_id',
            field=models.CharField(default=0, max_length=150, verbose_name='ID Dealer User'),
            preserve_default=False,
        ),
    ]