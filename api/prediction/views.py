from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from joblib import dump, load
import json

pmsb = load('./models/pmsb.joblib')
nmsb= load('./models/nmsb.joblib')
LABELS = ['Inhalant','Canabis', 'Narcotique analgésique', 'Anesthésique dissociatif', 'Hallucinogène', 'Stimulant', 'Dépresseur', 'Alcool']
HIDDEN_LABELS = ['Pas Inhalant',
 'Pas Canabis',
 'Pas Narcotique analgésique',
 'Pas Anesthésique dissociatif',
 'Pas Hallucinogène',
 'Pas Stimulant',
 'Pas Dépresseur',
 'Pas Alcool']
def pencode(value):
  r = 0
  for i in range(len(LABELS)):
    if value[pmsb.keys()[i]] == 1:
      r = r + 2**(i)


  return r
def nencode(value):
  r = 0
  for i in range(len(HIDDEN_LABELS)):
    if value[nmsb.keys()[i]] == 1:
      r = r + 2**(i)
  return r
def pdecode(value):
  
  return bin(value)[0]+bin(value)[2:]

def pdecode_and_name(value):
    d = dict.fromkeys(LABELS,0)
    value = pdecode(value)
    for i in range(len(LABELS)):
      d[LABELS[i]] = int(value[i])
    return d
f_scaler = load('./models/scaler.joblib')
encodeurs = load('./models/encodeurs.joblib')
imputer = load('./models/imputer.joblib')
with open('./models/model_input_columns_name.txt', 'r') as f:
  f.seek(0)
  input_columns = f.read().split(',')
model = load('./models/model.joblib')


@api_view(['GET'])
def labels(request):
    return Response({ 'labels': LABELS, 'HIDDEN_LABELS': HIDDEN_LABELS })
@api_view(['GET'])
def columns(request):
    return Response({ 'columns': input_columns })

@api_view(['POST'])
def pencode_list(request):
    d =  {**request.data}
    for v in dict.keys(request.data):
       
       d[v] = int(d[v]) 
    return Response({ 'payload': d })

@api_view(['POST'])
def nencode_list(request):
    return Response(nencode(request.data))

@api_view(['POST'])
def pdecode_value(request):
    return Response(pdecode_and_name(int(request.data['payload'])))