
#Declaramos los elementos de los conjuntos

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}


#Descartamos a Juan de los administradores
administradores.discard("Juan")
#Agregamos a Marcos a los administradores
administradores.add("Marcos")


for usuario in usuarios: #Buscamos dentro del conjunto usuarios los administradores
    if usuario in administradores:
        print(usuario, "es admin")
    else:
        print(usuario, "no es admin")
