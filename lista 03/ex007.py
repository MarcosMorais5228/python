# print inicial
print('Iniciando investigação... Zé Felipe está focado.')

numero_eventos = int(input())
eventos = []
cornometro = 0
corno = False
encontros_suspeitos = 0
alibis = 0

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
            if eventos[j][1] > eventos[j+1][1]:
                eventos[j], eventos[j+1] = eventos[j+1], eventos[j]

# iniciando o cornômetro
for i in range(numero_eventos):
    if eventos[i][2] == 'VJM':
        corno = True
        cornometro += 100

if corno == False:
    for i in range(numero_eventos-1):
        for j in range(i+1, numero_eventos):
            if eventos[i][3] == eventos[j][3]:
                if (eventos[i][2] == 'V' and eventos[j][2] == 'JM') or (eventos[i][2] == 'JM' and eventos[j][2] == 'V'):
                    inicio1 = int(eventos[i][0][:2])
                    fim1 = int(eventos[i][1][:2])
                    inicio2 = int(eventos[j][0][:2])
                    fim2 = int(eventos[j][1][:2])

                    if (inicio2 >= inicio1 and inicio2 < fim1) or (fim2 > inicio1 and fim2 <= fim1):
                        cornometro += 35
                        encontros_suspeitos += 1
                
                elif (eventos[i][2] == 'V' and eventos[j][2] == 'ZF') or (eventos[i][2] == 'ZF' and eventos[j][2] == 'V'):
                    cornometro -= 20
                    alibis += 1
                    if cornometro < 0:
                        cornometro = 0

    #trocando sigla por nomes
    for i in range(numero_eventos):
        if eventos[i][2]  == 'V':
            eventos[i][2] = 'Virgínia'
        
        elif eventos[i][2]  == 'JM':
            eventos[i][2] = 'Jogador Misterioso'
        
        elif eventos[i][2]  == 'ZF':
            eventos[i][2] = 'Zé Felipe'
        
        elif eventos[i][2]  == 'VJM':
            eventos[i][2] = ' Virginia e Jogador Misterioso'

    if cornometro < 100:
        # inicio linha do tempo
        print('\n--- Linha do Tempo dos Eventos ---')
        for i in range(numero_eventos):
            print(f'{eventos[i][0]}-{eventos[i][1]}: {eventos[i][2]} - {eventos[i][3]}')
        
        # resumo
        print('\n--- Resumo da Análise ---')
        print(f'Encontros Suspeitos: {encontros_suspeitos}')
        print(f'Álibis Confirmados: {alibis}')

        # frase final
        if cornometro <= 99 and cornometro >= 70:
            print(f'\nNível de Suspeita: {cornometro} - MUITO SUSPEITO! Zé Felipe vai ter uma conversa séria com a Virgínia.')
        
        elif cornometro <= 69 and cornometro >= 30:
            print(f'\nNível de Suspeita: {cornometro} - Hmmm, algo de estranho não está certo. Zé Felipe vai ficar de olho.')
        
        elif cornometro < 30:
            print(f'\nNível de Suspeita: {cornometro} - Não há motivo para preocupação. Zé Felipe pode respirar aliviado e voltar a brincar com a Maria Flor.')

if cornometro >= 100:
    print('\nTRAIÇÃO CONFIRMADA! Zé Felipe vai fazer uma música sobre isso.')