# print inicial
print('Finalmente Jamal chega no CInbebeda, pronto pra causar, quando de repente…')
print('Jamal - "Que danado é isso?"')

condicao = True
aprendeu = False
monitores = ['Guilherme','Henrique','Júnior','Miguel']
pessoas_notas = []
movimentos = []
matriz = [['.','.','.'],['.','.','.'],['.','.','.']]
movimentos_corretos = ['D12','D33','E12','E31','D12','E31','D12']

entrada = input().split(', ')

# separando monitores e notas
for i in range(0,8,2):
    pessoas_notas.append([entrada[i], int(entrada[i+1])])
pessoas_notas.sort()

for i in range(4):
    if pessoas_notas[i][0] != monitores[i]:
        condicao = False

#volta para ordem de entrada
pessoas_notas = []
for i in range(0,8,2):
    pessoas_notas.append([entrada[i], int(entrada[i+1])])

# testa nomes    
while condicao == False:
    print('Insira nomes válidos.')
    pessoas_notas = []
    condicao = True
    entrada = input().split(', ')

    for i in range(0,8,2):
        pessoas_notas.append([entrada[i], int(entrada[i+1])])
        pessoas_notas.sort()

    for i in range(4):
        if pessoas_notas[i][0] != monitores[i]:
            condicao = False



# avaliacao jamal
for i in range(4):
    if pessoas_notas[i][1] == 10:
        print(f'O monitor {pessoas_notas[i][0]} é diferenciado! Teve a aprovação do próprio Jamal.')

# ordenar por notas
for i in range(4):
    pessoas_notas[i][0], pessoas_notas[i][1] = int(pessoas_notas[i][1]), pessoas_notas[i][0]

pessoas_notas.sort()

print(f'Jamal avaliou a situação dos monitores e viu que {pessoas_notas[0][1]} é o mais necessitado.')

#fala e passos jamal
print('Jamal - "Vou ensinar apenas uma vez, então preste atenção."\n')
print('''Jamal - Movimentação 0:
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
        movimentos= []
        entrada_valida = True

        for i in range(7):
            movimentos.append(list(movimentacao_na_matriz[i]))

        for i in range(7):
            if entrada_valida:
                if len(movimentos[i]) != 3 or movimentos[i][0] not in ['D', 'E']:
                    print('Movimento inválido! Por favor, insira outro.')
                    movimentacao_na_matriz = input().split(', ')
                    tamanho = True
                    entrada_valida = False

                elif movimentos[i][1] not in ['1', '2', '3']:
                    print('Movimento inválido! Por favor, insira outro.')
                    movimentacao_na_matriz = input().split(', ')
                    tamanho = True
                    entrada_valida = False

                elif movimentos[i][2] not in ['1', '2', '3']:
                    print('Movimento inválido! Por favor, insira outro.')
                    movimentacao_na_matriz = input().split(', ')
                    tamanho = True
                    entrada_valida = False

# começar a imprimir os movimentos da pior nota
print(f'''{pessoas_notas[0][1]} - Movimentação 0:
. . .
. . .
E . D\n''')

lin_e = 2
col_e = 0
lin_d = 2
col_d = 2

for i in range(len(movimentos)):
    letra = movimentos[i][0]
    print(f'{pessoas_notas[0][1]} - Movimentação {i+1}:')
    if letra == 'D':
        matriz[lin_e][col_e] = 'E'
        lin_d = int(movimentos[i][1]) - 1
        col_d = int(movimentos [i][2]) -1

        matriz[lin_d][col_d]  = i+1

        for m in range(3):
            for n in range(3):
                if matriz[m][n] == 'D' or matriz[m][n] == i:
                    matriz[m][n] = '.'
                   
    else:
        matriz[lin_d][col_d] = 'D'
        lin_e = int(movimentos[i][1]) - 1
        col_e = int(movimentos [i][2]) -1

        matriz[lin_e][col_e]  = i+1

        for m in range(3):
            for n in range(3):
                if matriz[m][n] == 'E' or matriz[m][n] == i:
                    matriz[m][n] = '.'
            
    for i in range(3):
         print(' '.join(str(posicao) for posicao in matriz[i]))
    print()

erros = 0
# quantificar erros
for i in range(7):
    if movimentacao_na_matriz[i] != movimentos_corretos[i]:
        erros += 1

if erros == 0 and pessoas_notas[0][1] == 'Júnior':
    print('Uma máquina! Depois de horas vendo o passinho no Instagram ele conseguiu pegar mais rápido.')
    aprendeu = True

elif erros == 0 and pessoas_notas[0][1] == 'Henrique':
    print('O maldito talento ataca novamente! Tinha que ser o desenrolado.')
    aprendeu = True

elif erros == 0 and pessoas_notas[0][1] == 'Miguel':
    print('O cara veio do interior pra mostrar como que se faz!')
    aprendeu = True

elif erros == 0 and pessoas_notas[0][1] == 'Guilherme':
    print('Ninguém nunca tinha visto ele dançar! Sabíamos que ele estava escondendo um dom.')
    aprendeu = True

elif erros == 1:
    print('Foi quase! O monitor merece uma nova chance!\n')
    movimentacao_na_matriz = input().split(', ')
    matriz = [['.','.','.'],['.','.','.'],['.','.','.']]
    movimentos = []

    for i in range(7):
        movimentos.append(list(movimentacao_na_matriz[i]))
    
    print(f'''{pessoas_notas[0][1]} - Movimentação 0:
. . .
. . .
E . D\n''')

    lin_e = 2
    col_e = 0
    lin_d = 2
    col_d = 2

    for i in range(7):
        letra = movimentos[i][0]
        print(f'{pessoas_notas[0][1]} - Movimentação {i+1}:')
        if letra == 'D':
            matriz[lin_e][col_e] = 'E'
            lin_d = int(movimentos[i][1]) - 1
            col_d = int(movimentos [i][2]) -1

            matriz[lin_d][col_d]  = i+1

            for m in range(3):
                for n in range(3):
                    if matriz[m][n] == 'D' or matriz[m][n] == i:
                        matriz[m][n] = '.'
                    
        else:
            matriz[lin_d][col_d] = 'D'
            lin_e = int(movimentos[i][1]) - 1
            col_e = int(movimentos [i][2]) -1

            matriz[lin_e][col_e]  = i+1

            for m in range(3):
                for n in range(3):
                    if matriz[m][n] == 'E' or matriz[m][n] == i:
                        matriz[m][n] = '.'
                
        for i in range(3):
            print(' '.join(str(posicao) for posicao in matriz[i]))
        print()
    
    erros = 0
    # quantificar erros
    for i in range(7):
        if movimentacao_na_matriz[i] != movimentos_corretos[i]:
            erros += 1
    
    if erros == 0:
        print(f'Era isso! {pessoas_notas[0][1]} só estava precisando de um empurrãozinho.')
        aprendeu = True
    
    else:
        print(f'Nem com outra tentativa {pessoas_notas[0][1]} conseguiu ajeitar isso.')

elif erros == 2:
    print(f'Melhor o monitor {pessoas_notas[0][1]} deixar esse negócio de dança pra lá.')

elif erros == 3:
    print('Isso tá horrível!')

elif erros > 3:
    print(f'O monitor {pessoas_notas[0][1]} foi expulso da festa por não saber dançar.')

if aprendeu == True:
    print('Jamal - "Vocês aprendem rápido! Quero que vocês dancem no meu próximo show!"')      

    resposta = input()

    if resposta == 'Sim':
        print(f'Óbvio que o monitor {pessoas_notas[0][1]} não perderia essa oportunidade por nada!')  

    elif resposta == 'Não':
        print(f'Infelizmente o monitor {pessoas_notas[0][1]} jogou essa oportunidade fora. Todos sabem que lá na frente ele vai se arrepender disso.')  

elif aprendeu == False:
    print('Jamal desistiu de ensinar pra quem não aprende. Ele saiu em grande estilo, mandando o passinho e andando.')  