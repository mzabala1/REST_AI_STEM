from django.test import TestCase
from .models import Estudiante

class test_estudiante(TestCase):

    def setUp(self):
        self.test_estudiante1 = Estudiante(genero="0", edad="2", grado="10", gpCiencia="1", gpTecnologia="2",
                                          gpIngenieria="3", gpMatematica="4", estrato="1", vcMadre="1", vcPadre="0",
                                          numHermanos="5")
        self.test_estudiante1.save()

        self.test_estudiante2 = Estudiante(genero="1", edad="1", grado="6", gpCiencia="1", gpTecnologia="2",
                                          gpIngenieria="4", gpMatematica="3", estrato="1", vcMadre="0", vcPadre="0",
                                          numHermanos="0")
        self.test_estudiante2.save()

    def test_verificar_genero_es1(self):
        self.assertEquals(self.test_estudiante1.genero, "0")

    def test_verificar_grado_es1(self):
        self.assertEquals(self.test_estudiante1.grado, "10")

    def test_verificar_vcMadre_es1(self):
        self.assertEquals(self.test_estudiante1.vcMadre, "1")

    def test_verificar_gpIngenieria_es2(self):
        self.assertEquals(self.test_estudiante2.gpIngenieria, "4")

    def test_verificar_vcPadre_es2(self):
        self.assertEquals(self.test_estudiante2.vcPadre, "0")

    def test_verificar_numHermanos_es2(self):
        self.assertEquals(self.test_estudiante2.numHermanos, "0")

    def test_get_by_id(self):
        self.assertEquals(Estudiante.get_by_id(1), self.test_estudiante1)

    def tearDown(self):
        self.test_estudiante1.delete()
        self.test_estudiante2.delete()
