from django.db import models
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


class Predecidos(models.Model):
    PAU1C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU1C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU1C = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU2C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU2C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU2C = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU3C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU3C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU3C = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU4C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU4C = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU4C = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])

    PAU1T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU1T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU1T = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU2T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU2T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU2T = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU3T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU3T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU3T = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU4T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU4T = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU4T = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])

    PAU1I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU1I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU1I = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU2I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU2I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU2I = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU3I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU3I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU3I = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU4I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU4I = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU4I = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])

    PAU1M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU1M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU1M = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU2M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU2M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU2M = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU3M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU3M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU3M = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    PAU4M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PFU4M = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(0)])
    PASOU4M = models.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])

    def get_api_url(self, request=None):
        return api_reverse("app-stem:predecidos-rud", kwargs={'pk': self.pk}, request=request)


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

#     preguntas acertadas unidad X de tema Y
#     preguntas fallidas unidad X de tema Y
#     paso unidad X de tema Y

#     https://docs.google.com/document/d/1rYzZNIRgBlw-0ianox3LxofiBUtU48KA6bxYbSynGDw/edit
