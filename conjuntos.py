conjunto = set() # set () sirve para transformar una lista a un conjunto
print (conjunto)

conjunto = {1,2,3} #Los conjuntos se arman con corchetes {}
print (conjunto)

conjunto.add(4) #Se puede agregar items a los conjuntos con .add y entre parentesis () el item
print (conjunto)

conjunto.add(0)
print (conjunto)

conjunto.add('H')
print (conjunto)

conjunto.add('A')
conjunto.add('Z')

print (conjunto) #conjuntos no respeta el orden de las letras, si de los números

grupo = {'Axel', 'Bruno', 'Luis'}
print ('Luis' in grupo) #Busca en el conjunto si esta el nombre dentro de los corchetes
##con una respuesta de True or False
print ('Dafne' in grupo)
print ('Axel' not in grupo)

numero = {1,2,3,4,5}
print (1 in numero)
print (8 in numero)

test = {'Aldo','Aldo','Aldo'}
print (test)

a = [1,2,3,3,2,1] # Creamos una lista con numeros repetidos
print (a)

c = set(a) # Alojamos y convertimos la lista en conjuntos
print (c)

a = list(c) #Convertimos el conjunto a lista
print (a)

a = [1,2,3,3,2,1]
a = list(set(a)) #Convertimos una lista en conjunto y de conjunto a una lista en,-
## una linea
print (a)

s = "Axel es un gil" #Creamos una cadena(string) y la convertimos a conjunto eliminando las letras repetidas
print (set(s))
