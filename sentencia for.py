numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0
while(indice < len(numeros)):
    print(numeros[indice])
    indice += 1


for numero in numeros:
    print(numero)

for numero in numeros:
    numero *= 10

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0

for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print (numeros)

x = [1,2,3,4,5,6,7,8,9,10]
for indice, numero in enumerate(x):
    x[indice] *= 10
print(x)

cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2
print (cadena2)

for i in range(10):
    print(i)
    
