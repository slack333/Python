import sys
if len(sys.argv) == 3:
    filas = int(sys.argv[1])
    columnas = int(sys.argv[2])

    if filas < 1 or filas > 9 or columnas < 1 or columnas > 9:
        print ("Error - filas o culumnas incorrectos")
        print ("Ejemplo: tabla.py [1-9][1-9]")
    else:
        print("\n")
        for i in range(filas):
            print("")
            for f in range(columnas):
                print("|_______|", end='')
else:
    print ("Error - argumentos incorrectos")
    print ("Ejemplo: tabla.py [1-9][1-9]")

#print(sys.argv) #Argumentos enviados
