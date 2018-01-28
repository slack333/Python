#Las pilas equivaldrian a una pila de libros que se apilan uno arriba del otro
#En este caso son listas, que para sacar el ultimo número sería de a uno

pila = [3,4,5]
pila.append(6)
pila.append(7) # con .append se agregarían
print (pila)
pila.pop() # con .pop se eleminiaría el último numero de la lista
print (pila)

n = pila.pop() # en este punto del programa, con una variable guardamos el último número de la listas

print (n)

print (pila)
pila.pop()
pila.pop()
pila.pop()
print (pila)
print (n)

# ---- Colas ----

from collections import deque #la manera de activar las colas es importando de las colecciones con el modulo 'deque'
#Las colas son utilizadas por los servidores de base de datos
cola = deque()
print (cola)

cola = deque(['Hector','Juan','Miguel'])
print (cola)

cola.append('Dafne') # con .append agregamos a la cola 
cola.append('Bruno')

print(cola)

cola.popleft()
print (cola)

p = cola.popleft() #almacenamos el primero de la lista en una variable y lo saca de la cola
print (p)

print (cola)
