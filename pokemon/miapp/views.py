from django.shortcuts import render, HttpResponse 
from miapp.models import pokemon
import json 


# Create your views here.
#MVC = Modelo Vista Controlador -> Acciones (metodos)
#MVT = Modelo Template Vista -> Acciones (metodos)


#Request es un parametro para recibir datos de peticiones al URL
def hola_mundo(request):
    return HttpResponse("Hola mundo con Django")

def index(request): 
    return render(request, "index.html")

def pagina(request):
    return HttpResponse("""
        <h1> Pokemon </h1> 
    """)

def crear_pokemon(request):
    jsonPath = r'/Users/nickvice/projectDjango/pokemon/miapp/Extra/poke.json'
    with open(jsonPath) as json_file:
        datos = json.load(json_file)
    for i, data in datos.items():
        for j, k in data.items():
            id_p = int(data['species_id']),
            peso = int(data['weight']),
            nombre = data['identifier'],
            experiencia = int(data['base_experience'])
            
            new_pokemon = pokemon(id_pokemon=id_p, peso=peso, nombre=nombre, experiencia=experiencia)
            new_pokemon.save()

    return HttpResponse("Usuario creado:" )
