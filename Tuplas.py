tupla = (100, "Hola", [1,2,3,4], -50)
print (tupla)
print (tupla [0])
print (tupla[-1])
print (tupla[2:])
print (tupla[2][-1])
print (len(tupla))
print (len(tupla[2]))

#.index para buscar un elemento y saber su posición

print (tupla.index(100))
print (tupla.index("Hola"))
print (tupla.count(100))  #.count cuenta los elementos que estan repetidos dentro de la dupla
print (tupla.count("Trolo"))
tupla = (100,100,100,50,10)
print (tupla.count(100))

#print tupla.append(10) - no se puede modificar como las listas
