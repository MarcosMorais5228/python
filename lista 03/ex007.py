# print inicial
print('Iniciando investigação... Zé Felipe está focado.')

numero_eventos = int(input())
eventos = []
suspeita = 0

# inicia a entrada de eventos
for i in range(numero_eventos):
    sigla, evento, horai, horaf = input().split(' - ')
    eventos.append([horai, horaf, sigla, evento])

# organizando a matriz com Bubble Sort
for i in range(numero_eventos-1):
    for j in range(numero_eventos-i-1):
        if eventos[j][0] > eventos[j+1][0]:
            eventos[j], eventos[j+1] = eventos[j+1], eventos[j]
        elif eventos[j][0] == eventos[j+1][0]:
            if eventos[j][1] == eventos[j+1][0]:
                eventos[j], eventos[j+1] = eventos[j+1], eventos[j]
#trocanndo sigla por nomes
for i in range(numero_eventos):
    if eventos[i][2]  == 'V':
        eventos[i][2] = 'Virgínia'
    
    elif eventos[i][2]  == 'JM':
        eventos[i][2] = 'Jogador Misterioso'
    
    elif eventos[i][2]  == 'ZF':
        eventos[i][2] = 'Zé Felipe'
    
    elif eventos[i][2]  == 'vjm':
        eventos[i][2] = ' Virginia e Jogador Misterioso'

# inicio linha do tempo
print('\n-- Linha do Tempo dos Eventos ---')
for i in range(numero_eventos):
    print(f'{eventos[i][0]}-{eventos[i][1]}: {eventos[i][2]} - {eventos[i][3]}')