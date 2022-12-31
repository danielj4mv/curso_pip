import requests # Para hacer peticiones a una api


def get_categories():
    """Para Hacer un request de las categorias de la api
    """
    r=requests.get('https://api.escuelajs.co/api/v1/categories') #Hacer una petición a la api
    print(r.status_code) # Ver el estado de la información
    print(r.text) # Ver que retorna la api en formato string
    categories=r.json() # Convierte el contendido de la petición de JSON a objetos de python (listas, diccionarios)
    
    for category in categories:
        print(category['name']) # Imprimimos los nombres de cada categoria