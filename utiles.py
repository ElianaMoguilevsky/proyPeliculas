import os
anchoPantalla=os.get_terminal_size()

def bienvenidaGrupo1():
    print("¡Bienvenido a nuestro sistema!")
    print("")
    print("   _________________")
    print(" /                   \\")
    print("|   ¡Realizado en    |")
    print("|       Python!      |")
    print(" \\__________________/")
    print("        |     |")
    print("        |     |")
    print("        |     |")
    print("        |_____|")

    print("")
    print("                  _   _   _   _   _   _   _   _   _  ")                
    print("                 / \ / \ / \ / \ / \ / \ / \ / \ / \----------------------------------------> ********") 
    print("                - G   R   U   P   O       U   N   O ---------------------------------------->  ****** ")
    print("                 \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                                             ***  ")
    print("                                                                                                  V"   )


    print("                           ─────▄▀▀▄──────────")
    print("                           ─────█──█▄▄────────")
    print("                           ─────█──█──█▀▀▄▄───")
    print("                           ─▄▄▄─█──█──█──█─▀▄─            ----------   INTEGRANTES ------------------")                           
    print("                           ─█──▀█────────▀──█─            -         *  Miriam     Sivira              ")
    print("                           ──▀▄─█───────────█─            -         *  Daniela 	  Blasco              ")
    print("                           ───▀▄───────────█──            -         *  Eliana     Moguilevsky         ")
    print("                           ────▀▄──────────█──            -         *  Hernan     Valatkevicnis       ")
    print("                           ─────▀▄────────█───            -         *  Alejandro  Natera              ")
    print("                           ──────█▄▄▄▄▄▄▄▄█───             -------------------------------------------")

    print("")
    input("Presione enter para continuar")

def mostrarTitulo(titulo, carRelleno):
    print(carRelleno.center(anchoPantalla.columns,carRelleno))
    print(titulo.center(anchoPantalla.columns," "))
    print(carRelleno.center(anchoPantalla.columns,carRelleno))

def mostrarSubTitulo(subtitulo, carRelleno):
    print(subtitulo.center(anchoPantalla.columns,carRelleno))

def mostrarFinFuncion():
    print("")
    print("-".center(anchoPantalla.columns,"-"))
    input("Presione enter para continuar")

def mostrarLinea():
    print("")
    print("-".center(anchoPantalla.columns,"-"))

def limpiarPantalla():
    os.system("cls")  


def mostrarMenuIni():
    print("Elija alguna opción: 1,2,3,4 o 0 para salir")
    print("1- Listar películas")
    print("2- Agregar película")
    print("3- Modificar película")
    print("4- Eliminar película")
    print("5- Buscar pelicula")
    print("0- Salir")

    # el usuario ingresa la opción desada
    opcion=int(input("Ingrese alguna opción: "))
    
    return opcion

def mostrarMenuBusqueda():
    print("Elija el número del campo por el que desea realizar la búsqueda: ")
    print("1- Título")
    print("2- Título original")
    print("3- Director")
    print("4- Actor o Actriz")
    print("5- Género")
    print("0- Volver al menú anterior")

    # el usuario ingresa la opción desada
    opcion=int(input("Ingrese alguna opción: "))
    
    return opcion