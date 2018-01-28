import sys
if len(sys.argv) == 2:
    numero = int(sys.argv[1])
    if numero < 0 or numero > 9999:
        print ("Error - numeros incorrectos")
        print ("Ejemplo: tabla.py [0-9999]")
    else:
        #Aqui va la lógica
        cadena = str(numero)
        logitud = len(cadena)
        for i in range(logitud):
            print("{:04d}".format(int(cadena[logitud -1 -i]) * 10 ** i))       

else:
    print ("Error - argumentos incorrectos")
    print ("Ejemplo: tabla.py [0-9999]")
