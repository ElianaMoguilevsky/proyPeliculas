import utiles
import json
import os

anchoPantalla=os.get_terminal_size()

"""Función que lista todas las películas que dispone la aplicación"""
def listarPeliculas(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Listado de Películas", "-")
    print(" ")

    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Pos |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
   
    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)

    for i, peli in enumerate(peliculas):
        print(f'| {str(i+1):4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')

    utiles.mostrarFinFuncion()



"""Agrega una película a la lista de disponibles"""
def addPelicula(peliculas):
     # limpio pantalla y muestro título
    utiles.limpiarPantalla()

    utiles.mostrarSubTitulo("Agregar una Película", "-")

    ultimoId = peliculas[len(peliculas)-1]["id"] # último ID ingresado
    nuevoId = ultimoId + 1

    # el usuario ingresa el nombre de la peli para agregar a la lista
    titulo=input("Ingrese el nombre de la película: ")
    titulo_original=input("Ingrese el titulo en idioma original: ")
    director=input("Ingrese el nombre del director: ")
    puntuacion=input("Ingrese la puntuacion: ")
    genero=input("Ingrese el género: ")
    anio=input("Ingrese el año: ")
    sinopsis=input("Ingrese la sinopsis: ")
    actores=input("Ingrese los actores: ")
    duracion=input("Ingrese la duracion: ")

    #nueva pelicula a agregar
    nueva_pelicula = {
    "id": nuevoId,
    "titulo": titulo,
    "titulo_original": titulo_original,
    "director": director,
    "puntuacion": puntuacion,
    "genero": genero,
    "anio": anio,
    "sinopsis": sinopsis,
    "actores": actores,
    "duracion": duracion
}
    
    # agrega la pelicula recien ingresada a la lista películas
    peliculas.append(nueva_pelicula)
    fileToSave=open("peliculas.json","w")
    json.dump(peliculas, fileToSave)
    fileToSave.close()
    
    print("Su película fue agregada con éxito")

    utiles.mostrarFinFuncion()



"""Elimina una película a la lista de disponibles
    Al usuario se le muestra la lista de películas
    y luego decide cual eliminar.
    El usuario puede eliminar una película por su número
    o por su nombre.
"""
def delPelicula(peliculas):
     # limpio pantalla y muestro título
    utiles.limpiarPantalla()

    utiles.mostrarSubTitulo("Eliminar una Película", "-")

    # muestro todas las películas
    listarPeliculas(peliculas)

    utiles.mostrarLinea()
    
    # guarda la nueva lista con el elemento eliminado
    indice=int(input("Ingrese el número de la película a eliminar: "))
    pelEliminada=peliculas.pop(indice-1)
    fileToSave=open("peliculas.json","w")
    json.dump(peliculas, fileToSave)
    fileToSave.close()

    print(f'Se eliminó exitosamente la película {pelEliminada["titulo"]}')
    
    utiles.mostrarFinFuncion()

"""Modifica una película de la lista 
    Al usuario se le muestra la lista de películas
    y luego decide cual modificar.
"""

def modificarPeliculas(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Listado de Películas", "-")

    # listo peliculas existentes
    listarPeliculas(peliculas)

    utiles.mostrarFinFuncion()

    #selecciona y modifica el item de la lista
    indice=int(input("Ingrese el número de la película a modificar: "))
    peli=input("Ingrese nuevamente el nombre de la película: ")
    peliculas[indice-1]=peli
    fileToSave=open("peliculas.json","w")
    json.dump(peliculas, fileToSave)
    fileToSave.close()

    print("")
    print("Su película fue modificada con éxito")
    print("")

  # listo nuevamente peliculas existentes
    listarPeliculas(peliculas) 
    
    utiles.mostrarFinFuncion()
    
"""Función que busca películas por algún campo"""
def findPeliculas(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")
    
    op=utiles.mostrarMenuBusqueda()

    while op!=0:
        if op==1:
            findPeliculasPorTitulo(peliculas)
        elif op==2:
            findPeliculasPorTituloOriginal(peliculas)
        elif op==3:
            findPeliculasPorDirector(peliculas)
        elif op==4:
            findPeliculasPorActor(peliculas)
        elif op==5:
            findPeliculasPorGenero(peliculas)

    op=utiles.mostrarMenuBusqueda()            

    if op==0:
        utiles.limpiarPantalla()
        utiles.mostrarTitulo("Bienvenidos a la página de películas", "*")
        utiles.mostrarMenuIni()     
   
def findPeliculasPorTitulo(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")
   
    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)
   
    print("")
    print("Búsqueda de película por título")
    utiles.mostrarLinea()
   
    campo_a_buscar=(input("Ingrese el texto buscado: ").lower())
    peliEncontrada=False
    cont=0
    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Id  |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
    for peli in peliculas:
        if campo_a_buscar in peli["titulo"].lower():
            peliEncontrada=True
            cont+=1
            print(f'| {peli["id"]:4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')
            if peliEncontrada==False:
               print(f'Pelicula con título original"{campo_a_buscar}" no encontrada')
    
    print("")
    print("-"*55) 
    print(f'Cantidad de coincidencias con el texto buscado: {cont}')
    print("-"*55)   
          
    utiles.mostrarFinFuncion()
    utiles.limpiarPantalla()
    utiles.mostrarMenuBusqueda()

def findPeliculasPorTituloOriginal(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")
   
    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)
   
    print("")
    print("Búsqueda de película por título original")
    utiles.mostrarLinea()
   
    campo_a_buscar=(input("Ingrese el texto buscado: ").lower())
    peliEncontrada=False
    cont=0
    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Id  |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
    for peli in peliculas:
        if campo_a_buscar in peli["titulo_original"].lower():
            peliEncontrada=True
            cont+=1
            print(f'| {peli["id"]:4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')
            if peliEncontrada==False:
               print(f'Pelicula con título original "{campo_a_buscar}" no encontrada')
    
    print("")
    print("-"*55) 
    print(f'Cantidad de coincidencias con el texto buscado: {cont}')
    print("-"*55)   
          
    utiles.mostrarFinFuncion()
    utiles.limpiarPantalla()
    utiles.mostrarMenuBusqueda()

def findPeliculasPorDirector(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")

    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)
   
    print("")
    print("Búsqueda de película por director")
    utiles.mostrarLinea()
   
    campo_a_buscar=(input("Ingrese el texto buscado: ").lower())
    peliEncontrada=False
    cont=0
    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Id  |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
    for peli in peliculas:
        if campo_a_buscar in peli["director"].lower():
            peliEncontrada=True
            cont+=1
            print(f'| {peli["id"]:4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')
            if peliEncontrada==False:
               print(f'Pelicula con director "{campo_a_buscar}" no encontrada')
    
    print("")
    print("-"*55) 
    print(f'Cantidad de coincidencias con el texto buscado: {cont}')
    print("-"*55)   
          
    utiles.mostrarFinFuncion()
    utiles.limpiarPantalla()
    utiles.mostrarMenuBusqueda()
    
def findPeliculasPorActor(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")

    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)
   
    print("")
    print("Búsqueda de película por actor o actriz")
    utiles.mostrarLinea()
   
    campo_a_buscar=(input("Ingrese el texto buscado: ").lower())
    peliEncontrada=False
    cont=0
    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Id  |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
    for peli in peliculas:
        actores_minusculas = [actor.lower() for actor in peli["actores"]]
        if campo_a_buscar in actores_minusculas:
            peliEncontrada=True
            cont+=1
            print(f'| {peli["id"]:4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')
            if peliEncontrada==False:
               print(f'Pelicula con director "{campo_a_buscar}" no encontrada')
    
    print("")
    print("-"*55) 
    print(f'Cantidad de coincidencias con el texto buscado: {cont}')
    print("-"*55)   
          
    utiles.mostrarFinFuncion()
    utiles.limpiarPantalla()
    utiles.mostrarMenuBusqueda()

def findPeliculasPorGenero(peliculas):
    # limpio pantalla y muestro título
    utiles.limpiarPantalla()
    utiles.mostrarSubTitulo("Buscar Películas", "-")

    max_ancho_titulo = max(len(peli["titulo"]) for peli in peliculas)
    max_ancho_director = max(len(peli["director"]) for peli in peliculas)
   
    print("")
    print("Búsqueda de película por género")
    utiles.mostrarLinea()
   
    campo_a_buscar=(input("Ingrese el texto buscado: ").lower())
    peliEncontrada=False
    cont=0
    print("+------+-----------------------+------------+-------+--------------------+")
    print("|  Id  |        Titulo         | Puntuación |  Año  |      Director      |")
    print("+------+-----------------------+------------+-------+--------------------+")
    for peli in peliculas:
        genero_minusculas = [genero.lower() for genero in peli["genero"]]
        if campo_a_buscar in genero_minusculas:
            peliEncontrada=True
            cont+=1
            print(f'| {peli["id"]:4} | {peli["titulo"]:{max_ancho_titulo}} | {peli["puntuacion"]:10} | {peli["anio"]:10} | {peli["director"]:{max_ancho_director}} |')
            if peliEncontrada==False:
               print(f'Pelicula de género "{campo_a_buscar}" no encontrada')
    
    print("")
    print("-"*55) 
    print(f'Cantidad de coincidencias con el texto buscado: {cont}')
    print("-"*55)   
          
    utiles.mostrarFinFuncion()
    utiles.limpiarPantalla()
    utiles.mostrarMenuBusqueda()