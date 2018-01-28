#Calculadora codigo libre escrito por Bruno Aiub
#---------------------

#Menú
menu = "Menú \nA. Sumar \nB. Restar \nC. Multiplicar \nD. Dividir \nE. Módulo \nF. x a la n \n0. Salir\n"
#introduce1 = input("Introduce un número: ")
#introduce2 = input("Introduce otro número: ")
import os
os.system('clear')
version = ("""Calculadora versión 0.1.0, codigo libre, escrito por Bruno Aiub""")
puntos = ("""***************************************************************\n""")
resultado = "\n\t\t\t*** Total: "
dividirzero= "\n\t\t*** No se puede dividir entre 0 ***\n"
print (version)
print (puntos)
print (menu)

while (menu):
    opcion = input("Selecciona una opción: ")
    os.system('clear')
    if (opcion == "a" or opcion == "A"):
        #Suma
        print ("***SUMA***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        print (resultado, introduce1 + introduce2, "\n")

    elif (opcion == "b" or opcion == "B"):
        #Resta
        print ("***RESTA***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        print (resultado, introduce1 - introduce2, "\n")

    elif (opcion == "c" or opcion == "C"):
        #Multiplicar
        print ("***MULTIPLICACION***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        print (resultado, introduce1 * introduce2, "\n")

    elif (opcion == "d" or opcion == "D"):
        #Dividir
        print ("***DIVIDIR***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        if (introduce2 == 0):
            print (dividirzero)
        else:
            print (resultado, introduce1 / introduce2, "\n")

    elif (opcion == "e" or opcion == "E"):
        #MODULO
        print ("***MODULO***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        print (resultado, introduce1 % introduce2, "\n")

    elif (opcion == "f" or opcion == "F"):
        #ELEVADO A LA N
        print ("***X A LA N***")
        introduce1 = float(input("Introduce un número: "))
        introduce2 = float(input("Introduce otro número: "))
        os.system('clear')
        print (version)
        print (puntos)
        print (menu)
        print (resultado, introduce1 ** introduce2, "\n")

    elif (opcion == "0"):
        os.system('clear')
        exit()
