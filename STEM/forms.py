from django import forms
from .models import Estudiante, Preguntas

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante

        fields = [
            'nombre',
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
            'nombre': 'Nombre',
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

class PreguntasForm(forms.ModelForm):
    class Meta:
        model = Preguntas

        fields = [
            'pregunta',
            'respuestac',
            'respuestaf1',
            'respuestaf2',
            'respuestaf3',
            'nivel',
            'area',
            'unidad',
        ]

        labels = {
            'pregunta': 'Ingrese pregunta',
            'respuestac': 'Ingrese respuesta correcta',
            'respuestaf1': 'Ingrese respuesta fallida 1',
            'respuestaf2': 'Ingrese respuesta fallida 2',
            'respuestaf3': 'Ingrese respuesta fallida 3',
            'nivel': 'Seleccione nivel de la pregunta',
            'area': 'Seleccione area',
            'unidad': 'Seleccione unidad',
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