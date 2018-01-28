import os

#Creamos los combatientes y guardamos sus característcas en diccionarios
soldado = {'vida':2, 'ataque':3, 'defensa':1, 'alcance':3}
marin = {'vida':3, 'ataque':4, 'defensa':4, 'alcance':1}
francot = {'vida':1, 'ataque':4, 'defensa':3, 'alcance':6}

#Creamos los enemigos y guardamos sus característcas en diccionarios
soldadoNazi = {'vida':2, 'ataque':3, 'defensa':2, 'alcance':3}
marinNazi = {'vida':4, 'ataque':2, 'defensa':5, 'alcance':1}
francotNazi = {'vida':1, 'ataque':3, 'defensa':4, 'alcance':6}

os.system ('clear') #Borrado de pantalla

#Creamos menú de inicio del juego con una variable
menuInicio = """ Juego V.0.0.1
1. Jugar
2. Mostrar características de los combatientes
3. Mostrar características de los enemigos
4. Modificar combatientes
5. Modificar enemigos
Q. Salir \n"""
print (menuInicio)

#Creamos menú para seleccionar un combatiente en una variable
menuB = """\n Selecciona tu combatiente
1. Soldado
2. Marin
3. Francotirador

C. Cancelar - Salir al menú principal \n"""

#Creamos menú para seleccionar un enemigo en una variable
menuC = """\n Selecciona tu enemigo
1. Soldado Nazi
2. Marin Nazi
3. Francotirador Nazi

C. Cancelar - Salir al menú principal \n"""

#Creamos menú para modificar a los combatientes
menuD = """\n Para modificar los combatientes selecciona uno de la listas
1. Soldado
2. Marin
3. Francotirador

C. Cancelar - Salir al menú principal \n"""

#Declaramos variables de los nombres de los combatientes
soldadoN = "Soldado"
marinN = "Marin"
francoN = "Francotirador"

#Declaramos variables de los nombres de los enemigos
soldadoNz = "Soldado Nazi"
marinNz = "Marin Nazi"
francoNz = "Francotirador Nazi"


#Inicio del programa
while True:

    seleccion = input("\n\nSelecciona una opción: ")

    if seleccion == "1":
        print ("\n",menuB) #Llamamos a la variable menuB
        seleccionA = input("Selecciona tu combatiente: ")

        if seleccionA == "1":
            os.system ('clear')
            print ("Haz seleccionado al soldado")
            print ("Las características de tu soldado son: ")
            #Imprimimos las caractrísticas del combatiente
            print (soldado['vida'], soldado['ataque'], soldado['alcance'], soldado['defensa'])
            print ("\n¿Contra quién quieres combatir?")
            print (menuC) #Llamamos a la variale menuC
            seleccionB = input("Selecciona un enemigo: ")

            if seleccionB == "1":
                print ("\nHaz seleccionado al Soldado Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                print (soldadoNazi['vida'], soldadoNazi['ataque'], soldadoNazi['alcance'], soldadoNazi['defensa'])
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")

                    soldadoModulo = (soldado['vida'], soldado['ataque'], soldado['alcance'], soldado['defensa'])
                    combatiente = sum(soldadoModulo)

                    soldadoModuloNazi = (soldadoNazi['vida'],soldadoNazi['ataque'],soldadoNazi['alcance'],soldadoNazi['defensa'])
                    enemigo = sum(soldadoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoN, "\n")
                        print (menuInicio)

                else:
                    os.system ('clear')
                    print (menuInicio)

            elif seleccionB == "2":
                print ("\nHaz seleccionado al Marin Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (marinvidaN, marinataqueN, marinalcanceN, marindefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    soldadoModulo = (soldado['vida'], soldado['ataque'], soldado['alcance'], soldado['defensa'])
                    combatiente = sum(soldadoModulo)
                    marinNaziModulo = (marinNazi['vida'],marinNazi['ataque'],marinNazi['alcance'],marinNazi['defensa'])
                    enemigo = sum(marinNaziModulo)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoN, "\n")
                        print (menuInicio)

                else:
                    os.system ('clear')
                    print (menuInicio)

            elif seleccionB == "3":
                print ("\nHaz seleccionado al Francotirador Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (francotvidaN, francotataqueN, francotalcanceN, francotdefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    soldadoModulo = (soldado['vida'], soldado['ataque'], soldado['alcance'], soldado['defensa'])
                    combatiente = sum(soldadoModulo)
                    francoModuloNazi = (francotNazi['vida'],francotNazi['ataque'],francotNazi['alcance'],francotNazi['defensa'])
                    enemigo = sum(francoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", francoNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoN, "\n")
                        print (menuInicio)

                else:
                    os.system ('clear')
                    print (menuInicio)

        elif seleccionA == "2":
            os.system ('clear')
            print ("Haz seleccionado al Marin")
            print ("Las características de tu Marin son: ")
            print (marinvida, marinataque, marinalcance, marindefensa)
            print ("\n¿Contra quién quieres combatir?")
            print (menuC)
            seleccionB = input("Selecciona un enemigo: ")

            if seleccionB == "1":
                print ("\nHaz seleccionado al Soldado Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (soldadovidaN, soldadoataqueN, soldadoalcanceN, soldadodefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    marinModulo = (marin['vida'], marin['ataque'], marin['alcance'], marin['defensa'])
                    combatiente = sum(marinModulo)
                    soldadoModuloNazi = (soldadoNazi['vida'],soldadoNazi['ataque'],soldadoNazi['alcance'],soldadoNazi['defensa'])
                    enemigo = sum(soldadoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinN, "\n")
                        print (menuInicio)

            elif seleccionB == "2":
                print ("\nHaz seleccionado al Marin Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (marinvidaN, marinataqueN, marinalcanceN, marindefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n...iniciando batalla...")
                    marinModulo = (marin['vida'], marin['ataque'], marin['alcance'], marin['defensa'])
                    combatiente = sum(marinModulo)
                    marinModuloNazi = (marinNazi['vida'],marinNazi['ataque'],marinNazi['alcance'],marinNazi['defensa'])
                    enemigo = sum(marinModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinN, "\n")
                        print (menuInicio)

            elif seleccionB == "3":
                print ("\nHaz seleccionado al Francotirador Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (francotvidaN, francotataqueN, francotalcanceN, francotdefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    marinModulo = (marin['vida'], marin['ataque'], marin['alcance'], marin['defensa'])
                    combatiente = sum(marinModulo)
                    francoModuloNazi = (francotNazi['vida'],francotNazi['ataque'],francotNazi['alcance'],francotNazi['defensa'])
                    enemigo = sum(francoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", francoNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinN, "\n")
                        print (menuInicio)

        elif seleccionA == "3":
            os.system ('clear')
            print ("Haz seleccionado al Francotirador")
            print ("Las características de tu Francotirador son: ")
            #print (francotvida, francotataque, francotalcance, francotdefensa)
            print ("\n¿Contra quién quieres combatir?")
            print (menuC)
            seleccionB = input("Selecciona un enemigo: ")

            if seleccionB == "1":
                print ("\nHaz seleccionado al Soldado Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (soldadovidaN, soldadoataqueN, soldadoalcanceN, soldadodefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    francoModulo = (francot['vida'], francot['ataque'], francot['alcance'], francot['defensa'])
                    combatiente = sum(francoModulo)
                    soldadoModuloNazi = (soldadoNazi['vida'],soldadoNazi['ataque'],soldadoNazi['alcance'],soldadoNazi['defensa'])
                    enemigo = sum(soldadoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", soldadoNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", francoN, "\n")
                        print (menuInicio)

            elif seleccionB == "2":
                print ("\nHaz seleccionado al Marin Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (marinvidaN, marinataqueN, marinalcanceN, marindefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    francoModulo = (francot['vida'], francot['ataque'], francot['alcance'], francot['defensa'])
                    combatiente = sum(francoModulo)
                    marinModuloNazi = (marinNazi['vida'],marinNazi['ataque'],marinNazi['alcance'],marinNazi['defensa'])
                    enemigo = sum(marinModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", francoN, "\n")
                        print (menuInicio)

            elif seleccionB == "3":
                print ("\nHaz seleccionado al Francotirador Nazi\n")
                print ("Las características del enemigo son: \n")
                #Imprimimos las caractrísticas del enemigo
                #print (francotvi, francotataqueN, francotalcanceN, francotdefensaN)
                iniciarpelea = input("\n¿Deseas inicar batalla de? - S/n: ")

                if iniciarpelea == "S" or iniciarpelea == "s":
                    print ("\n\t...iniciando batalla...")
                    francoModulo = (francot['vida'], francot['ataque'], francot['alcance'], francot['defensa'])
                    combatiente = sum(francoModulo)
                    francoModuloNazi = (francotNazi['vida'],francotNazi['ataque'],francotNazi['alcance'],francotNazi['defensa'])
                    enemigo = sum(francoModuloNazi)

                    if combatiente < enemigo:
                        os.system ('clear')
                        print ("\n\tHa ganado ", marinNz, "\n")
                        print (menuInicio)

                    else:
                        os.system ('clear')
                        print ("\n\tHa ganado ", francoN, "\n")
                        print (menuInicio)

        elif seleccionA == "C" or seleccionA == "c":
            seleccion

        else:
            os.system ('clear')
            print("Error en la seleccion, vuelve a intentarlo")
            seleccion
            print(menuInicio)

    elif seleccion == "2":
        print ("\nCaracterísticas de los combatientes:")
        print ("Soldado: ",soldado['vida'], soldado['ataque'], soldado['alcance'], soldado['defensa'])
        print ("Marin: ",marin['vida'], marin['ataque'], marin['alcance'], marin['defensa'])
        print ("Francotirador: ",francot['vida'], francot['ataque'], francot['alcance'], francot['defensa'])

    elif seleccion == "3":
        print ("\nCaracterísticas de los enemigos:")
        print ("Soldado Nazi: ",soldadoNazi['vida'], soldadoNazi['ataque'], soldadoNazi['alcance'], soldado['defensa'])
        print ("Marin Nazi: ",marinNazi['vida'], marinNazi['ataque'], marinNazi['alcance'], marinNazi['defensa'])
        print ("Francotirador Nazi: ",francotNazi['vida'], francotNazi['ataque'], francotNazi['alcance'], francotNazi['defensa'])

    elif seleccion == "4":
        print(menuD)
        elegir = input("¿Cuál quieres modificar?: ")

        if elegir == "1":

            while True:
                soldado['vida'] = int(input("¿Cuanta vida quieres que tenga el Soldado?: "))
                if soldado['vida'] >= 30 or soldado['vida'] <= 5:
                    print("Error, el soldado debe de tener por lo menos 5HP y un máximo de 30HP")
                    print(soldado)
                    soldado['vida'] = int(input("¿Cuanta vida quieres que tenga el Soldado?: "))
                #else:
                #    soldado['ataque'] = int(input("¿Cuanto daño de ataque quieres que tenga el Soldado?: "))

                if soldado['ataque'] >= 15 or soldado['ataque'] <= 7:
                    print("Error, el soldado debe de tener un daño mínimo de: 7 y un daño máximo de: 15")
                    print(soldado)
                    soldado['ataque'] = int(input("¿Cuanto daño de ataque quieres que tenga el Soldado?: "))
                #else:
                #    soldado['defensa'] = int(input("¿Cuanta defensa quieres que tenga el Soldado?: "))

                if soldado['defensa'] >= 40 or solado['defensa'] <= 20:
                    print("Error, el soldado debe de tener una defensa mínima de: 20 y una defensa máximo de: 40")
                    print(soldado)
                    soldado['defensa'] = int(input("¿Cuanta defensa quieres que tenga el Soldado?: "))
                #else:
                #    soldado['alcance'] = int(input("¿Cuanto alcance quieres que tenga el Soldado?: "))

                if soldado['alcance'] >= 3 or soldado['alcance'] <= 1:
                    print("Error, el soldado debe de tener un alcance mínimo de: 1 y un daño máximo de: 3. (Recuerda que es un melé)")
                    print(soldado)
                    soldado['alcance'] = int(input("¿Cuanto alcance quieres que tenga el Soldado?: "))
                else:
                    elegir

        elif elegir == "2":
            marin['vida'] = input("¿Cuanta vida quieres que tenga el Marin?: ")
            print(marin)
            marin['ataque'] = input("¿Cuanto daño de ataque quieres que tenga el Marin?: ")
            print(marin)
            marin['defensa'] = input("¿Cuanta defensa quieres que tenga el Marin?: ")
            print(marin)
            marin['alcance'] = input("¿Cuanto alcance quieres que tenga el Marin?: ")
            print(marin)

        elif elegir == "3":
            francot['vida'] = input("¿Cuanta vida quieres que tenga el Francotirador?: ")
            print(francot)
            francot['ataque'] = input("¿Cuanto daño de ataque quieres que tenga el Francotirador?: ")
            print(francot)
            francot['defensa'] = input("¿Cuanta defensa quieres que tenga el Francotirador?: ")
            print(francot)
            francot['alcance'] = input("¿Cuanto alcance quieres que tenga el Francotirador?: ")
            print(francot)

    elif seleccion == "5":
        print(menuC)
        elegir = input("¿Cuál quieres modificar?: ")

        if elegir == "1":
            soldadoNazi['vida'] = int(input("¿Cuanta vida quieres que tenga el Soldado Alemán?: "))
            print(soldadoNazi)
            soldadoNazi['ataque'] = int(input("¿Cuanto daño de ataque quieres que tenga el Soldado Alemán?: "))
            print(soldadoNazi)
            soldadoNazi['defensa'] = int(input("¿Cuanta defensa quieres que tenga el Soldado Alemán?: "))
            print(soldadoNazi)
            soldadoNazi['alcance'] = int(input("¿Cuanto alcance quieres que tenga el Soldado Alemán?: "))
            print(soldadoNazi)

        elif elegir == "2":
            marinNazi['vida'] = int(input("¿Cuanta vida quieres que tenga el Marin Alemán?: "))
            print(marinNazi)
            marinNazi['ataque'] = int(input("¿Cuanto daño de ataque quieres que tenga el Marin Alemán?: "))
            print(marinNazi)
            marinNazi['defensa'] = input("¿Cuanta defensa quieres que tenga el Marin Alemán?: ")
            print(marinNazi)
            marinNazi['alcance'] = input("¿Cuanto alcance quieres que tenga el Marin Alemán?: ")
            print(marinNazi)

        elif elegir == "3":
            francotNazi['vida'] = input("¿Cuanta vida quieres que tenga el Francotirador Alemán?: ")
            print(francotNazi)
            francotNazi['ataque'] = input("¿Cuanto daño de ataque quieres que tenga el Francotirador Alemán?: ")
            print(francotNazi)
            francotNazi['defensa'] = input("¿Cuanta defensa quieres que tenga el Francotirador Alemán?: ")
            print(francotNazi)
            francotNazi['alcance'] = input("¿Cuanto alcance quieres que tenga el Francotirador Alemán?: ")
            print(francotNazi)

    elif seleccion == "Q" or seleccion == "q":
        salir = input("¿Estás seguro que deseas salir?")
        break
