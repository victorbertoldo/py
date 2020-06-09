def imprimir(maximo, atual):
    if atual >= maximo:  # condição de parada
        return  # return sem nhm parametro, finaliza execucao
    print(atual)
    imprimir(maximo, atual + 1)


imprimir(10, 1)
