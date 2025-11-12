doces = int(input())

print('DOCES OU TRAVESSURAS???')

# função para  calcular as possibilidades
def possibilidades(n, k):
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return possibilidades(n, k - 1) + possibilidades(n - k, k)

# receber possibilidades
possib = possibilidades(doces, doces)

print(f'sem travessuras por hoje! tenho {possib} sacolinhas pra vocês')

# par ou ímpar
if possib % 2 == 1:
    print('hmm... número ímpar de sacolinhas 🍭 cuidado com as bruxas!')

else:
    print('doces equilibrados, sem travessuras!')