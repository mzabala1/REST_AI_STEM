from django import forms
from .models import Estudiante
from django.core.validators import MaxValueValidator, MinValueValidator

BOOL_CHOICES = ('0', '1')

class EstudianteForm(forms.ModelForm):

    class Meta:
        model = Estudiante

        fields = [
            'genero',
            'edad',
            'grado',
            'gpCiencia',
            'gpTecnologia',
            'gpIngenieria',
            'gpMatematica',
            'estrato',
            'vcMadre',
            'vcPadre',
            'numHermanos',
        ]

        labels = {
            'genero': 'Genero',
            'edad': 'Edad',
            'grado': 'Grado',
            'gpCiencia' : 'Gusto por la ciencia',
            'gpTecnologia': 'Gusto por la tecnología',
            'gpIngenieria': 'Gusto por la ingeniería',
            'gpMatematica': 'Gusto por la matemática',
            'estrato': 'Estrato',
            'vcMadre': 'Vive con la madre',
            'vcPadre': 'Vive con el padre',
            'numHermanos': 'Número de herman@s',
        }

        # widgets = {
        #     'genero': forms.CheckboxSelectMultiple(),
        #     'edad': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'grado':forms.NumberInput(attrs={'class': 'form-control'}),
        #     'gpCiencia': forms.CheckboxSelectMultiple(),
        #     'gpTecnologia': forms.CheckboxSelectMultiple(),
        #     'gpIngenieria': forms.CheckboxSelectMultiple(),
        #     'gpMatematica': forms.CheckboxSelectMultiple(),
        #     'estrato': forms.CheckboxSelectMultiple(),
        #     'vcMadre': forms.CheckboxSelectMultiple(),
        #     'vcPadre': forms.CheckboxSelectMultiple(),
        #     'numHermanos': forms.CheckboxSelectMultiple(),
        # }

    #para posterior uso en caso de querer modificar widgets
    # genero = models.BooleanField()
    # edad = models.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(1)])
    # grado = models.IntegerField(validators=[MaxValueValidator(11),MinValueValidator(6)])
    # gpCiencia = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpTecnologia = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpIngenieria = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpMatematica = models.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # estrato = models.IntegerField(validators=[MaxValueValidator(6),MinValueValidator(0)])
    # vcMadre = models.BooleanField()
    # vcPadre = models.BooleanField()
    # numHermanos = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
