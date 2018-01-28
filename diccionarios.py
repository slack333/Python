vacio = {}
print (vacio)

print (type(vacio)) #type es la clasificacion de diccionarios, para crearlos utilizamos corchetes

colores = {'amarillo':'yellow','negro':'black','blanco':'white'} #esto sería un diccionario en dos idiomas
print (colores)

print (colores['negro']) #Nos muestra la traducción del diccionario de la palabra en corchetes cuadrados
print (colores['blanco'])

numeros = {10:'diez', 20:'veinte'} #Nos muestra los números en letras según el diccionario
print (numeros[10], numeros[20])

colores['amarillo'] = 'red' #Cambiamos la traduccion o corregimos dentro del diccionario
print (colores)

del(colores['amarillo'])
print (colores)

edades ={'Axel':18,'Bruno':31,'Valentina':24} #Creamos un diccionario de edades
print (edades)

edades['Bruno']+=1 #Le sumamos una año a Bruno
print (edades)

print (edades['Axel'] + edades['Valentina']) #Sumamos edades de los nombres del diccionario

for edad in edades:
    print(edad)

for clave in edades:
    print (edades[clave])

for clave in edades:
    print(clave,edades[clave])
for c,v in edades.items():
    print(c,v)

personajes = [] #creamos un diccionario de personajes

p = {'Nombre':'Gandalf','Clase':'Mago','Raza':'Humano'} #personaje 1
personajes.append(p)
print (personajes)

p = {'Nombre':'Superman','Clase':'Superheroe','Raza':'Extraterrestre'} #personaje 2
personajes.append(p)
print (personajes)

p = {'Nombre':'Thor','Clase':'Superheroe','Raza':'Dios'} #personaje 3
personajes.append(p)

print (personajes)

for p in personajes:
    print (p['Nombre'], p['Clase'], p['Raza'])
