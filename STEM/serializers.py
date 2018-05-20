from rest_framework.serializers import ModelSerializer
from .models import Estudiante

class EstudianteSerializer(ModelSerializer):

    class Meta:
        model = Estudiante
        fields = '__all__'
        read_only_fields = ['id']

    # pk = serializers.IntegerField(read_only=True)
    # genero = serializers.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    # edad = serializers.IntegerField(validators=[MaxValueValidator(3),MinValueValidator(1)])
    # grado = serializers.IntegerField(validators=[MaxValueValidator(11),MinValueValidator(6)])
    # gpCiencia = serializers.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpTecnologia = serializers.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpIngenieria = serializers.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # gpMatematica = serializers.IntegerField(validators=[MaxValueValidator(4),MinValueValidator(1)])
    # estrato = serializers.IntegerField(validators=[MaxValueValidator(6),MinValueValidator(0)])
    # vcMadre = serializers.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    # vcPadre = serializers.IntegerField(validators=[MaxValueValidator(1),MinValueValidator(0)])
    # numHermanos = serializers.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])

    # def create(self, validated_data):
    #     return Serie.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     instance.datos = validated_data.get('datos', instance.datos)
    #     instance.genero = validated_data.get('genero', instance.genero)
    #     instance.edad = validated_data.get('edad', instance.edad)
    #     instance.grado = validated_data.get('grado', instance.grado)
    #     instance.gpCiencia = validated_data.get('gpCiencia', instance.gpCiencia)
    #     instance.gpTecnologia = validated_data.get('gpTecnologia', instance.gpTecnologia)
    #     instance.gpIngenieria = validated_data.get('gpIngenieria', instance.gpIngenieria)
    #     instance.gpMatematica = validated_data.get('gpMatematica', instance.gpMatematica)
    #     instance.estrato = validated_data.get('estrato', instance.estrato)
    #     instance.vcMadre = validated_data.get('vcMadre', instance.vcMadre)
    #     instance.vcPadre = validated_data.get('vcPadre', instance.vcPadre)
    #     instance.numHermanos = validated_data.get('numHermanos', instance.numHermanos)

    #     instance.save()
    #     return instance
