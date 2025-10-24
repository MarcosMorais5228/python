sudoku = [[],[],[],[],[],[],[],[],[]]

# receber sudoku
for i in range(9):
    linha = input()
    linha = linha.split()
    for j in range(9):
        sudoku[i].append(linha[j])

# transformar em inteiros e marcar os números iniciais
inicial = []    
for lin in range(9):
    linha = []
    for col in range(9):
        if sudoku[lin][col] == '.':
            sudoku[lin][col] = 0
            linha.append(False)
        else:
            sudoku[lin][col] = int(sudoku[lin][col])
            linha.append(True)
    inicial.append(linha)

# começar a preencher
i = 0
j = 0
voltando = False

while i < 9:
    # se for um número inicial, não posso mexer
    if inicial[i][j] == True:
        if not voltando:
            if j == 8:
                j = 0
                i += 1
            else:
                j += 1
        else:
            if j == 0:
                j = 8
                i -= 1
            else:
                j -= 1

    # não é inicial            
    else:
        sudoku[i][j] = sudoku[i][j] + 1

        # se for maior que 9, tentei todos os números e deu errado
        if sudoku[i][j] > 9:
            sudoku[i][j] = 0
            voltando = True
            if j == 0:
                j = 8
                i -= 1
            else:
                j -= 1
        else:
            ok = True
            
            # checar se o número existe na linha
            for m in range(9):
                if m != j and sudoku[i][m] == sudoku[i][j]:
                    ok = False

            # checar se o número existe na coluna
            for m in range(9):
                if m != i and sudoku[m][j] == sudoku[i][j]:
                    ok = False

            # checar se o número existe no bloco
            if ok:
                bloco_i = i // 3
                bloco_j = j // 3
                for a in range(bloco_i * 3, bloco_i * 3 + 3):
                    for b in range(bloco_j * 3, bloco_j * 3 + 3):
                        if i != a and j != b:
                            if sudoku[i][j] == sudoku[a][b]:
                                ok = False

            # se deu tudo ok, vou pro próximo número
            if ok:
                voltando = False
                if j == 8:
                    j = 0
                    i += 1
                else:
                    j += 1

# print final se deu tudo certo
print('Caso encerrado! Mizael provou sua inocência lógica e o Sudoku foi resolvido!')
for linha in sudoku:
    print(' '.join(str(numero) for numero in linha))