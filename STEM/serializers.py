from rest_framework.serializers import ModelSerializer
from .models import Estudiante, Predecidos, Preguntas

class EstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'
        read_only_fields = ['id']

class PredecidosSerializer(ModelSerializer):
    class Meta:
        model = Predecidos
        fields = '__all__'
        read_only_fields = ['id']

class PreguntasSerializer(ModelSerializer):

    class Meta:
        model = Preguntas
        fields = '__all__'
        read_only_fields = ['id']