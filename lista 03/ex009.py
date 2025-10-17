print('Sejam bem-vindos à Big Sub Brasil, onde a fama é temporária, os barracos são eternos, e só um vai conquistar o título de maior subcelebridade do país!')

nn1 = []
nn2 = []
matriz1 = []
matriz2 = []

# receber participantes
participantes = input()
participante1, participante2 = participantes.split(', ')
participante1 = participante1.capitalize()
participante2 = participante2.capitalize()

# formar matriz 1
n1 = input()
n1 = n1.split()

for i in range(10):
    nn1.append(int(n1[i]))
nn1.sort()

matriz1 = [[nn1[7],nn1[8],nn1[9]],[nn1[0],nn1[1],nn1[2]],[nn1[3]+1,nn1[4]+1,nn1[5]+1]]
desempate1 = nn1[6]

# formar matriz 2
n2 = input()
n2 = n2.split()

for i in range(10):
    nn2.append(int(n2[i]))
nn2.sort()

matriz2 = [[nn2[7],nn2[8],nn2[9]],[nn2[0],nn2[1],nn2[2]],[nn2[3]+1,nn2[4]+1,nn2[5]+1]]
desempate2 = nn2[6]

determinante1 = matriz1[0][0]*matriz1[1][1]*matriz1[2][2]+matriz1[0][1]*matriz1[1][2]*matriz1[2][0]+matriz1[0][2]*matriz1[1][0]*matriz1[2][1]-matriz1[2][0]*matriz1[1][1]*matriz1[0][2]-matriz1[2][1]*matriz1[1][2]*matriz1[0][0]-matriz1[2][2]*matriz1[1][0]*matriz1[0][1] 

determinante2 = matriz2[0][0]*matriz2[1][1]*matriz2[2][2]+matriz2[0][1]*matriz2[1][2]*matriz2[2][0]+matriz2[0][2]*matriz2[1][0]*matriz2[2][1]-matriz2[2][0]*matriz2[1][1]*matriz2[0][2]-matriz2[2][1]*matriz2[1][2]*matriz2[0][0]-matriz2[2][2]*matriz2[1][0]*matriz2[0][1] 

print(f'{participante1} e {participante2} disputarão entre si.')

# matriz 1
for i in range(3):
    print(' '.join(str(posicao) for posicao in matriz1[i]))

# pontos 1    
print(f'{participante1} está com pontuação {determinante1} pontos.')

# matriz 2
for i in range(3):
    print(' '.join(str(posicao) for posicao in matriz2[i]))

# pontos 2    
print(f'{participante2} está com pontuação {determinante2} pontos.')

# anúncio vencedor
if determinante1 > determinante2:
    print(f'Com talento duvidoso e esforço máximo, a vitória é de {participante1}!')

elif determinante2 > determinante1:
    print(f'Com talento duvidoso e esforço máximo, a vitória é de {participante2}!')

elif determinante1 == determinante2:
    print('RODADA DESEMPATE!!')
    
    if desempate1 > desempate2:
        print(f'Contra todas as expectativas (inclusive as nossas), {participante1} venceu a rodada!')
        print(f'Seu momento de brilhar virou eclipse {participante2}. Melhor sorte no próximo flop!')
    
    elif desempate2 > desempate1:
        print(f'Contra todas as expectativas (inclusive as nossas), {participante2} venceu a rodada!')
        print(f'Seu momento de brilhar virou eclipse {participante1}. Melhor sorte no próximo flop!')
    
    elif desempate2 == desempate1:
        print('Como isso é possível?? Os participantes empataram até na rodada desempate! EU DESISTO!!!')