def labirinto(matriz, Bi, Bj, tempo):
    if matriz[Bi][Bj] == 'A' or Bi > n or Bi < 0 or Bj > n or Bj < n:
        return 0
    
    elif matriz[Bi][Bj] == 'S':
        return tempo
    
    return labirinto(matriz, Bi + 1, Bj, tempo-1) + labirinto(matriz, Bi, Bj + 1, tempo-1) + labirinto(matriz, Bi - 1, Bj, tempo-1) + labirinto(matriz, Bi, Bj - 1, tempo-1)

hora = input()
hora, minuto = hora.split(':')
x = 60 - int(minuto)

print(f'“O relógio marca 23 horas e {minuto} minuto(s)! Byte tem apenas {x} minuto(s) para escapar!”')

n = int(input())
matriz = []

for i in range(n):
    matriz.append([])
    a = input()
    for algo in a:
        matriz[i].append(algo)

for i in range(n):
    for j in range(n):
        if matriz[i][j] == 'B':
            bi = i
            bj = j

print(labirinto(matriz, bi, bj, x))