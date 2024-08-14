def positivos_negativos(lista):
    positivos = []
    negativos = []

    for numero in lista:
        if numero >= 0:
            positivos.append(numero)
        else:
            negativos.append(numero)
    return positivos, negativos

def main():
    entrada = input ('digite uma lista de numeros inteiros separados por espaço:')
    lista_numeros = list(map(int, entrada.split()))
    positivos,negativos = positivos_negativos(lista_numeros)
    print('numeros negativos', negativos)
    print('numeros positivos', positivos)
if __name__ == '__main__':
    main()