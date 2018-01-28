menu = ("""Bienvenido al programa de 3 opciones
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. SALIR
""")
print(menu)

while True:
    opcion = input("Elige una opción: ")
    if (opcion == "1"):
        n1 = float(input("Introduce un número: "))
        n2 = float(input("Introduce otro número: "))
        print (n1 + n2)
    elif (opcion == "2"):
        n1 = float(input("Introduce un número: "))
        n2 = float(input("Introduce otro número: "))
        print (n1 - n2)
    elif (opcion == "3"):
        n1 = float(input("Introduce un número: "))
        n2 = float(input("Introduce otro número: "))
        print (n1 * n2)
    elif (opcion == "4"):
        opcion2 = input("¿Estás seguro que quieres salir? S/n: ")
        if opcion2 == "s" or opcion2 == "S":
            break
    else:
        print ("Error en la selección, elige una opción.")
