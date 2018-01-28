#La magia de las iteraciones

c = 0
while c <= 5:
    c+=1
    print ("c vale", c)
else:
    print ("Se ha completado toda la iteración y c vale", c)


c = 0
while c <= 5:
    c+=1
    if (c==4):
        print("Rompemos el bucle cuando c vale",c)
        break
    print ("c vale", c)
else:
    print ("Se ha completado toda la iteración y c vale", c)


c = 0
while c <= 5:
    c+=1
    if (c==4):
        #print("Continuamos con la siguiente interacion",c)
        continue
    print ("c vale", c)
else:
    print ("Se ha completado toda la iteración y c vale", c)


print ("Bienvenido al menú iteractivo")
while (True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) SALUDAR
    2) SUMAR DOS NÚMEROS
    3) SALIR""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el otro número: "))
        print ("El resultado de la suma es: ", n1+n2)
    elif opcion == '3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")
        
