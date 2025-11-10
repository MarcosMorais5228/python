# calcular combinações e notas usadas
def combinacoes(x, y, notasl, qnotasl, i, usar):
    if x == 0:
        return usar + 1, qnotasl
    elif x < 0:
        qnotasl[i] -= 1
        return 0, qnotasl
    
    elif x > 0:
        qnotasl[i] += 1
        usar, qnotasl = combinacoes(x-notasl[i], y, notasl, qnotasl, i, usar)
        

        if i < 4:
            usar, qnotasl = combinacoes(x, y, notasl, qnotasl, i+1, usar)

        return usar, qnotasl

notas = [100, 50, 20, 10, 5]
qnotas = [0, 0, 0, 0, 0]
# receber o valor da conta
valor_conta = int(input())

# print inicial
print(f'Calculando possibilidades para o valor: {valor_conta}')
if valor_conta != 0:
    comb, qnotas = combinacoes(valor_conta, valor_conta, notas, qnotas, 0, 0)
else:
    comb = 0

print(comb)
print(qnotas)