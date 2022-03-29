import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.1")
    
    def test_saldo_vahenee_kun_rahaa_on_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_saldo_ei_vahene_kun_raha_ei_riita(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), False)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")