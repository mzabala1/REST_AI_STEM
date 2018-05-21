from django import forms
from .models import Estudiante

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