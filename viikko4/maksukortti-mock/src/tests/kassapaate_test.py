import unittest
from unittest.mock import Mock, ANY
from kassapaate import Kassapaate, HINTA
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()

    def test_kortilta_velotetaan_hinta_jos_rahaa_on(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 10

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_called_with(HINTA)

    def test_kortilta_ei_veloteta_jos_raha_ei_riita(self):
        maksukortti_mock = Mock()
        maksukortti_mock.saldo.return_value = 4

        self.kassa.osta_lounas(maksukortti_mock)

        maksukortti_mock.osta.assert_not_called()

    def test_lataa_positiivisella_luvulla_lataa_korttia(self):
        maksukortti_mock = Mock()
        summa = 74

        self.kassa.lataa(maksukortti_mock, summa)

        maksukortti_mock.lataa.assert_called_with(summa)

    def test_lataa_negativisella_luvulla_ei_tee_mitaan(self):
        maksukortti_mock = Mock()
        summa = -74

        self.kassa.lataa(maksukortti_mock, summa)

        maksukortti_mock.lataa.assert_not_called()
