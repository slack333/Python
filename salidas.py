v = "otro tezto"
n = 10
print ("Un texto ", v, " y un número ",n)

#cambiando el formato de los textos en una variable para que sea más prolija y legible
c = "Un texto {} y un número {}".format(v,n)
c = "Un texto '{}' y un número '{}'".format(v,n)

print (c)

c = "Un texto '{0}' y un número '{1}'".format(v,n)
print(c)

c = "Un texto '{1}' y un número '{0}'".format(v,n)
print(c)

c = "Un texto '{texto}' y un número '{numero}'".format(texto = v,numero = n)

print(c)

print("{:>30}".format("palabra")) #Alineamiento a la derecha en 30 caracteres
print("{:30}".format("palabra")) #Alineamiento a la izquierda en 30 caracteres
print("{:^30}".format("palabra")) #Alineamiento al centro en 30 caracteres
print("{:.5}".format("palabra")) #Truncamiento a 3 caracteres
print("{:>30}".format("palabra")) #Alineamiento a la derecha en 30 caracteres
print("{:>30.3}".format("palabra")) #Trucamiento en 3 carácteres a la derecha en 30 caracteres

#Formateo de números enteros, rellenados con espacios

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#Formateo de números enteros, rellenados con ceros

print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#Formateo de números flotantes, rellendados con espacios
print ("{:7.3f}".format(3.1415926))
print ("{:7.3f}".format(153.21))

#Formateo de números flotantes, rellendados con espacios
print ("{:07.3f}".format(3.1415926))
print ("{:07.3f}".format(153.21))
