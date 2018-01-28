numeros = [1,2,3,4]
datos = [4,"hola",-3,4,56,"Otra cadena"]
print (datos[0])

print (numeros + [5,6,7,8]) #Suma de listas

pares = [0,2,4,5,8,10] #Listas pares y queremos cambiar la del puesto Nº3
pares[3] = 6

print (pares)

pares.append(12) #Agregamos una nueva lista
print (pares)

pares.append(7*2)
print (pares)

letras = ['a','b','c','d','e','f']
print (letras[:3])

letras[:3] = ['A','B','C']
print (letras)

letras[:3] = []
print (letras)

letras = []
print (letras)

print (len(pares)) #la funcion len, muestra la longitud de letras

## listas anidadas dentro de listas
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print (r)

print (r[2][1])
