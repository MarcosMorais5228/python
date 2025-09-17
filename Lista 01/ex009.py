participante1, participante2, participante3, participante4 = input(), input(), input(), input()

print('Bem-vindos ao Jimmy Jab!')

if('Terry' in [participante1, participante2, participante3, participante4] or 'Holt' in [participante1, participante2, participante3, participante4]):
    print('Jimmy Jab CANCELADO!')
else:
    print('Nosso primeiro evento é...')
    print('A Bocatona!')
    if('Scully' in [participante1, participante2, participante3, participante4]):
        print('Scully leva a melhor, não tem como competir com ele.')
        perdedor = input()
        print(f'{perdedor} não avançou para a próxima fase!')
    else:
        vencedor = input()
        perdedor = input()
        print(f'{vencedor} levou a melhor na Bocatona!')
        print(f'{perdedor} não avançou para a próxima fase!')
    if(participante1 == perdedor):
        semif1 = participante2
        semif2 = participante3
        semif3 = participante4
    elif(participante2 == perdedor):
        semif1 = participante1
        semif2 = participante3
        semif3 = participante4
    elif(participante3 == perdedor):
        semif1 = participante1
        semif2 = participante2
        semif3 = participante4
    elif(participante4 == perdedor):
        semif1 = participante1
        semif2 = participante2
        semif3 = participante3
    print('O segundo evento é A corrida volumosa!')
    
    tempo1 = int(input())
    tempo2 = int(input())
    tempo3 = int(input())
    tempo_vencedor = min(tempo1, tempo2, tempo3)
    tempo_perdedor = max(tempo1, tempo2, tempo3)

    if(tempo_vencedor == tempo1):
        vencedor2 = semif1
    elif(tempo_vencedor == tempo2):
        vencedor2 = semif2
    elif(tempo_vencedor == tempo3):
        vencedor2 = semif3

    if(tempo_perdedor == tempo1):
        perdedor2 = semif1
    elif(tempo_perdedor == tempo2):
        perdedor2 = semif2
    elif(tempo_perdedor == tempo3):
        perdedor2 = semif3
    
    print(f'{vencedor2} levou a melhor na Corrida Volumosa!')
    print(f'{perdedor2} não avançou para a próxima fase!')

    if(semif1 == perdedor2):
        finalista1 = semif2
        finalista2 = semif3
    elif(semif2 == perdedor2):
        finalista1 = semif1
        finalista2 = semif3
    elif(semif3 == perdedor2):
        finalista1 = semif1
        finalista2 = semif2
    
    if(finalista1 in ['Jake','Amy']) and (finalista2 in ['Jake','Amy']):
        print('Jake ficou com o 2º lugar!')
        print('Amy VENCEU O JIMMY JABS!')
    else:
        ganhou = input()
        if(ganhou == finalista1):
            print(f'{finalista2} ficou com o 2º lugar!')
            print(f'{ganhou} VENCEU O JIMMY JABS!')
        elif(ganhou == finalista2):
            print(f'{finalista1} ficou com o 2º lugar!')
            print(f'{ganhou} VENCEU O JIMMY JABS!')