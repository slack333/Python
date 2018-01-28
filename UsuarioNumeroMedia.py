menu = "Introduce la cantidad de números que quieras."
print (menu)
numeros = int(input("Cuántos números?: "))
suma = 0
for i in range(numeros):
    i = int( input("Número: ") )
    suma += i
print ("La suma total de los números es: ", suma)
print ("La media arimética es: ", suma / numeros)
