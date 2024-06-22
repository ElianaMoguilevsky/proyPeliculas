import os
import json
import crud 
import utiles 

# inicializo la lista películas, después la voy a llenar con datos 
# traidos desde json
filePeli=open("peliculas.json","r")
# filePeli=open("proyPeliculas/peliculas.json","r")
peliculas = json.load(filePeli)

utiles.limpiarPantalla()
utiles.bienvenidaGrupo1()
utiles.limpiarPantalla()
utiles.mostrarTitulo("Bienvenidos a la página de películas", "*")

op=utiles.mostrarMenuIni()

while op!=0:
    if op==1:
        crud.listarPeliculas(peliculas)
    elif op==2:
        crud.addPelicula(peliculas)
    elif op==3:
        crud.modificarPeliculas(peliculas)
    elif op==4:
        crud.delPelicula(peliculas)
    elif op==5:
        crud.findPeliculas(peliculas)

    utiles.limpiarPantalla()
    op=utiles.mostrarMenuIni()

utiles.mostrarTitulo("Gracias por utilizar nuestra aplicación", "*")

filePeli.close()

