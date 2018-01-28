import os
os.system ('clear')

menu = """Superheroes V.0.0.1

1. Crea un nuevo Superhéroe
2. Muestra Superhéroes
3. Modificar Superhéroes
4. Eliminar Superhéroe

X. Salir """

print (menu)

while True:
    opcion = int(input("Selecciona una opción: "))
    heroe = []
    if opcion == 1:
        h = {'Nombre':'','Clase':'','Poder':'','Raza':''}
        h['Nombre'] = input("Ingresa el nombre del Superhéroe: ")
        h['Clase'] = input("Ingresa el tipo de Superhéroe: ")
        h['Poder'] = input("Ingresa el poder del Superhéroe: ")
        h['Raza'] = input("Ingresa la raza del Superhéroe: ")
        heroe.append(h)
        print (heroe)
    elif opcion == 2:
            print (h['Nombre'], h['Clase'], h['Poder'], h['Raza'])
    elif opcion == 3:
        #nombre = input("Ingresa el Nombre del Superhéroe:")
        print ("¿Qué quieres modificar de?")
        print ("""
        1. Nombre
        2. Clase
        3. Poder
        4. Raza """)
        opcion2 = int(input("Selecciona una opción: "))
        if opcion2 == 1:
            h['Nombre'] = input("Ingresa un nuevo nombre para este Superhéroe: ")
        elif opcion2 == 2:
            h['Clase'] = input("Ingresa una nueva clase para este Superhéroe: ")
        elif opcion2 == 3:
            h['Poder'] = input("Ingresa un nuevo poder para este Superhéroe: ")
        elif opcion2 == 4:
            h['Raza'] = input("Ingresa una nueva raza para este Superhéroe: ")
        else:
            print ("Error, ", opcion2)
    #elif (opcion == "X" or opcion =="x"):
    #    salir = input(("¿Estás seguro que quieres salir? S/n: ")
