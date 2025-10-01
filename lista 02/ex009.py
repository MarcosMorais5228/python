print('INICIANDO SIMULAÇÃO…')

jogador1 = input()
while(jogador1 != 'Arhur') and (jogador1 != 'Samuel'):
    print('Jogador inválido! Essa competição é apenas entre Arthur e Samuel!')
    jogador1 = input()

if(jogador1 == 'Arthur'):
    jogador2 = 'Samuel'

else:
    jogador2 = 'Arthur'

rodadas = int(input())

for i in range(0, rodadas):
    print(f'{jogador1} começa na corda!')
    print(f'Começa a {i+1}ª rodada!')
    tropecos_jogador1 = 0
    frase = 0

    if(i == (rodadas-1)):
        print('Última rodada! Valendo 2 pontos!')

    ritmo = int(input())
    aposta = int(input())
    pulos = aposta

    print(f'{jogador2} aposta que {jogador1} não chega a {aposta} pulos! Vamos ver se é verdade! O ritmo de {jogador1} será {ritmo}!')

    while(ritmo < pulos):
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
            if(5*(soma**2)+4 == b*b):
                y = False
        
        if(y == False) or (x == False):
            print(f'O número da soma é {soma}, que faz parte da sequência de Fibonacci!! {jogador1} tropeça!')
            tropecos_jogador1 += 1
            pulos -= ritmo
        
        else:
            if(pulos < aposta/4) and (frase == 0):
                print(f'{jogador1} está quase chegando ao apostado! Falta pouco!')
                frase = 1
                pulos -= ritmo
            
            else:
                pulos -= ritmo
                print(f'{jogador1} pula com maestria! Faltam {pulos} pulos!')