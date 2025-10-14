lista_frases = ['"Que tiro foi esse?"','"Segura a marimba"','"Tá com raiva? Morde as costas"','"Bateu de frente é só rajadão"']

qtd_frases = int(input())
citadas = []

# adiciona frases
for i in range(qtd_frases):
    lista_frases.append('"'+input()+'"')

# imprime frases
for i in range(4+qtd_frases):
    apareceu = 0
    for j in range(4+qtd_frases):
        if lista_frases[i] == lista_frases[j]:
            apareceu += 1

    if i == 0:
        print(f'{lista_frases[i]}: {apareceu}')
        citadas.append(lista_frases[i])
    
    elif lista_frases[i] not in citadas:
        print(f'{lista_frases[i]}: {apareceu}')
        citadas.append(lista_frases[i])

lista_frases.sort()
lista_frases = [frase.replace('"', '') for frase in lista_frases]
print(lista_frases)