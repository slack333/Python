matriz = [
    [1,1,1,3],
    [2,2,2,7],
    [3,3,3,9],
    [4,4,4,13]
]

#matriz[1][3] = 6
#matriz[3][3] = 12
#Cambiamos los numeros de la listas de la matriz que está mal
matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])
print (matriz)


#formateo de cadena y conseguir una estructura como Nombre Apellido Nota
cadena = "zereP nauJ,01"

cadena_volteada = cadena[::-1]
print ("La nota de " + cadena_volteada[3:] + " es " + cadena_volteada[:2])
