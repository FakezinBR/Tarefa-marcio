def somar_numeros_pares(inicio, fim):
    soma = 0
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:
            soma += numero
    return soma

resultado = somar_numeros_pares(50, 100)
print("Soma:", resultado)
