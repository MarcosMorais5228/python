print('Começa agora o treinamento para grande final mundial de cabo de guerra!')

partidas = int(input())
pontos_arthur = 0
pontos_joao  = 0

while (partidas % 2 == 0):
    print('Não deverá haver empates! O número de partidas deverá ser ímpar.')
    partidas = int(input())

else:
    print(f'Eles batalharão em {partidas} longas partidas.')

forca_arthur = int(input())
forca_joao = int(input())

if(forca_arthur > forca_joao):
    mais_forte = 'Arthur'
    mais_fraco = 'João'

else:   
    mais_forte = 'João'
    mais_fraco = 'Arthur'

resistencia = int(input())

i = 1
while ((i <= partidas) and ((pontos_arthur < (partidas//2 + 1)) and (pontos_joao < (partidas//2 + 1)))):
    resistencia_arthur = resistencia
    resistencia_joao = resistencia
    
    print(f'Começa a {i}ª partida!')
    print(f'Placar geral: {pontos_arthur} X {pontos_joao}')
    
    while(resistencia_arthur > 0) and (resistencia_joao > 0):
        numero = int(input())
        x = True
        y = True
        for a in range(2, int(numero**0.5 + 1)):
            if numero % a == 0:
                x = False

        for b in range(1, int(numero**0.5 + 1)):
            if(numero == b*b):
                y = False

        if(y == False) or (numero == 0):
            print('O número é um quadrado perfeito! Arthur consegue puxar mais forte.')
            resistencia_arthur += 1
            resistencia_joao -= 1
        
        elif(x == True) and (numero != 0) and (numero != 1):
            print('O primo do primo é primo do primo? João puxa mais forte!')
            resistencia_arthur -= 1
            resistencia_joao += 1
        
        else:
            print(f'{mais_forte} é o mais forte! {mais_fraco} não consegue segurar.')

            if(mais_forte == 'Arthur'):
                resistencia_arthur += 1
                resistencia_joao -= 1
            else:
                resistencia_arthur -= 1
                resistencia_joao += 1
    
    if(resistencia_arthur > 0):
        print('Arthur dá orgulho para Maceió e ganha a partida!')
        pontos_arthur += 1
    
    else:
        print('João usa seus talentos de mangueboy e leva essa para casa!')
        pontos_joao += 1
    i += 1

print('\nAgora eles estão prontos para o mundial!')
print(f'Placar final: {pontos_arthur} X {pontos_joao}')

if(pontos_arthur > pontos_joao):
    if(pontos_joao == 0):
        print('João não teve chance! Arthur venceu todas as partidas.')
    else:
        print(f'O ganhador foi Arthur com uma diferença de {pontos_arthur - pontos_joao} partidas.')

elif(pontos_joao > pontos_arthur):
    if(pontos_arthur == 0):
        print('Arthur não teve chance! João venceu todas as partidas.')
    else:
        print(f'O ganhador foi João com uma diferença de {pontos_joao - pontos_arthur} partidas.')

