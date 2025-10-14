print('--- Simulador de Cancelamento ---\n')

numero_artistas = int(input())
artista = []
seguidores = []
sequencia = []
evento = []

# receber artistas e seguidores
for i in range(numero_artistas):
    sequencia.append(input().split(' - '))

# receber eventos
for i in range(numero_artistas):
    evento.append(int(input()))

# alterar seguidores
for i in range(numero_artistas):
    print(f'A subcelebridade da vez é: {sequencia[i][0]}')

    if evento[i] == 1:
        sequencia[i][1] = int(int(sequencia[i][1])*0.9)
        print(f'{sequencia[i][0]} perdeu 10% dos seguidores!')
    elif evento[i] == 2:
        sequencia[i][1] = int(int(sequencia[i][1])*1.05)
        print(f'{sequencia[i][0]} ganhou 5% de seguidores!')
    elif evento[i] == 3:
        sequencia[i][1] = int(int(sequencia[i][1])*0.85)
        print(f'{sequencia[i][0]} perdeu 15% dos seguidores!')
    else:
        print('Nenhum evento relevante. Seguidores continuam os mesmos.')

# organizar a nova matriz SEM USAR SORT!!!!!! :(
for i in range(numero_artistas):
    for j in range(numero_artistas-1):
        if int(sequencia[j][1]) < int(sequencia[j+1][1]):
            sequencia[j], sequencia[j+1] = sequencia[j+1], sequencia[j]

print('\n--- RANKING FINAL DE SEGUIDORES ---')
if numero_artistas >= 3:
    for i in range(3):
        print(f'{i+1}º Lugar: {sequencia[i][0]} com {sequencia[i][1]} seguidores.')

else:
    for i in range(numero_artistas):
        print(f'{i+1}º Lugar: {sequencia[i][0]} com {sequencia[i][1]} seguidores.')           


