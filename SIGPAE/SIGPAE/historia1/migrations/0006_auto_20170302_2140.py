# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historia1', '0005_auto_20170302_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='asignatura',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='document',
            name='bibliografias',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='codigo',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='document',
            name='contenidos',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='creditos',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='departamento',
            field=models.CharField(choices=[('Ciencias Físicas y Matemáticas', ((1, 'Departamento de Física'), (2, 'Departamento de Química'), (3, 'Departamento de Mecánica'), (4, 'Departamento de Matemáticas Puras y Aplicadas'), (5, 'Departamento de Computación y Tecnología de la Información'), (6, 'Departamento de Cómputo Científico y Estadística'), (7, 'Departamento de Electrónica y Circuitos'), (8, 'Departamento de Termodinámica y Fenómenos de Transferencia'), (9, 'Departamento de Conversión y Transporte de Energía'), (10, 'Departamento de Procesos y Sistemas'), (11, 'Departamento de Ciencias de los Materiales'), (12, 'Departamento de Ciencias de la Tierra'))), ('Ciencias Sociales y Humanidades', ((13, 'Departamento de Ciencia y Tecnología del Comportamiento'), (14, 'Departamento de Lengua y Literatura'), (15, 'Departamento de Ciencias Económicas y Administrativas'), (16, 'Departamento de Idiomas'), (17, 'Departamento de Filosofía'), (18, 'Departamento de Ciencias Sociales'), (19, 'Departamento de Diseño Arquitectura y Artes Plásticas'), (20, 'Departamento de Planificación Urbana'))), ('Ciencias Biológicas', ((21, 'Departamento de Biología Celular'), (22, 'Departamento de Estudios Ambientales'), (23, 'Departamento de Biología de Organismos'), (24, 'Departamento de Tecnología de Procesos Biológicos y Bioquímicos'))), ('Ciencias y Tecnologías Administrativas e Industriales', ((25, 'Departamento de Tecnología de Servicios'), (26, 'Departamento de Tecnología Industrial'), (27, 'Departamento de Formación General y Ciencias Básicas'))), ('Decanato de Estudios Generales', ((28, 'Coordinación del Ciclo Básico'), (29, 'Coordinación del Ciclo Profesional'), (30, 'Coordinación de Formación General'), (31, 'Coordinación del Ciclo de Iniciación Universitaria'))), ('Decanato de Estudios Tecnológicos', ((47, 'Coordinación de Tecnología e Ingeniería Eléctrica'), (33, 'Coordinación de Tecnología Eléctrica y Electrónica'), (54, 'Coordinación de Ingeniería de Producción y Organización Empresarial'), (35, 'Coordinación de Turismo, Hotelería y Hospitalidad'), (36, 'Coordinación de Administración Aduanera'), (37, 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional'), (38, 'Coordinación de Administración del Transporte y Organización Empresarial'), (39, 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'))), ('Decanato de Estudios de Postgrado', ((40, 'Ciencias Básicas y Aplicadas'), (41, 'Ciencias Sociales y Humanidades'), (42, 'Ingeniería y Tecnología'))), ('Decanato de Estudios Profesionales', ((43, 'Coordinación de Química'), (44, 'Coordinación de Matemática'), (45, 'Coordinación de Biología'), (46, 'Coordinación de Física'), (47, 'Coordinación de Tecnología e Ingeniería Eléctrica'), (48, 'Coordinación de Tecnología e Ingeniería Electrónica'), (49, 'Coordinación de Ingeniería Mecánica'), (50, 'Coordinación de Ingeniería Química'), (51, 'Coordinación de Ingeniería de Computación'), (52, 'Coordinación de Ingeniería Geofísica'), (53, 'Coordinación de Ingeniería de Materiales'), (54, 'Coordinación de Ingeniería de Producción y Organización Empresarial'), (55, 'Coordinación de Tecnología Mecánica, Mantenimiento Aeronáutico e Ingeniería de Mantenimiento'), (56, ' Coordinación de Ingeniería de Telecomunicaciones'), (57, 'Coordinación de Arquitectura'), (58, 'Coordinación de Estudios Urbanos'), (59, 'Coordinación de Turismo, Hotelería y Hospitalidad'), (60, 'Coordinación de Comercio Exterior y Licenciatura en Comercio Internacional')))], default=12, max_length=2),
        ),
        migrations.AddField(
            model_name='document',
            name='evaluacion',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='horas_lab',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='horas_practica',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='horas_teoria',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='document',
            name='metodologias',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='objetivos',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='document',
            name='requisitos',
            field=models.TextField(blank=True),
        ),
    ]
