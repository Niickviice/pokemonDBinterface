from django.shortcuts import render, HttpResponse 

# Create your views here.
#MVC = Modelo Vista Controlador -> Acciones (metodos)
#MVT = Modelo Template Vista -> Acciones (métodos)

layout = """
<h1> Sitio web con Django </h1>
"""

#Request es un parámetro para recibir datos de peticiones al URL
def hola_mundo(request):
    return HttpResponse(layout + "Hola mundo con Django")

def index(request): 
    return render(request, "index.html")

def pagina(request):
    return HttpResponse("""
        <h1> Pokemon </h1> 
    """)

