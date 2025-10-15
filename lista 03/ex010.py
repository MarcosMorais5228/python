# print inicial
print('Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…')
print('Jamal - "Que danado é isso?"')

monitores = ['Guilherme','Henrique','Júnior','Miguel']
pessoas_notas = []
movimentos = []
matriz = [['.','.','.'],['.','.','.'],['.','.','.']]

entrada = input().split(', ')

# separando monitores e notas
for i in range(0,8,2):
    pessoas_notas.append([entrada[i], entrada[i+1]])
    pessoas_notas.sort()
    condicao = True

for i in range(4):
    if pessoas_notas[i][0] != monitores[i]:
        print('Insira nomes válidos.')
        condicao = False

# testa nomes    
while condicao == False:
    pessoas_notas = []
    condicao = True
    entrada = input().split(', ')

    for i in range(0,8,2):
        pessoas_notas.append([entrada[i], int(entrada[i+1])])
        pessoas_notas.sort()

    for i in range(4):
        if pessoas_notas[i][0] != monitores[i]:
            print('Insira nomes válidos.')
            condicao = False

# ordenar por notas
for i in range(4):
    pessoas_notas[i][0], pessoas_notas[i][1] = int(pessoas_notas[i][1]), pessoas_notas[i][0]

pessoas_notas.sort()

# avaliacao jamal
for i in range(4):
    if pessoas_notas[i][0] == 10:
        print(f'O monitor {pessoas_notas[i][1]} é diferenciado! Teve a aprovação do próprio Jamal.')
print(f'Jamal avaliou a situação dos monitores e viu que {pessoas_notas[0][1]} é o mais necessitado.')

#fala e passos jamal
print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."\n')
print('''Jamal - movimentação 0:
. . .
. . .
E . D\n''')

print('''Jamal - Movimentação 1:
. 1 .
. . .
E . .\n''')

print('''Jamal - Movimentação 2:
. . .
. . .
E . 2\n''')

print('''Jamal - Movimentação 3:
. 3 .
. . .
. . D\n''')

print('''Jamal - Movimentação 4:
. . .
. . .
4 . D\n''')

print('''Jamal - Movimentação 5:
. 5 .
. . .
E . .\n''')

print('''Jamal - Movimentação 6:
. D .
. . .
6 . .\n''')

print('''Jamal - Movimentação 7:
. 7 .
. . .
E . .\n''')

# entrada nova movimentação
movimentacao_na_matriz = input().split(', ')

#testando
tamanho = True
while tamanho:
    tamanho = False
    if len(movimentacao_na_matriz) != 7:
        print('Movimento inválido! Por favor, insira outro.')
        movimentacao_na_matriz = input().split(', ')
        tamanho = True
    
    else:
        # transformar movimentos em matrizes
        for i in range(7):
            movimentos.append(list(movimentacao_na_matriz[i]))
        print(movimentos)
        for i in range(7):
            if movimentos[i][0] not in ['D', 'E']:
                print('Movimento inválido! Por favor, insira outro.')
                movimentacao_na_matriz = input().split(', ')
                tamanho = True
                movimentos = []

            elif movimentos[i][1] not in ['1', '2', '3']:
                print('Movimento inválido! Por favor, insira outro.')
                movimentacao_na_matriz = input().split(', ')
                tamanho = True
                movimentos = []

            elif movimentos[i][2] not in ['1', '2', '3']:
                print('Movimento inválido! Por favor, insira outro.')
                movimentacao_na_matriz = input().split(', ')
                tamanho = True
                movimentos = []

# começar a imprimir os movimentos da pior nota
print(f'''{pessoas_notas[0][1]} - Movimentação 0:
. . .
. . .
E . D\n''')

lin_e = 2
col

for i in range(7):
    letra = movimentos[i][0]
    x = int(movimentos[i][1]) - 1
    y = int(movimentos [i][2]) -1

    for j in range(3)
            





