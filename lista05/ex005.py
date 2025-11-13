# funçãopara resolver labirinto
def labirinto(matriz, Bi, Bj, tempo, visitado):
    # se sair da matriz, retorna que não achou caminho
    if Bi < 0 or Bj < 0 or Bi >= n or Bj >= n:
        return None

    # Se pisar numa abóbora, ir por um caminho que já foi ou acabar o tempo, não achou caminho
    if matriz[Bi][Bj] == 'A' or visitado[Bi][Bj] or tempo < 0:
        return None

    # achou a saída
    if matriz[Bi][Bj] == 'S':
        return 0  

    # marcar caminho visitado
    visitado[Bi][Bj] = True

    # movimentos possíveis
    caminhos = []
    caminhos.append(labirinto(matriz, Bi + 1, Bj, tempo - 1, visitado))
    caminhos.append(labirinto(matriz, Bi - 1, Bj, tempo - 1, visitado))
    caminhos.append(labirinto(matriz, Bi, Bj + 1, tempo - 1, visitado))
    caminhos.append(labirinto(matriz, Bi, Bj - 1, tempo - 1, visitado))

    # desmarcar posição para caminho futuro
    visitado[Bi][Bj] = False

    caminhos_validos = []
    # retirar os Nones de caminhos válidos
    for i in range(len(caminhos)):
        if caminhos[i] is not None:
            caminhos_validos.append(caminhos[i])

    # se não tem caminho... adeus byte
    if len(caminhos_validos) == 0:
        return None

    # como o primeiro valor é 0, vai retornar 0+1 para o tepo(quando der um passo), mas sempre vai retornar o menor tempo
    return 1 + min(caminhos_validos)

# entrada dde horas
hora = input().strip()
h, m = hora.split(':')
m = int(m)
x = 60 - m

print(f"O relógio marca 23 horas e {m} minuto(s)! Byte tem apenas {x} minuto(s) para escapar!")

n = int(input())
matriz = []

# montar labirinto
for i in range(n):
    matriz.append([])
    a = input()
    for algo in a:
        matriz[i].append(algo)

# pegar a posição do byte
for i in range(n):
    for j in range(n):
        if matriz[i][j] == 'B':
            bi, bj = i, j

# criar lista de visitados e atribuir False para todas as posições
visitado = []
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(False)
    visitado.append(linha)

resultado = labirinto(matriz, bi, bj, x, visitado)

if resultado is None or resultado > x:
    print("NÃÃÃÃO! Tudo isso por causa de um docinho! Você estará para sempre conosco, Byte!")
else:
    print(f"CONSEGUIMOS!! Byte precisou de {resultado} minuto(s) para conseguir escapar!")
    folga = x - resultado
    if folga > 10:
        print(f"Abóboras CInistras que nada! Byte mostrou quem é que manda e conseguiu sair faltando {folga} minutos para elas acordarem")
    else:
        print("Ufa! Essa foi por pouco! Mas com ajuda dos alunos de IP essas abóboras nem pareciam tão sinistras assim.")