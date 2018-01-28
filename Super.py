import os
os.system ('clear')

menu = """Superheroes V.0.0.1

1. Crea un nuevo Superhéroe
2. Muestra Superhéroes
3. Modificar Superhéroes
4. Eliminar Superhéroe

M. Menú
Q. Salir """

print (menu)
heroe = []

while True:
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        cantidad = int(input("Cuántos Superhéroes?: "))
        os.system ('clear')
        print ("Elegiste crear ",cantidad, " Superhéroes\n")
        for h in range(cantidad):
            h = {'Nombre':'','Clase':'','Poder':'','Raza':''}
            h['Nombre'] = input("Ingresa el nombre del Superhéroe: ")
            h['Clase'] = input("Ingresa el tipo de Superhéroe: ")
            h['Poder'] = input("Ingresa el poder del Superhéroe: ")
            h['Raza'] = input("Ingresa la raza del Superhéroe: ")
            heroe.append(h)
            os.system ('clear')
            print ("Elige el siguiente Superhéroe\n")
        print (heroe)
    elif opcion == "2":
        for h in heroe:
            print ("-->Nombre: ", h['Nombre'], "-->Clase: ", h['Clase'], "-->Poder: ", h['Poder'], "-->Raza: ", h['Raza'])
    elif opcion == "3":

        print ("""¿Qué quieres modificar de?
        1. Nombre
        2. Clase
        3. Poder
        4. Raza

        Q. Cancelar""")
        for i,h in enumerate(heroe):
            opcion2 = input("Selecciona una opcion: ")
            while True:

                if opcion2 == "1":
                    nombre = input("Escribe el nombre del Superhéroe: ")
                    if h['Nombre'] == nombre:
                        heroe[i]['Nombre'] = input("Ingresa un nuevo nombre para el Superhéroe: ")
                        #opcion2 = input("Selecciona una opcion: ")
                elif opcion2 == "2":
                    clase = input("Escribe la clase del Superhéroe: ")
                    if h['Clase'] == clase:
                        heroe[i]['Clase'] = input("Ingresa un nuevo clase para el Superhéroe: ")
                        #opcion2 = input("Selecciona una opcion: ")
                elif opcion2 == "3":
                    poder = input("Escribe el poder del Superhéroe: ")
                    if h['Poder'] == poder:
                        heroe[i]['Poder'] = input("Ingresa un nuevo poder para el Superhéroe: ")
                        #opcion2 = input("Selecciona una opcion: ")
                elif opcion2 == "4":
                    raza = input("Escribe la raza del Superhéroe: ")
                    if h['Raza'] == poder:
                        heroe[i]['Raza'] = input("Ingresa una nueva raza para el Superhéroe: ")
                        #opcion2 = input("Selecciona una opcion: ")
                elif opcion2 == "Q" or opcion2 == "q":
                    break
                else:
                    print("Error en selección")
                    opcion2 = input("Selecciona una opcion: ")
                opcion2 = input("Selecciona una opcion: ")
    elif opcion == "4":
        nombre = input("¿Qué Superheroe quieres eliminar?: ")
        # Buscamos un héroe en la lista con ese nombre y si concuerda lo sacamos con remove
        for h in heroe:
            if h['Nombre'] == nombre:
                heroe.remove(h)
    elif opcion == "M" or opcion == "m":
        os.system ('clear')
        print (menu)
    elif opcion == "q" or opcion == "Q":
        salir = input("¿Estás seguro que quieres salir? S/n: ")
        if (salir == "S" or salir == "s"):
            break
            os.system ('clear')
        else:
            opcion
