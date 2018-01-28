print """
 CALCULO DE KM/H
 ***************

Selecciona la marca
*******************

1)Audi
2)Bugatti
3)Chevy
4)Toyota

*******************

"""

class Auto:

    def __init__(self, gasolina):
        self.gasolina = gasolina
        print "Tenemos ", gasolina, "litros de combustible"
        
    def arrancar(self):
        arrancar_auto = raw_input("¿Deseas arrancar el auto? S/n: ")
            if arrancar_auto == "S" or arrancar_auto == "s":
                if self.gasolina > 0:
                    print "Tu auto arranca"
                    print "Tu auto tiene ", mi_auto.gasolina , " litros de combustible.\n"
                elif arrancar_auto == "N" or arrancar_auto == "n":
                    print "Tu auto no arranca"
                    print "No es posible que funcione sin combustible!"
                    mi_auto.opcion()
            elif arrancar_auto == "N" or arrancar_auto == "n":
                mi_auto.opcion()
    def conducir(self):
        conducir_auto = raw_input("¿Deseas conducir el auto? Se consumira combustible S/n: ")
        while conducir_auto == "S" or conducir_auto == "s":
            if conducir_auto == "S" or conducir_auto == "s":
                
                if self.gasolina > 0:
                    self.gasolina -= 1
                    print "Quedan", self.gasolina, "litros de gasolina.\n"
                    conducir_auto = raw_input("¿Desea conducir el auto? Se consumira combustible S/n: ")
                else:
                    print "No Se mueve"
            elif conducir_auto == "N" or conducir_auto == "n":
                mi_auto.opcion
    def opcion(self):
        opcion = int(input("Selecciona el auto: "))
        while opcion < "1" or opcion > "6":
            if (opcion == 1):
                print "Elegiste un Audi"
                mi_auto.calculo()
                mi_auto.arrancar()
                mi_auto.conducir()
                mi_auto.opcion()
            elif (opcion == 2):
                print "Elegiste un Bugatti"
                mi_auto.calculo()
                mi_auto.arrancar()
                mi_auto.conducir()
                mi_auto.opcion()
            elif (opcion == 3):
                print "Elegiste un Chevy"
                mi_auto.calculo()
                mi_auto.arrancar()
                mi_auto.conducir()
                mi_auto.opcion()
            elif (opcion == 4):
                print "Elegiste un Toyota"
                mi_auto.calculo()
                mi_auto.arrancar()
                mi_auto.conducir()
                mi_auto.opcion()
            elif (opcion == 5):
                sys.exit()
            break
    def calculo(self):
            km = float(input("Ingresa la distancia en KM a recorrer: "))
            tiempo = float(input("Ingresa el tiempo en HORAS de recorrido: "))
            try:
                calculo = km/tiempo
                print "La velocidad estimada de viaje es: ", calculo, "Km/h\n"
            except CeroDivisionError:
                print "El calculo del km/h no es real\n"
                opcion = float(input("Seleciona el auto: "))
mi_auto = Auto(50)
mi_auto.opcion()




