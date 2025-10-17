sudoku = [[],[],[],[],[],[],[],[],[]]

# receber sudoku
for i in range(9):
    linha = input()
    linha = linha.split()
    for j in range(9):
        sudoku[i].append(linha[j])

# transformar em inteiros e marcar quais são fixos
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

i = 0
j = 0
voltando = False

while i < 9:
    while j < 9:
        ok = True
        proximo = True
        while ok and proximo:
            if inicial[i][j] == False:
                proximo = False
                if sudoku[i][j] < 9 and voltando == False:
                    sudoku[i][j] = sudoku[i][j] + 1

                    # verifica linha
                    for m in range(9):
                        if m != j:
                            if sudoku[i][j] == sudoku[i][m]:
                                ok = False

                    # verifica coluna
                    if ok:
                        for m in range(9):
                            if m != i:
                                if sudoku[i][j] == sudoku[m][j]:
                                    ok = False

                    # verifica bloco 3x3
                    if ok:
                        bloco_i = i // 3
                        bloco_j = j // 3
                        for a in range(bloco_i * 3, bloco_i * 3 + 3):
                            for b in range(bloco_j * 3, bloco_j * 3 + 3):
                                if i != a or j != b:
                                    if sudoku[i][j] == sudoku[a][b]:
                                        ok = False

                    proximo = True
                else:
                    if sudoku[i][j] == 9:
                        sudoku[i][j] = 0
                        proximo = False
                        voltando = True
                        repete = True
                        while repete:
                            if j == 0:
                                j = 8
                                i -= 1
                            else:
                                j -= 1
                            if i < 0:
                                i = 0
                                j = 0
                                repete = False
                            elif inicial[i][j] == False:
                                repete = False

                if ok and proximo:
                    voltando = False
                    repete = True
                    while repete:
                        if j == 8:
                            j = 0
                            i += 1
                        else:
                            j += 1
                        if i >= 9:
                            repete = False
                        elif inicial[i][j] == False:
                            repete = False

                else:
                    if sudoku[i][j] == 9:
                        sudoku[i][j] = 0
                        voltando = True
                        repete = True
                        while repete:
                            if j == 0:
                                j = 8
                                i -= 1
                            else:
                                j -= 1
                            if i < 0:
                                i = 0
                                j = 0
                                repete = False
                            elif inicial[i][j] == False:
                                repete = False
                    else:
                        voltando = False
                        repete = True
                        while repete:
                            if j == 0:
                                j = 8
                                i -= 1
                            else:
                                j -= 1
                            if i < 0:
                                i = 0
                                j = 0
                                repete = False
                            elif inicial[i][j] == False:
                                repete = False
            else:
                if voltando == False:
                    if j == 8:
                        j = 0
                        i += 1
                    else:
                        j += 1
                else:
                    repete = True
                    while repete:
                        if j == 0:
                            j = 8
                            i -= 1
                        else:
                            j -= 1
                        if i < 0:
                            i = 0
                            j = 0
                            repete = False
                        elif inicial[i][j] == False:
                            repete = False

# imprimir resultado final
for linha in sudoku:
    print(' '.join(str(x) for x in linha))
