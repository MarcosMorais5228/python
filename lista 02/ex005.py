bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())
numero_jogadores = 3
bolinhas_final_andre = 1
bolinhas_final_bruno = 1
bolinhas_final_clara = 1
erros_andre = 0
erros_bruno = 0
erros_clara = 0
andre = 'jogador'
bruno = 'jogador'
clara = 'jogador'

while numero_jogadores > 1:
    if(bolinhas_andre > 0) and (numero_jogadores > 1) and (andre == 'jogador'):
        jogada_andre = input()

        if(jogada_andre == 'acertou'):
            erros_andre = 0
            if(numero_jogadores == 3):
                bolinhas_andre += 2
            else:
                bolinhas_andre +=1
            if(bruno == 'jogador'):
                bolinhas_bruno -= 1
            if(clara == 'jogador'):
                bolinhas_clara -= 1
        else:
            erros_andre += 1

        if(bolinhas_andre == 0) or (erros_andre == 3):
            if(bolinhas_andre == 0):
                print('andre saiu do jogo')
            elif(erros_andre == 3): 
                print('andre perdeu feio')
            numero_jogadores -= 1
            andre = 'perdeu'
            
    
        if(bolinhas_bruno == 0) and (bruno == 'jogador'):
            print('bruno saiu do jogo')
            numero_jogadores -= 1
            bruno = 'perdeu'
    
        if(bolinhas_clara == 0) and (clara == 'jogador'):
            print('clara saiu do jogo')
            numero_jogadores -= 1
            clara = 'perdeu'
    
    if(bolinhas_bruno > 0) and (numero_jogadores > 1) and (bruno == 'jogador'):
        jogada_bruno = input()

        if(jogada_bruno == 'acertou'):
            erros_bruno = 0
            if(numero_jogadores == 3):
                bolinhas_bruno += 2
            else:
                bolinhas_bruno += 1
            if(andre == 'jogador'):    
                bolinhas_andre -= 1
            if(clara == 'jogador'):    
                bolinhas_clara -= 1
        else: 
            erros_bruno +=1

        if(bolinhas_andre == 0) and (andre == 'jogador'):
            print('andre saiu do jogo')
            numero_jogadores -= 1
            andre = 'perdeu'
    
        if(bolinhas_bruno == 0) or (erros_bruno == 3):
            if(bolinhas_bruno == 0):    
                print('bruno saiu do jogo')
            elif(erros_bruno == 3): 
                print('bruno perdeu feio')
            numero_jogadores -= 1
            bruno = 'perdeu'
    
        if(bolinhas_clara == 0) and (clara == 'jogador'):
            print('clara saiu do jogo')
            numero_jogadores -= 1
            clara = 'perdeu'
    
    if(bolinhas_clara > 0) and (numero_jogadores > 1) and (clara == 'jogador'):
        jogada_clara = input()

        if(jogada_clara == 'acertou'):
            erros_clara = 0
            if(numero_jogadores == 3):
                bolinhas_clara += 2
            else:
                bolinhas_clara += 1
            if(andre == 'jogador'):
                bolinhas_andre -= 1
            if(bruno == 'jogador'):
                bolinhas_bruno -= 1
        else:
            erros_clara += 1

        if(bolinhas_andre == 0) and (andre == 'jogador'):
            print('andre saiu do jogo')
            numero_jogadores -= 1
            andre = 'perdeu'
    
        if(bolinhas_bruno == 0) and (bruno == 'jogador'):
            print('bruno saiu do jogo')
            numero_jogadores -= 1
            bruno = 'perdeu'
    
        if(bolinhas_clara == 0) or (erros_clara == 3):
            if(bolinhas_clara == 0):    
                print('clara saiu do jogo')
            elif(erros_clara == 3): 
                print('clara perdeu feio')
            numero_jogadores -= 1
            clara = 'perdeu'

if(andre == 'perdeu') and (bruno == 'perdeu'):
    print('clara ganhou')
    print('a quantidade final de bolas foi:')
    print(f'andre: {bolinhas_andre}')
    print(f'bruno: {bolinhas_bruno}')
    print(f'clara: {bolinhas_clara}')
    
elif(andre == 'perdeu') and (clara == 'perdeu'):
    print('bruno ganhou')
    print('a quantidade final de bolas foi:')
    print(f'andre: {bolinhas_andre}')
    print(f'bruno: {bolinhas_bruno}')
    print(f'clara: {bolinhas_clara}')

elif(clara == 'perdeu') and (bruno == 'perdeu'):
    print('andre ganhou')
    print('a quantidade final de bolas foi:')
    print(f'andre: {bolinhas_andre}')
    print(f'bruno: {bolinhas_bruno}')
    print(f'clara: {bolinhas_clara}')