# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0019_auto_20170316_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencia',
            name='titulo',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]