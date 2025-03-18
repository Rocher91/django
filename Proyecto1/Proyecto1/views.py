from django.http import HttpResponse
import datetime
from django.template import Template,Context 
from django.template import loader 
from django.shortcuts import render

class Persona():

    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

def saludo( request ):

    persona         = Persona("Profesor","Juan")
    fecha_actual    = datetime.datetime.now()

    temas_curso     = ["Plantillas","Modelos","Formularios","Vistas","Despliegue"]
    #doc_externo = open("C:/Users/Xavi/Documents/SW/Python/django/Proyecto1/Proyecto1/plantillas/mi_plantilla.html")
    
    #plt = Template( doc_externo.read() )
    #doc_externo.close()

    #doc_externo = loader.get_template('mi_plantilla.html')

    """
    ctx = Context(  { 
                        "nombre_persona"    : persona.nombre, 
                        "apellido_persona"  : persona.apellido, 
                        "momento_actual"    : fecha_actual,
                        "temas"             : temas_curso
                    } 
                  
                    )
    """
    dictionary =    { 
                        "nombre_persona"    : persona.nombre, 
                        "apellido_persona"  : persona.apellido, 
                        "momento_actual"    : fecha_actual,
                        "temas"             : temas_curso
                    } 
                  
                    
    #document0 = plt.render( ctx )
    #documento = doc_externo.render( dictionary )

    
    return render( request, "mi_plantilla.html", dictionary )

def CursoC ( request ):

    fecha_actual = datetime.datetime.now()

    return render( request, "CursoC.html",{"dameFecha" : fecha_actual})

def CursoCSS ( request ):

    return render( request, "CursoCSS.html")

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