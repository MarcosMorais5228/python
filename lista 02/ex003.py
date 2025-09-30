doces1 = int(input())
doces_sobraram = doces1 % 10

rodadas = int((doces1 - doces_sobraram)/10)
if(doces1 % 10 != 0):
    i = 1
    rodadas += 1
else:
    i = 0

jogador1 = input()
jogador2 = input()
vida1 = 10
vida2 = 10

if(jogador1 != 'Arthur') and (jogador2 != 'Arthur'):
    print('Epa!!! E cadê o dono dos doces??')
else:
    print('A batalha vai começar!')
    
    if(doces1 % 10 != 0):
        print(f'Pra aquecer, essa primeira vale menos, só {doces_sobraram} doces!')
        while (vida1 > 0) and (vida2 > 0):
            jogada1 = input()
            jogada2 = input()

            if(jogada1 == jogada2):
                print('Eita, jogaram a mesma coisa dessa vez.')
            else:
                if(jogada1 == 'pedra') and (jogada2 == 'tesoura'):
                    vida2 -= 4
                    
                elif(jogada1 == 'pedra') and (jogada2 =='papel'):
                    vida1 -= 2
                    vida2 += 2

                elif(jogada1 == 'papel') and (jogada2 =='pedra'):
                    vida1 += 2
                    vida2 -= 2

                elif(jogada1 == 'papel') and (jogada2 =='tesoura'):
                    vida1 -= 3
                    vida2 += 1

                elif(jogada1 == 'tesoura') and (jogada2 =='pedra'):
                    vida1 -= 4

                elif(jogada1 == 'tesoura') and (jogada2 =='papel'):
                    vida1 += 1
                    vida2 -= 3

                if(vida1 < 0):
                    vida1 = 0
                elif(vida2 < 0):
                    vida2= 0
                
                print(f'Esse turno terminou com {jogador1} tendo {vida1} de vida e {jogador2} tendo {vida2}!')
        
        if(vida1 <= 0):
            print(f'A rodada {1} vai para {jogador2}, que garante seus doces!')
            vida1 = 10
            vida2 = 10
        elif(vida2 <= 0):
            print(f'A rodada {1} vai para {jogador1}, que garante seus doces!')
            vida1 = 10
            vida2 = 10
    
    if(rodadas > 0):
            
        for a in range(i, rodadas):
            print(f'Batalha número {i+1}!')
            while (vida1 > 0) and (vida2 > 0):
                jogada1 = input()
                jogada2 = input()

                if(jogada1 == jogada2):
                    print('Eita, jogaram a mesma coisa dessa vez.')
                else:
                    
                    if(jogada1 == 'pedra') and (jogada2 == 'tesoura'):
                        vida2 -= 4
                            
                    elif(jogada1 == 'pedra') and (jogada2 =='papel'):
                        vida1 -= 2
                        vida2 += 2

                    elif(jogada1 == 'papel') and (jogada2 =='pedra'):
                        vida1 += 2
                        vida2 -= 2

                    elif(jogada1 == 'papel') and (jogada2 =='tesoura'):
                        vida1 -= 3
                        vida2 += 1

                    elif(jogada1 == 'tesoura') and (jogada2 =='pedra'):
                        vida1 -= 4

                    elif(jogada1 == 'tesoura') and (jogada2 =='papel'):
                        vida1 += 1
                        vida2 -= 3

                    if(vida1 < 0):
                        vida1 = 0
                    elif(vida2 < 0):
                        vida2= 0    

                    print(f'Esse turno terminou com {jogador1} tendo {vida1} de vida e {jogador2} tendo {vida2}!')
            
            if(vida1 <= 0):
                print(f'A rodada {i+1} vai para {jogador2}, que garante seus doces!')
                vida1 = 10
                vida2 = 10
            elif(vida2 <= 0):
                print(f'A rodada {i+1} vai para {jogador1}, que garante seus doces!')
                vida1 = 10
                vida2 = 10
            
            i += 1
        

        

