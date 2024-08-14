def caracteres(frase):
    contar = {}

    for caractere in frase:
        if caractere in contar:
            contar[caracteres] += 1
        else:
            contar[caractere] = 1
    return contar

frase =  input('Digite uma frase:')

resultado = caracteres(frase)

print(resultado)