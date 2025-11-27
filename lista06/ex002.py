exigencia = ''
recebidos = ''
mimos = {}

# receber as exigências
while exigencia != 'MIMOS RECEBIDOS':
    exigencia = input()

    if exigencia != 'MIMOS RECEBIDOS':
        categoria, principal, qtd = exigencia.split(':')
        categoria = categoria.strip()
        principal = principal.strip()
        qtd = int(qtd.strip())

        if categoria == 'Bebidas' and principal == 'latte':
            qtd += 1
        mimos.update({categoria : (principal, qtd)})

# receber os mimos
while recebidos != 'ACABOU, a Glinda está pronta!':
    recebidos = input()
    
    if recebidos != 'ACABOU, a Glinda está pronta!':
        recebidos = recebidos.split(' ')

        categoria = recebidos[5]
        principal = recebidos[7]
        principal = principal.replace(')', '')
        qtd = int(recebidos[1])

        existe = mimos.get(categoria, 'nope')
        if existe != 'nope':
            atual = int(mimos[categoria][1]) - qtd
            mimos.update({categoria : (principal, atual)})

# relatório
print('Relatório de Balanço Final:')

negativos = 0

for categoria, (item, saldo) in mimos.items():
    print(f'Categoria: {categoria} Item: {item} Status: ', end='')

    if saldo <= 0:
        print('Você entregou TUDO! O mimo tá mais que garantido.')
    else:
        print(f'Golpe BAIXÍSSIMO! Faltam {saldo} mimos. Corre!')
        negativos += 1

# pular linha
print()

# tem gloss?
if "Maquiagem" in mimos and mimos["Maquiagem"][0] == "Gloss":
    saldo = mimos["Maquiagem"][1]
    if saldo <= 0:
        print('TUDO! O Gloss tá on. O look de Glinda tá salvo!')
    else:
        print('CADÊ meu gloss? Como divarei? ... A Glinda tá chorando de raiva!')

# tem latte?
if "Bebidas" in mimos and mimos["Bebidas"][0] == "latte":
    saldo = mimos["Bebidas"][1]
    if saldo <= 0:
        print('Latte gelado pronto! A voz de Glinda está salva. Pode vir o próximo take')
    else:
        print('Cadeia neles! Faltou o Mimo Sagrado. Essa equipe tá perdida!')

# veredito
print('\nVeredito Final')

if negativos >= 3:
    print('Thank U, Next! A equipe de camarim foi demitida!')
else:
    print('Estoque Aprovado! Glinda vai brilhar em Wicked!')


