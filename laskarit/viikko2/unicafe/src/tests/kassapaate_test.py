import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_luodun_paatteen_raha_ja_myydyt_lounaat_oikeat(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_edullinen_kateisosto_toimii_edullinen_kun_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(480), 240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_kateisosto_ei_onnistu_kun_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(230), 230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_maukas_kateisosto_toimii_edullinen_kun_rahaa_tarpeeksi(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(800), 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_kateisosto_ei_onnistu_kun_raha_ei_riita(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(390), 390)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_edullinen_korttiosto_onnistuu_kun_rahaa_tarpeeksi(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 7.6")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_edullinen_korttiosto_ei_onnistu_kun_raha_ei_riita(self):
        kortti = Maksukortti(230)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 2.3")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        
    def test_maukas_korttiosto_onnistuu_kun_rahaa_tarpeeksi(self):
        kortti = Maksukortti(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
        self.assertEqual(str(kortti), "saldo: 6.0")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_maukas_korttiosto_ei_onnistu_kun_raha_ei_riita(self):
        kortti = Maksukortti(390)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(str(kortti), "saldo: 3.9")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_kortin_lataus_toimii(self):
        kortti = Maksukortti(10)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(str(kortti), "saldo: 1.1")
    
    def test_kortin_lataus_ei_hyvaksy_negatiivista(self):
        kortti = Maksukortti(10)
        self.kassapaate.lataa_rahaa_kortille(kortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(str(kortti), "saldo: 0.1")