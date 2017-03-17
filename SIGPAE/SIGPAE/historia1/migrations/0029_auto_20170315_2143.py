# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 21:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0028_auto_20170315_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='guardar',
            field=models.CharField(choices=[('PASA', 'P.A.S.A.'), ('TRAN', 'Transcripción')], default='TRAN', max_length=4, verbose_name='Guardar como:'),
        ),
        migrations.AlterField(
            model_name='document',
            name='horas_lab',
            field=models.PositiveIntegerField(blank=True, verbose_name='Horas de Laboratorio'),
        ),
        migrations.AlterField(
            model_name='document',
            name='horas_practica',
            field=models.PositiveIntegerField(blank=True, verbose_name='Horas de Práctica'),
        ),
        migrations.AlterField(
            model_name='document',
            name='horas_teoria',
            field=models.PositiveIntegerField(blank=True, verbose_name='Horas de Teoría'),
        ),
    ]
