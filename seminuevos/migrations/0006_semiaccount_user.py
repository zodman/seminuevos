# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-01 23:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seminuevos', '0005_auto_20170825_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='semiaccount',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='semi_account', to=settings.AUTH_USER_MODEL, verbose_name='Cuenta de SEMI'),
            preserve_default=False,
        ),
    ]
