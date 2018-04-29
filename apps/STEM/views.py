from django.shortcuts import render, redirect
# Create your views here.
from sklearn import tree

from .forms import EstudianteForm


def index(request):
    return render(request, 'estudiante/index.html')

def estudiante_view(request):
    form = EstudianteForm(request.POST)
    if form.is_valid():
        datos = form.cleaned_data
        genero = datos.get("genero")
        edad = datos.get("edad")
        grado = datos.get("grado")
        gpCiencia = datos.get("gpCiencia")
        gpTecnologia = datos.get("gpTecnologia")
        gpIngenieria = datos.get("gpIngenieria")
        gpMatematica = datos.get("gpMatematica")
        estrato = datos.get("estrato")
        vcMadre = datos.get("vcMadre")
        vcPadre = datos.get("vcPadre")
        numHermanos = datos.get("numHermanos")
        print("==================================================================================================================================================================================")
        print("Datos ingresados por el estudiante:")
        print(datos)
        print("==================================================================================================================================================================================")
        print("Resultados predecidos:")

        entrenar(x, y)
        print("El modelo ha sido entrenado")

        print("Presicion: ", probar(xp, yp))

        array = predecir([genero, edad, grado, gpCiencia, gpTecnologia, gpIngenieria, gpMatematica, estrato, vcMadre, vcPadre, numHermanos])
        print("Datos a predecir: ", [genero, edad, grado, gpCiencia, gpTecnologia, gpIngenieria, gpMatematica, estrato, vcMadre, vcPadre, numHermanos])
        print("Prediccion: ", array)

        print("Interpretación")
        interpretar(array)

        form.save()

    return render(request, 'estudiante/estudiante_form.html', {'form': form})

    # 	if request.method == 'POST':
    # 		form = EstudianteForm(request.POST)
    #
    # 		if form.is_valid():
    #         form.save()
    #     return redirect('index')
    # else:
    #     form = EstudianteForm()
    #
    #
    # return render(request, 'estudiante/estudiante_form.html', {'form': form})

# def prediccion_view(request):
# 	form_estudiante = EstudianteForm(request.POST)
# 	if form_estudiante.is_valid():
# 		datos = form_estudiante.cleaned_data
# 		genero = datos.get("genero")
# 		edad = datos.get("edad")
# 		grado = datos.get("grado")
# 		gpCiencia = datos.get("gpCiencia")
# 		gpTecnologia = datos.get("gpTecnologia")
# 		gpIngenieria = datos.get("gpIngenieria")
# 		gpMatematica = datos.get("gpMatematica")
# 		estrato = datos.get("estrato")
# 		vcMadre = datos.get("vcMadre")
# 		vcPadre = datos.get("vcPadre")
# 		numHermanos = datos.get("numHermanos")
#
# 		print genero
# 		print edad
# 		print vcPadre
# 		print gpMatematica


# 	return render(request, 'estudiante/estudiante.html', {'form': form})

x=[[1,2,9,1,2,3,2,2,1,0,1],[0,2,9,4,3,2,1,4,1,0,5],[1,3,9,2,4,2,1,2,1,0,2],
    [0,2,9,1,1,1,1,2,1,0,0],[0,3,9,3,1,2,4,3,1,1,0],[1,2,9,3,4,3,3,2,0,0,5],[1,2,9,4,3,1,2,2,0,1,1],
    [1,3,9,1,3,4,2,4,1,1,1],[1,2,9,3,1,2,4,3,1,1,2],[1,2,9,1,3,4,2,5,1,1,1],[0,3,9,4,2,2,1,4,1,0,1],
    [1,2,9,3,2,4,4,4,1,1,1],[0,3,9,2,4,4,1,3,1,0,1],[0,3,9,2,1,2,2,3,1,1,2],[1,2,9,1,2,3,2,2,1,0,1],
    [0,3,9,3,3,3,3,3,1,1,1],[1,2,9,3,3,1,1,3,1,1,2],[1,2,9,3,3,3,2,4,0,1,3],[1,3,9,2,1,4,4,3,1,0,3],
    [0,2,9,3,4,2,1,2,1,1,2],[0,2,9,3,4,3,2,3,1,1,2],[1,2,9,3,2,3,1,3,1,0,3],[1,2,9,2,1,3,3,3,1,1,1],
    [1,2,9,1,2,4,3,2,1,0,0],[0,2,10,3,4,4,4,3,1,0,2],[1,2,10,4,3,2,1,3,1,0,3],[0,3,10,2,4,4,3,2,1,1,3],
    [0,2,10,1,2,1,2,4,1,0,2],[0,2,10,1,4,4,1,2,1,0,2],[0,2,10,3,4,1,2,4,1,0,1],[0,2,10,2,4,3,4,4,0,1,1],
    [0,3,10,2,2,2,4,4,1,1,1],[0,2,10,3,3,2,3,2,1,1,1],[1,3,10,4,3,2,2,1,1,1,2],[0,3,10,3,4,3,2,3,1,1,1],
    [0,3,10,3,1,2,4,3,1,1,2],[0,3,10,4,4,4,4,3,1,1,2],[0,3,10,3,4,2,3,3,1,0,1],[1,2,10,3,4,4,3,2,1,0,4],
    [0,3,10,3,3,3,3,3,0,0,4],[0,3,10,1,1,1,1,4,1,1,0],[0,2,10,3,4,3,2,4,1,0,3],[0,2,10,1,4,3,4,2,1,1,2],
    [0,3,10,3,3,3,2,3,0,0,2],[0,2,10,1,4,3,4,4,1,1,2],[0,2,10,3,4,3,3,3,1,1,2],[0,2,10,3,4,2,3,2,1,1,2],
    [0,2,10,2,4,4,4,5,1,0,1],[0,2,10,3,4,4,3,2,1,1,0],[0,3,10,4,3,2,2,5,1,0,2],[1,2,10,2,3,4,1,4,1,1,0],
    [0,3,10,1,3,2,4,2,1,0,0],[1,3,10,1,3,4,2,3,1,0,1],[0,2,10,3,4,2,2,3,1,1,3],[1,1,6,1,2,1,2,2,1,1,2],
    [1,2,9,2,1,3,4,3,1,0,1],[1,2,9,4,1,2,4,2,1,1,1],[0,3,9,1,4,1,1,4,1,0,2],[1,2,9,3,2,1,1,2,0,0,2],
    [1,2,7,3,1,3,3,1,1,0,0],[1,2,9,2,3,2,1,2,1,0,1],[1,2,7,1,1,1,1,1,1,0,0],[1,2,10,2,3,2,3,3,1,1,1],
    [1,2,9,1,2,2,3,3,1,0,2],[1,3,11,2,3,2,2,2,0,0,2],[0,3,11,1,2,3,4,2,1,0,1],[0,3,11,3,4,4,3,3,1,0,2],
    [0,3,11,1,2,1,1,4,1,0,1]]

y=[[1,2,0,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,1,2,0,1,2,0,1,2,0,0,3,0,1,2,1,2,1,1,1,2,0],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,3,0,1,2,1,1,0,3,0,3,0,1,1,2,1,3,0,1,1,2,0],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,0,3,0,3,0,1,3,0,0,3,0,1,1,2,0],
    [2,1,1,3,0,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,2,1,1,1,2,0,1,2,0,1,2,0,2,1,1,2,1,1,1,2,0],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,0,3,0,3,0,1,3,0,1,2,1,1,3,0,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,2,1,1,1,2,0,1,2,0,1,2,1,3,0,1,1,2,0],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,1,2,0,2,1,1,2,1,1],
    [3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,1,2,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,1,2,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,0,3,0,1,3,0,1],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,0,1,2,0,1,2,1,3,0,1,2,1,1],
    [1,2,0,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,1,2,0,0,3,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,3,0,1,1,2,0,1,2,0,1,2,1,3,0,1,3,0,1],
    [3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,0,3,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [2,1,1,2,1,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,2,1,1,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,0,3,0],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,0,3,0,2,1,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,3,0,1,2,1,1,1,2,0,1,2,0,2,1,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1],
    [3,0,1,2,1,1,1,2,0,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,0,2,1,1,1,2,0,3,0,1,2,1,1,2,1,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,0,3,0,1,2,0,3,0,1,2,1,1,3,0,1],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,2,1,1,1,2,0],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,1,2,0,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,1,2,0,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,1,2,0],
    [3,0,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,1,2,0,3,0,1,1,2,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [3,0,1,3,0,1,1,2,0,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [1,2,0,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [1,2,0,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,0,3,0,3,0,1,3,0,1,2,1,1,1,2,0],
    [2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,0,3,0,2,1,1,1,2,0,1,2,0,3,0,1,2,1,1,1,2,0],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,1,2,0],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1],
    [2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,3,0,1],
    [2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,0,3,0,3,0,1,2,1,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,1,2,0,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,0,3,0,3,0,1,2,1,1,2,1,1,2,1,1],
    [2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,1,2,0,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,2,1,1],
    [0,3,0,2,1,1,1,2,0,2,1,1,3,0,1,1,2,0,2,1,1,1,2,0,2,1,1,2,1,1,2,1,1,1,2,0,1,2,0,2,1,1,2,1,1,1,2,0],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,0,2,1,1,1,2,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,0,3,0,2,1,1,2,1,0,3,0,1,3,0,1],
    [2,1,1,1,2,0,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,1,2,1,1,2,0,2,1,1],
    [3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,0,1,2,0,2,1,0,3,0,1,2,1,1],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,1,2,0],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,0,3,0,3,0,1,2,1,1,2,1,1,3,0,1],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,0,3,0,1,1,2,1,3,0,1,2,1,1],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,0,3,0,1,1,2,0],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,2,1,1,0,3,0,3,0,1,3,0,1,3,0,1,1,2,0],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,1,2,1,2,1,1,1,2,0],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,0,3,0,1,1,2,0],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,0,2,1,1,1,2,0]]

xp=[[0,3,11,4,3,2,3,4,1,1,1],[1,2,11,1,1,1,3,2,1,1,1],[0,2,11,4,4,4,4,3,0,0,0],[0,3,11,1,2,3,1,4,1,0,3],
    [0,2,11,3,3,3,4,4,1,1,1],[0,3,11,1,4,3,2,1,1,1,0],[0,3,11,3,4,4,3,3,1,1,1],[0,3,11,2,1,3,4,4,1,1,2],
    [0,3,11,2,1,3,4,4,1,1,0],[0,3,11,3,4,4,3,5,0,1,1],[0,3,11,4,4,4,4,5,1,1,1],[1,3,11,2,4,1,2,4,1,1,1],
    [1,3,11,4,4,1,3,4,1,1,1],[1,2,8,2,2,2,3,2,1,1,3],[1,1,6,1,3,2,4,1,0,1,2],[0,1,6,2,2,2,2,1,1,1,2],
    [1,3,11,1,1,3,2,3,1,0,2],[1,3,11,1,2,3,3,2,1,0,1],[1,3,11,3,2,3,1,3,1,0,2],[0,3,11,4,4,4,4,3,1,0,1],
    [1,1,6,1,4,3,2,4,1,1,3],[0,3,10,4,4,3,3,3,1,0,4],[0,3,11,3,4,4,3,3,1,0,2],[0,3,11,1,2,1,1,4,1,0,1],
    [1,3,11,2,3,2,2,2,0,0,2],[0,3,11,1,2,3,4,2,1,0,1]]

yp=[[2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,2,1,1,1,2,0],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0],
    [1,2,0,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,1,2,0,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1],
    [2,1,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,1,2,1,3,0,1,1,2,0],
    [3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,3,0,0,3,0,1,2,1,1],
    [2,1,1,2,1,1,0,3,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,0,3,0,2,1,1,2,1,1,1,2,0,2,1,1,1,2,0,2,1,1,2,1,1,0,3,0,1,2,0,1,2,0,1,2,1,2,1,1,1,2,0],
    [3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,1,2,0,2,1,1,0,3,0,3,0,1,2,1,1,1,2,0,0,3,0,1,2,0,2,1,0,0,3,0,2,1,1],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,3,0,1,2,1,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,0,3,0,3,0,1,3,0,1,1,2,0,0,3,0],
    [3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,1,2,0,2,1,1,2,1,1,3,0,1,2,1,1,1,2,0,0,3,0,1,2,0,3,0,1,0,3,0,2,1,1],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,2,1,1,2,1,1,2,1,1,2,1,1,3,0,1,1,2,0,2,1,1,2,1,1,2,1,0,1,2,0,0,3,0],
    [2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,1,2,0,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,1,2,1,3,0,1,2,1,1],
    [2,1,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,3,0,1,2,1,1,3,0,1,3,0,0,2,1,1,1,2,0],
    [2,1,1,2,1,1,1,2,0,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,1,2,0,3,0,1,1,2,1,2,1,1,1,2,0],
    [3,0,1,3,0,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,1,3,0,1,2,1,1,2,1,1,3,0,1,3,0,1,3,0,1,3,0,0,3,0,1,1,2,0]]

clasif = tree.DecisionTreeClassifier() #crea un variable con todos los atributos y metodos del arbol clasificador
z=['U1C','U2C','U3C','U4C','U1T','U2T','U3T','U4T','U1I','U2I','U3I','U4I','U1M','U2M','U3M','U4M']

# def cargarArchivos():
# 	entidad=[]
# 	atributos=[]
# 	with open(sys.argv[1]) as f:  #abre el archivo donde estan los 60 datos por estudiante
# 		for line in f:  # por cada iteracion carga en f linea a linea el archivo
# 			cont = 0
# 			temp = line.strip()  #quita especios adelante y atras de cada linea
# 			array = temp.split(',')  # separa la lina por ',' y cada uno de estas particiones las guarda como elementos en un arreglo
# 			entidad.append(array[0:11]) # toma los primeros datos los cuales corresponden a datos personales
# 			atributos.append(array[11:len(array)]) #toma los datos resptantes correspondientes al desempeno
# 	global clasif
# 	clasif= clasif.fit(entidad,atributos) # entrena el modelos con 2 matrices dadas (de 11 y 49 datos)
# 	imprimir()

def entrenar(entrada,salida):
    global clasif
    clasif= clasif.fit(entrada,salida) # entrena el modelos con 2 matrices dadas (de 11 y 49 datos)

def predecir(datoPredecir):
    global clasif
    return clasif.predict([datoPredecir]) #predice desempeno en base a un dato entrada

def interpretar(x):	#interpreta la prediccion obtenida, la resive como parametro
    i=2
    y=[]
    while i < len(x[0]):
        if x[0][i]> 0.0:
            y.append('-')
        else:
            y.append('Reforzar')
        i=i+3
    i=0
    while i < len(z):
        print (y[i],z[i])
        i=i+1

def probar(entrada,salida): #dadas 2 matrices (20% de los datos) prueba que tan preciso es el modelo
    i=0
    cantDatosIguales=0
    for dato in entrada:
        array=predecir(dato)
        cantDatosIguales=cantDatosIguales + probarIgualdad(array[0],salida[i])
        i=i+1
    size=len(salida)*48
    presicion=(cantDatosIguales+0.0)/(size+0.0)
    return presicion

def probarIgualdad(array1,array2): #este metodo sirve como apoyo al metodo probar compara 2 arrays
    cantDatosIgu=0
    i=0
    while i < len(array1):
        a=int(array1[i])
        b=int(array2[i])
        if a == b:
            cantDatosIgu=cantDatosIgu+1
        #else:
            #print(array1[i],array2[i])
        i=i+1
    return cantDatosIgu


# entrenar(x,y)
# print("modelo entrenado")
#
# print("presicion: ", probar(xp,yp))
#
# array=predecir([1,3,3,3,1,2,4,2,2,2,1])
# array=predecir([1,3,9,3,1,2,4,2,2,2,1])
# print("prediccion: ",array)
#
# print("interpretacion")
# interpretar(array)

# print("arbol")
# pr.imprimir()

#pr.entrenarR(x,y)

#array=pr.predecirR([1,2,9,4,1,2,4,2,1,1,1])
#print(array)
