# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0022_auto_20170315_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camposextra',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='camposextra',
            name='value',
            field=models.TextField(verbose_name='Texto'),
        ),
    ]
