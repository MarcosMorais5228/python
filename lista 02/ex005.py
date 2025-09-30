bolinhas_andre = int(input())
bolinhas_bruno = int(input())
bolinhas_clara = int(input())
numero_jogadores = 3

while numero_jogadores > 1:
    if(bolinhas_andre > 0):
        jogada_andre = input()
        bolinhas_andre -= 1

        if(jogada_andre == 'acertou'):
            bolinhas_andre += 2
            bolinhas_bruno -= 1
            bolinhas_clara -= 1

            if(bolinhas_andre == 0):
                print('andre saiu do jogo')
                bolinhas_final_andre = 0
    
            if(bolinhas_bruno == 0):
                print('bruno saiu do jogo')
                bolinhas_final_bruno = 0
    
            if(bolinhas_clara == 0):
                print('clara saiu do jogo')
                bolinhas_final_clara = 0
    
    if(bolinhas_bruno > 0):
        jogada_bruno = input()
        bolinhas_bruno -= 1

        if(jogada_bruno == 'acertou'):
            bolinhas_bruno += 2
            bolinhas_andre -= 1
            bolinhas_clara -= 1

            if(bolinhas_andre == 0):
                print('andre saiu do jogo')
                bolinhas_final_andre = 0
    
            if(bolinhas_bruno == 0):
                print('bruno saiu do jogo')
                bolinhas_final_bruno = 0
    
            if(bolinhas_clara == 0):
                print('clara saiu do jogo')
                bolinhas_final_clara = 0
    
    if(bolinhas_clara > 0):
        jogada_clara = input()
        bolinhas_clara -= 1

        if(jogada_clara == 'acertou'):
            bolinhas_clara += 2
            bolinhas_andre -= 1
            bolinhas_bruno -= 1

            if(bolinhas_andre == 0):
                print('andre saiu do jogo')
                bolinhas_final_andre = 0
    
            if(bolinhas_bruno == 0):
                print('bruno saiu do jogo')
                bolinhas_final_bruno = 0
    
            if(bolinhas_clara == 0):
                print('clara saiu do jogo')
                bolinhas_final_clara = 0
    