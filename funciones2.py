def imprimir(texto, veces = 1):
    print veces * texto
def varios(param1, param2, *otros):
    for val in otros:
        print val

varios(1, 2)
varios(1, 2, 3)
varios(1, 2, 3, 4)
