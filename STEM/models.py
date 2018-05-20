from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework.reverse import reverse as api_reverse

class Estudiante(models.Model):
    genero = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    edad = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(1)])
    grado = models.IntegerField(validators=[MaxValueValidator(11),MinValueValidator(6)])
    gpCiencia = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    gpTecnologia = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    gpIngenieria = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    gpMatematica = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    estrato = models.IntegerField(validators=[MaxValueValidator(6),MinValueValidator(0)])
    vcMadre = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    vcPadre = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    numHermanos = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])


    @classmethod
    def get_by_id(cls, uid):
        return Estudiante.objects.get(pk=uid)

    def get_api_url(self, request=None):
        return api_reverse("app-stem:estudiante-rud", kwargs={'pk': self.pk}, request=request)

#     genero 0=hombre 1=mujer
#     edad = 1=5-10años 2=10-15 3=15-20
#     grado = 6,7,8,9,10,11
#     gusto por ciencia= 1,2,3,4
#     gusto por tecnologia= 1,2,3,4
#     gusto por ingenieria= 1,2,3,4
#     gusto por matematica= 1,2,3,4
#     estrato = 0,1,2,3,4,5,6
#     vive con madre = 0=no 1=si
#     vive con papa = 0=no 1=si
#     cantidad de hermanos = 0 a 5
#
#     preguntas acertadas un1 mod ciencia =  0 a 3
#     preguntas perdidas un1 mod ciencia = 0 a 3
#     paso un1 mod ciencia = 0, no paso=1
#
#     un1 mod ciencia
#     un2 mod ciencia
#     un3 mod ciencia
#     un4 mod ciencia
#     un1 mod tecnologia
#     un2 mod tecnologia
#     un3 mod tecnologia
#     un4 mod tecnologia
#     un1 mod ing
#     un2 mod ing
#     un3 mod ing
#     un4 mod ing
#     un1 mod matematicas
#     un2 mod matematicas
#     un3 mod matematicas
#     un4 mod matematicas

#     https://docs.google.com/document/d/1rYzZNIRgBlw-0ianox3LxofiBUtU48KA6bxYbSynGDw/edit
