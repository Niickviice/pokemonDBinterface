import csv 
import json
import io
import os


def crear_json(csv_path, json_file):

    datos = {}

    with io.open(csv_path, encoding='utf-8') as csvf:
        pokemones = csv.DictReader(csvf)
        for i in pokemones:
            id = i['id']
            datos[id] = i
    #print("datos",datos)
    
    with io.open(json_file, 'w', encoding = "utf-8") as jsonf:
        jsonf.write(unicode(json.dumps(datos, indent=8)))

csvPath = r'/Users/nickvice/projectDjango/pokemon/miapp/Extra/pokemon_.csv'
jsonPath = r'/Users/nickvice/projectDjango/pokemon/miapp/Extra/poke.json'

crear_json(csvPath, jsonPath)
print(os.getcwd())
