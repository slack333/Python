if True: #Se ejectua
    print ("se cumple la condicion")

if False: #No se ejecuta
    print ("se cumple la condicion")

a = 5

if a == 2: #no detecta ya que a = 5
    print ("a vale 2")
if a == 5: #se cumple la funcion
    print ("a vale 5")

a = 5
b = 10

if a == 5:
    print ("a vale", a)
    if b == 10:
        print ("y b vale", b)


if a == 5 and b == 10:
    print ("a vale 5 y b vale 10")

n = 10
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")

comando = "SALIR"
if comando == "ENTRAR":
    print("Bienvendio al sistema")
elif comando == "SALUDAR":
    print("Hola, espero que te lo estés pasando bien aprendiendo Python")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")

nota = float(input("Introduce una nota: "))

if nota >= 9:
    print ("Sobresaliente")
elif nota >= 7:
    print ("Notable")
elif nota >= 6:
    print ("Bien")
elif nota >= 5:
    print ("Suficiente")
else:
    print ("Insuficiente")

if True:
    pass
