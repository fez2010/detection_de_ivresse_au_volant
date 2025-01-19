from django.test import TestCase
from django.conf import settings
from django.test import Client
from api import settings as s
import django
import json


LABELS = ['Inhalant','Canabis', 'Narcotique analgésique', 'Anesthésique dissociatif', 'Hallucinogène', 'Stimulant', 'Dépresseur', 'Alcool']
HIDDEN_LABELS = [
 'Pas Inhalant',
 'Pas Canabis',
 'Pas Narcotique analgésique',
 'Pas Anesthésique dissociatif',
 'Pas Hallucinogène',
 'Pas Stimulant',
 'Pas Dépresseur',
 'Pas Alcool'
]

with open('./models/model_input_columns_name.txt', 'r') as f:
  f.seek(0)
  input_columns = f.read().split(',')
data = {
 'Reaction lum': 1.0,
 'Depot pied': 1.0,
 'Sautillement': 0.0,
 'Bras': 0.0,
 'Balancement': 0.0,
 'Equi d': 19.0,
 'Equi g': 33.0,
 'Pas 2': 9.0,
 'Pas 1': 9.0,
 'Pivot incorrect': 1.0,
 'Utilisation bras': 0.0,
 'Pas hors ligne': 0.0,
 'Talon/orteille': 1.0,
 'Depart hatif': 0.0,
 'Larmoyant': 0.0,
 'Conjonctive rouge': 0.0,
 'Injecté sang': 1.0,
 'Yeux normaux': 0.0,
 'Ambiant': 6.5,
 'Noirceur': 6.5,
 'Direct': 4.5,
 'Dilatation bond': 1.0,
 'Romberg 1': 0.0,
 'Romberg 2': 0.0,
 'Romberg 3': 10.0,
 'Température': 36.6,
 'Tension a': 170.0,
 'Tension b': 100.0,
 'Test toucher': 4.0,
 'Tonus musculaire': 0.0,
 'Paupieres': 0.0,
 'Pupilles': 0.0,
 'Perte equilibre': 1.0,
 'Pouls': 106.0,
 'Injection': 0.0,
 'Nistagmus horizontal': 0.0,
 'Nistagmus vertical': 0.0,
 'Convergence': 1.0
}

label = {
 'Inhalant': 0,
 'Canabis': 1,
 'Narcotique analgésique': 0,
 'Anesthésique dissociatif': 0,
 'Hallucinogène': 0,
 'Stimulant': 0,
 'Dépresseur': 0,
 'Alcool': 1
}
class ApiTestCase(TestCase):
    client = None
    def setUp(self):
        self.client = Client()

    def test_labels(self):
        """Label list"""
        response = self.client.get("/api/labels/")

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.content), { 'labels': LABELS, 'HIDDEN_LABELS': HIDDEN_LABELS })
    
    def test_columns(self):
        """Column List"""
        response = self.client.get("/api/columns/")
        
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(json.loads(response.content), { 'columns': input_columns })
    def test_pencode(self):
        """pencode"""
        response = self.client.post("/api/pencode/",label)
        self.assertEqual(int(response.content),  66 )
    #def test_nencode(self):
    #    """Nencode"""
    #    response = self.client.post("/api/nencode/",{ 'payload': 66 })
    #     self.assertDictEqual(json.loads(response.content), label)
    def test_pdecode(self):
        """Nencode"""
        response = self.client.post("/api/pdecode/",{ 'payload': 66 })
        
        
        self.assertDictEqual(json.loads(response.content), label)