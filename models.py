from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    asignatura= models.CharField(max_length=255,blank=True)
    codigo= models.CharField(max_length=10,blank=True)
    creditos= models.PositiveIntegerField(blank=True,null=True)
    requisitos= models.TextField(blank=True)
    objetivos= models.TextField(blank=True)
    contenidos= models.TextField(blank=True)
    metodologias=models.TextField(blank=True)
    evaluacion=models.TextField(blank=True)
    bibliografias=models.TextField(blank=True)
    horas_teoria=models.PositiveIntegerField(blank=True,null=True)
    fecha= models.DateField(blank=True,null=True)
    horas_lab=models.PositiveIntegerField(blank=True,null=True)
    horas_practica=models.PositiveIntegerField(blank=True,null=True)

    def __str__(self):
    	return self.name
