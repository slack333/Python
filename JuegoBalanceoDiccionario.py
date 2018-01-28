import os

caballero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
guerrero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
arquero = {'vida':2, 'ataque':2, 'defensa':2, 'alcance':2}
os.system ('clear')
menu1 = ("""Guerra 0.0.1

1. Ver estadisticas de todos los combatientes
2. Modificar las condiciones de los combatientes
Q. Salir""")
print (menu1)

while True:
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        os.system ('clear')
        menu = ("""Los combatientes son:
        1. Caballero
        2. Guerrero
        3. Arquero
        C. Cancelar """)
        print (menu)
        opcion2 = input("Selecciona un combatiente: ")
        os.system ('clear')
        if opcion2 == "1":
            print ("La vida del caballero es: ",caballero['vida'])
            print ("El ataque del caballero es: ",caballero['ataque'])
            print ("La defensa del caballero es: ",caballero['defensa'])
            print ("El alcance del caballero es: ",caballero['alcance'])
            print (menu1)
        elif opcion2 == "2":
            print ("La vida del guerrero es: ",guerrero['vida'])
            print ("El ataque del guerrero es: ",guerrero['ataque'])
            print ("La defensa del guerrero es: ",guerrero['defensa'])
            print ("El alcance del guerrero es: ",guerrero['alcance'])
            print (menu1)
        elif opcion2 == "3":
            print ("La vida del arquero es: ",arquero['vida'])
            print ("El ataque del arquero es: ",arquero['ataque'])
            print ("La defensa del arquero es: ",arquero['defensa'])
            print ("El alcance del arquero es: ",arquero['alcance'])
            print (menu1)
        elif opcion2 == "C" or opcion2 == "c":
            opcion
            print (menu1)
        else:
            print("Error en seleción. ")
            print (menu1)
    elif opcion == "2":
        os.system ('clear')
        print ("""Los combatientes son:
        1. Caballero
        2. Guerrero
        3. Arquero
        C. Cancelar """)
        opcion3 = input("Selecciona un combatiente: ")
        os.system ('clear')
        if opcion3 == "1":
            caballero['vida'] = guerrero['vida'] * 2
            caballero['defensa'] = guerrero['defensa'] * 2
            print ("La vida del caballero es ",caballero['vida']," y la defensa ", caballero['defensa'])
            print (menu1)
        elif opcion3 == "2":
            guerrero['ataque'] = caballero['ataque'] * 2
            guerrero['alcance'] = caballero['alcance'] * 2
            print ("El ataque del guerrero es ",guerrero['ataque']," y el alcance ", guerrero['alcance'])
            print (menu1)
        elif opcion3 == "3":
            arquero['vida'] = guerrero['vida']
            arquero['ataque'] = guerrero['ataque']
            arquero['defensa'] = guerrero['defensa'] / 2
            arquero['alcance'] = guerrero['alcance'] * 2
            print ("La vida del arquero es, ",arquero['vida'],", el ataque, ", arquero['ataque'], "la defensa, ", arquero['defensa'], "y el alcance, ", arquero['alcance'])
            print(menu1)
        elif opcion3 == "C" or opcion2 == "c":
            opcion
            print (menu1)
        else:
            print("Error en seleción. ",opcion3)
            print(menu1)
    elif opcion == "Q" or opcion == "q":
        break
