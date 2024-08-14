def maior_menor(dicionario):
    # Verifica se o dicionário está vazio
    if not dicionario:
        return None, None

    # Extrai os valores do dicionário
    valores = dicionario.values()

    # Encontra o maior e o menor valor
    maior = max(valores)
    menor = min(valores)

    return maior, menor

# Exemplo de uso
dicionario = {
    'a': 10,
    'b': 23,
    'c': 5,
    'd': 42,
    'e': 18
}

maior, menor = maior_menor(dicionario)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
