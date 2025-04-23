##importar, utilizar 
# una dependencia en python

from flask import Flask, render_template

#crear la aplicacion 
# de flask 

app = Flask(__name__)

#utilizar app
#para crear una ruta 
@app.route('/prueba')
def prueba():
    #defino la lista de  paises 
    paises = [
        {
            'nombre': 'Argentina',
            'capital':'Buenos Aires',
            'moneda':'Peso argentino',
            'poblacion':'45.54',
            'superficie': '2.78',
            'ciudadesprincipales': [
                                    'rosario',
                                    'resistencia',
                                    'ciudad de corrientes',
                                    'ciudad de san luis'
                                    ]
        }, 
        {
            'nombre': 'Brasil',
            'capital':'Brasilia',
            'moneda':'real brasileño',
            'poblacion':'211.1',
            'superficie': '8.51',
            'ciudadesprincipales': [
                                    'rio de janeiro',
                                    'São Paulo'
                                    ]     
        },
         {
            'nombre': 'Colombia',
            'capital':'Bogota',
            'moneda':'Peso comlombiano',
            'poblacion':'52.32',
            'superficie': '1.142',
            'ciudadesprincipales': ['Medellin',
                                    'Barranquilla',
                                    'Cali'
                                    ]
        },
         {
            'nombre': 'Peru',
            'capital':'Lima',
            'moneda':'Sol peruano',
            'poblacion':'33.85',
            'superficie': '1.285',
            'ciudadesprincipales': [
                                    'Arequipa',
                                    'Cusco'
                                    ]                              
        },
    ]


    #envio la lista de paises 
    # a la vista 
    return render_template ('paises.html',
                     paises=paises,
                     usuario="Santiago")


