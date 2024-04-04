import csv 
import json
import io
import os

#Función para leer un csv para extraer los datos en un json.
def crear_json(csv_path, json_file):

#Diccionario donde se almacena la información extraida del csv
    datos = {}

#Extracción de datos del csv 
    with io.open(csv_path, encoding='utf-8') as csvf:
        pokemones = csv.DictReader(csvf)
        for i in pokemones:
            id = i['id']
            datos[id] = i
    #print("datos",datos)

#Escritura de datos en un archivo JSON    
    with io.open(json_file, 'w', encoding = "utf-8") as jsonf:
        jsonf.write(unicode(json.dumps(datos, indent=8)))

#Ligas de los archivos (Por si se quiere cambiar de dataset)
csvPath = r'/Users/nickvice/projectDjango/pokemon/miapp/Extra/pokemon_.csv'
jsonPath = r'/Users/nickvice/projectDjango/pokemon/miapp/Extra/poke.json'

crear_json(csvPath, jsonPath)
#Función que utilice para identificar el path de los archivos.
print(os.getcwd())
