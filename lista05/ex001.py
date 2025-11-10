# calcular combinações e guardar todas as notas usadas
def combinacoes(x, notasl, i, comb1):
    if x == 0:
        lista.append(list(a))
        return comb1 + 1
        
    elif x < 0 or i >= 5:
        return comb1
    
    a.append(notasl[i])
    comb1 = combinacoes(x-notasl[i], notasl, i, comb1)
    a.pop()
        
    comb1 = combinacoes(x, notasl, i+1, comb1)

    return comb1

lista = []
a = []
notas = [100, 50, 20, 10, 5]
qnotas1 = []
qnotas = []
# receber o valor da conta
valor_conta = int(input())

# print inicial
print(f'Calculando possibilidades para o valor: {valor_conta}')

# iniciar função
if valor_conta != 0:
    comb = combinacoes(valor_conta, notas, 0, 0)

    # transformar a lista e listas em uma lista única
    for m in range(len(lista)):
        for n in range(len(lista[m])):
            qnotas1.append(lista[m][n])

    # guardar quantiade de notas usadas
    for c in range(5):
        qnotas.append(qnotas1.count(notas[c]))
else:
    comb = 0
    qnotas = [0, 0, 0, 0, 0]

if comb == 0:
    print('\nInfelizmente, não há como pagar essa conta com as notas disponíveis.')

elif comb == 1:
    print('\nEssa foi fácil! Só existe 1 possibilidade de pagar essa conta.')

print(f'\nTotal de possibilidades: {comb}')
print('\nUso das notas:')

for i in range(5):
    print(f'R${notas[i]}: usada em {qnotas[i]} combinações')