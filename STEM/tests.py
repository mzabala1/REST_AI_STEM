from django.test import TestCase
from .models import Estudiante, Predecidos
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

User = get_user_model()

class EstudiantesAPITestCase(APITestCase):
    def setUp(self):
        user = User(username='testcfeuser', email='test@stem.com')
        user.set_password("xpassword")
        user.save()
        estudiante1 = Estudiante.objects.create(genero="1", edad="2", grado="8", gpCiencia="2", gpTecnologia="2",
                                                gpIngenieria="3", gpMatematica="4", estrato="1", vcMadre="0",
                                                vcPadre="0", numHermanos="3")
    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = User.objects.count()
        self.assertEqual(post_count, 1)

    def test_get_item(self):
        data = {}
        url = api_reverse("app-stem:estudiante-list")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

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

        self.test_prediccion = Predecidos(PAU1C="2", PFU1C="0", PASOU1C="1", PAU2C="0", PFU2C="3",
                                          PASOU2C="0", PAU3C="3", PFU3C="1", PASOU3C="1", PAU4C="1",
                                          PFU4C="1", PASOU4C="0", PAU1T="2", PFU1T="0", PASOU1T="1",
                                          PAU2T="0", PFU2T="3", PASOU2T="0", PAU3T="3", PFU3T="1",
                                          PASOU3T="1", PAU4T="1", PFU4T="1", PASOU4T="0", PAU1I="2",
                                          PFU1I="0", PASOU1I="1", PAU2I="0", PFU2I="3", PASOU2I="0",
                                          PAU3I="3", PFU3I="1", PASOU3I="1", PAU4I="1", PFU4I="1",
                                          PASOU4I="0", PAU1M="2", PFU1M="0", PASOU1M="1", PAU2M="0",
                                          PFU2M="3", PASOU2M="0", PAU3M="3", PFU3M="1", PASOU3M="1",
                                          PAU4M="1", PFU4M="1", PASOU4M="0")
        self.test_prediccion.save()

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

    def test_verificar_PFU2C_pred(self):
        self.assertEquals(self.test_prediccion.PFU2C, "3")

    def test_verificar_PAU1T_pred(self):
        self.assertEquals(self.test_prediccion.PAU1T, "2")

    def test_verificar_PASOU2M_pred(self):
        self.assertEquals(self.test_prediccion.PASOU2M, "0")

    def test_get_by_id(self):
        self.assertEquals(Estudiante.get_by_id(4), self.test_estudiante1)

    def tearDown(self):
        self.test_estudiante1.delete()
        self.test_estudiante2.delete()
