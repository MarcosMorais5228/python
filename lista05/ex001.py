doces = int(input())

print('DOCES OU TRAVESSURAS???')

# função para  calcular as possibilidades
def possibilidades(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return possibilidades(n, k - 1) + possibilidades(n - k, k)

print(possibilidades(doces, doces))
