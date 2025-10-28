# funcao calculadora de distancia 
def distancia(y1,x1,y2,x2):
    if x1 > x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1
    
    if y1 > y2:
        y3 = y1 - y2
    else:
        y3 = y2 - y1

    res = max(x3,y3)
    return res

# funcao atirar
def atirar(arma, distancia):
    if arma == 'Espingarda':
        if distancia <= 2:
            dano = 25
        else:
            dano = 0
    
    elif arma == 'Rifle':
        if distancia == 3:
            dano = 15
        else:
            dano = 5
    
    elif arma == 'Metralhadora':
        if distancia >= 4:
            dano = 15
        else:
            dano = 0

    return dano

# funcao teleporte
def teleporte(y, x):
    for i in range(6):
        for j in range(6):
            if i == 0 and j == 0:
                res1 = distancia(y,x,i,j)
                casa = [0, 0]
            
            else:
                res2 = distancia(y,x,i,j)
                if res2 >= res1 and matriz[i][j] != 'I':
                    res1 = res2
                    casa = [i, j]
    
    return casa

#inicio
print('Sam: Mas que lugar é esse aqui?')
print('Dollman: WASD... Num exclusivo de PS5? Ah, fala sério!\n')

frase = 0
sam = 100
neil = 100
matriz = []
posicao_s = []
posiao_n = []
qtd = 0
tel = 0
danoNeil = 0
hitsFogo = 0
armamento = 'Rifle'

# receber matriz
for i in range(6):
    entrada = input().split(' ')
    matriz.append(entrada)

# jogo
pos = 'P'
pos1 = 'P'
movimento = input()
while sam > 0 and neil > 0:
    for m in range(6):
        for n in range(6):
            if matriz[m][n] == 'S':
                posicao_s = [int(m), int(n)]
            if matriz[m][n] == 'N':
                posiao_n = [int(m), int(n)]
    
    # Sam se move
    if movimento == 'W':
        if posicao_s[0] != 0 and matriz[posicao_s[0]-1][posicao_s[1]] != 'I':
            matriz[posicao_s[0]][posicao_s[1]] = pos
            pos = matriz[posicao_s[0]-1][posicao_s[1]]
            matriz[posicao_s[0]-1][posicao_s[1]] = 'S'


    elif movimento == 'A':
        if posicao_s[1] != 0 and matriz[posicao_s[0]][posicao_s[1]-1] != 'I':
            matriz[posicao_s[0]][posicao_s[1]] = pos
            pos = matriz[posicao_s[0]][posicao_s[1]-1]
            matriz[posicao_s[0]][posicao_s[1]-1] = 'S'


    elif movimento == 'S':
        if posicao_s[0] != 5 and matriz[posicao_s[0]+1][posicao_s[1]] != 'I':
            matriz[posicao_s[0]][posicao_s[1]] = pos
            pos = matriz[posicao_s[0]+1][posicao_s[1]]
            matriz[posicao_s[0]+1][posicao_s[1]] = 'S'


    elif movimento == 'D':
        if posicao_s[1] != 5 and matriz[posicao_s[0]][posicao_s[1]+1] != 'I':    
            matriz[posicao_s[0]][posicao_s[1]] = pos
            pos = matriz[posicao_s[0]][posicao_s[1]+1]
            matriz[posicao_s[0]][posicao_s[1]+1] = 'S'

    
    # Sam troca armamento
    elif movimento == 'Espingarda':
        armamento = 'Espingarda'
        print('Arma trocada para Espingarda.')
    
    elif movimento == 'Rifle':
        armamento = 'Rifle'
        print('Arma trocada para Rifle.')

    elif movimento == 'Metralhadora':
        armamento = 'Metralhadora'
        print('Arma trocada para Metralhadora.')

    # Sam atira
    elif movimento == 'Atirar':
        d = distancia(posicao_s[0],posicao_s[1],posiao_n[0],posiao_n[1])

        dano = atirar(armamento, d)
        neil -= dano
        if dano > 0:
            tel += 1

        # teleporte de Neil
        if tel == 3 and neil > 0:
            nova = teleporte(posicao_s[0], posicao_s[1])

            matriz[posiao_n[0]][posiao_n[1]] = pos1
            if matriz[nova[0]][nova[1]] != 'N':
                pos1 = matriz[nova[0]][nova[1]]
            matriz[nova[0]][nova[1]] = 'N'
            for i in range(6):
                print(' '.join(str(letra) for letra in matriz[i]))
            tel = 0
    
    if pos == 'F':
        sam -= 5
        hitsFogo += 1
        
    qtd += 1

    if qtd == 4 and neil > 0:
        print('>>> Você recebe um disparo de Neil! <<<')
        sam -= 15
        danoNeil += 15
        qtd = 0

        if sam <= 40 and frase == 0:
            print('Dollman: A Fragile comeu todos os criptobiontes da DHV Magalhães... Se curar não é uma opção. Tome cuidado, Sam.')
            frase += 1
    
    if sam > 0 and neil > 0:
        movimento = input()
    

likes = 1000 - (danoNeil * 8) - (hitsFogo * 10)

if sam <= 0:
    print('''\nMISSÃO FALHOU
==============
Sam foi derrotado.
[Sua alma vaga pela Emenda, buscando reencontrar seu corpo perdido...]''')

elif neil <= 0:
    print(f'''\nMISSÃO COMPLETA! - Investigue a Anomalia
========================================
Likes recebidos: 👍 {likes}''')
