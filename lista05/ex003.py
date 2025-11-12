# função que descriptografa mensagem
def descurupirador(mensagem, chave, indice = 0, resultado = '', armadilhas = []):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T' ,'U', 'V' ,'W', 'X', 'Y' ,'Z']
    
    if indice == len(mensagem):
        return resultado, armadilhas
    
    letra = mensagem[indice]
    
    if letra not in alfabeto:
        armadilhas.append(indice)
        return descurupirador(mensagem, chave, indice + 1, resultado, armadilhas)

    
    c = alfabeto.index(letra)
    k = alfabeto.index(chave)
    m = (c - k) % 26

    prox_letra = alfabeto[m]

    return descurupirador(mensagem, prox_letra, indice + 1, resultado + prox_letra, armadilhas)

# entradas
chave_inicial = input()
frase_curupirada = input()

print('Decifrando mensagem do Trickster...')

# iniciar função
mensagem_descupirada, trickster = descurupirador(frase_curupirada, chave_inicial)

# verificar se teve armadilha
if len(trickster) > 0:
    posicoes = ", ".join(str(posicao) for posicao in trickster)
    print(f"Esse Trickster é um picareta mesmo. Foram encontradas armadilhas nas posições: {posicoes}")
else:
    print("Nenhuma armadilha encontrada! Até que o Trickster foi bonzinho.")

# imprimir mensagem
print(f"Mensagem revelada: {mensagem_descupirada}")