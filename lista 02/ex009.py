print('INICIANDO SIMULAÇÃO...')
pontosarthur = 0
pontossamuel = 0

jogador1 = input()
while(jogador1 != 'Arthur') and (jogador1 != 'Samuel'):
    print('Jogador inválido! Essa competição é apenas entre Arthur e Samuel!')
    jogador1 = input()

if(jogador1 == 'Arthur'):
    jogador2 = 'Samuel'

else:
    jogador2 = 'Arthur'
print(f'{jogador1} começa na corda!')
rodadas = int(input())

for i in range(0, rodadas):
    print(f'Começa a {i+1}ª rodada!')
    tropecos_jogador1 = 0
    frase = 0

    if(i == (rodadas-1)):
        print('Última rodada! Valendo 2 pontos!')

    ritmo = int(input())
    aposta = int(input())
    pulos = aposta

    print(f'{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!')

    while(tropecos_jogador1 != 3) and (pulos > 0):
        numero = str(pulos)
        soma = 0
        y = True
        x = True
        for digito in numero:
            soma += int(digito)
        
        for a in range(1, int((5*(soma**2)+4)**0.5 + 1)):
            if(5*(soma**2)+4 == a*a):
                x = False

        for b in range(1, int((5*(soma**2)+4)**0.5 + 1)):
            if(5*(soma**2)-4 == b*b):
                y = False
        
        if((y == False) or (x == False)) and (soma != 0):
            print(f'O número da soma é {soma}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!')
            tropecos_jogador1 += 1
            pulos -= ritmo
        
        else:
            if(pulos < aposta/4) and (frase == 0):
                print(f'{jogador1} está quase chegando ao apostado! Falta pouco!')
                frase = 1
                pulos -= ritmo
            
            else:
                print(f'{jogador1} pula com maestria! Faltam {pulos} pulos!')
                pulos -= ritmo

        if(tropecos_jogador1 == 3):
            print(f'E agora não tem jeito, {jogador1} cai de cara no chão!')

            if(pulos > aposta/2):
                print(f'Nossa!! Parece que {jogador1} não chegou nem na metade do apostado! Ainda bem que não foi competir pra valer no Round 6!')
            
            elif(pulos > aposta/4):
                print(f'Nem muito perto, nem muito longe do apostado. Talvez {jogador1} teve apenas azar!')
            
            elif(pulos <= aposta/4) and (pulos > 0):
                print(f'Quase lá! por pouco {jogador1} não alcançou o apostado!')
            
        else: 
            if(pulos == 0):
                print(f'{jogador1} cumpriu o prometido e alcançou {aposta} pulos! Ponto merecidíssimo!')

                if(i == (rodadas-1)):
                    if(jogador1 == 'Arthur'):
                        pontosarthur += 2
            
                    else:
                        pontossamuel += 2
                else:

                    if(jogador1 == 'Arthur'):
                        pontosarthur += 1
            
                    else:
                        pontossamuel += 1

            elif(pulos < 0):
                print(f'{jogador1} vai além, e supera a aposta em {0 - pulos} Ponto(s)! Deixou o {jogador2} no chinelo!')
                
                if(i == (rodadas-1)):
                    if(jogador1 == 'Arthur'):
                        pontosarthur += 2
            
                    else:
                        pontossamuel += 2
                else:
                    
                    if(jogador1 == 'Arthur'):
                        pontosarthur += 1
            
                    else:
                        pontossamuel += 1
        
    if(jogador1 == 'Arthur'):
        jogador1 = 'Samuel'
        jogador2 = 'Arthur'
        
    else:
        jogador1 = 'Arthur'
        jogador2 = 'Samuel'

print('COMPUTANDO PREVISÃO FINAL...')

if(pontosarthur > pontossamuel):
    print(f'Arthur venceu a competição com {pontosarthur} ponto(s)! Trouxe orgulho para Maceió!')

elif(pontossamuel > pontosarthur):
    print(f'Samuel venceu a competição com {pontossamuel} ponto(s)! O Messi careca em sua foto de perfil ficaria impressionado se soubesse!')

elif(pontosarthur == pontossamuel) and (pontosarthur > 0):
    print(f'Houve um empate técnico! Ambos fizeram {pontosarthur} ponto(s)! Óbvio que os dois monitores mais rápidos iriam empatar!')

elif(pontosarthur == 0) and (pontossamuel == 0):
    print('Ninguém pontuou! Que competição sem graça! Acho que os monitores se garantem mais nas dúvidas de IP mesmo...')
