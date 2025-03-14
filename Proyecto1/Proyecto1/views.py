from django.http import HttpResponse
import datetime
from django.template import Template,Context 

class Persona():

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo( request ):

    persona         = Persona("Profesor","Juan")
    fecha_actual    = datetime.datetime.now()

    temas_curso     = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    doc_externo = open("C:/Users/xavier.rocher/Documents/Software/Python/django/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    
    plt = Template( doc_externo.read() )
    doc_externo.close()

    ctx = Context(  { 
                        "nombre_persona"    : persona.nombre, 
                        "apellido_persona"  : persona.apellido, 
                        "momento_actual"    : fecha_actual,
                        "temas"             : temas_curso
                    } 
                  
                    )
    document0 = plt.render( ctx )
    
    return HttpResponse( document0 )


def despedida( request ):

    return HttpResponse( "Hasta luego!!")

def dameFecha( request ):
    
    fecha_actual = datetime.datetime.now()
    doc =   f"""
                <html>
                    <body>
                        <h1>Fecha y hora actual: {fecha_actual}</h1>
                    </body>
                </htnl>
            """
    return HttpResponse( doc )

def calculaEdad( request, edad,agno ):

    #edadActual  = 34
    periodo     = ( agno - 2025 )
    edadFutura  = edad + periodo

    doc =   f"""
                <html>
                    <body>
                        <h1>En el año {agno} tendras {edadFutura} años</h1>
                    </body>
                </htnl>
            """ 
    return HttpResponse( doc )