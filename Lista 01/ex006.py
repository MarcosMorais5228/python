item_entrada = input()
valor = float(input())
responsavel_entrada = input()
tipo_evento_entrada = input()

item = item_entrada.capitalize()
responsavel = responsavel_entrada.capitalize()
tipo_evento = tipo_evento_entrada.capitalize()

if(responsavel == 'Angela'):
    print('Compra Aprovada!')
    if(valor > 100):
        print('Apenas eu tenho discernimento para gastos desta magnitude.')
    elif(valor <= 100):
        print('Compra feita por mim, obviamente dentro dos padrões de excelência.')
else:
    if(valor > 100):
        print('Compra Reprovada!')
        print('Gasto excessivo e irresponsável! Onde está a disciplina fiscal?!')
    elif(responsavel == 'Michael'):
        if(item == 'Mágica') or (item == 'Fantasia'):
            print('Compra Reprovada!')
            print('O Comitê não financia frivolidades e palhaçadas, Michael.')
        elif(valor > 60):
            print('Compra Aprovada com ressalvas!')
            if(tipo_evento == 'Natal'):
                print('O espírito natalino de Michael é... excessivo. A nota será conferida.')
            elif(tipo_evento == 'Aniversário'):
                print('Michael nunca gasta tanto nos aniversários dos funcionários, deve ser o dele!')
        elif(valor <= 60):
            print('Compra Aprovada!')
            print('Uma compra surpreendentemente sensata vinda do Michael. Suspeito.')
    elif(tipo_evento == 'Halloween'):
        if(item == 'Abóbora') and (valor <= 30):
            print('Compra Aprovada!')
            print('Uma abóbora de tamanho e custo razoáveis. Eficiente.')
        elif(item == 'Abóbora') and (valor > 30):
            print('Compra Aprovada com ressalvas!')
            print('Por que uma abóbora precisa ser tão cara? Extravagância.')
        elif(valor <= 100):
            print('Compra Aprovada com ressalvas!')
            print('Decoração de Halloween... Tenho certeza que Phyllis exagerou de novo.')
    elif(tipo_evento == 'Aniversário'):
        if(item == 'Bolo') and (valor <= 40):
            print('Compra Aprovada!')
            print('Um bolo modesto para celebrar mais um ano de produtividade, parabéns!')
        elif(item == 'Sorvete de menta com chocolate'):
            print('Compra Reprovada!')
            print('Este sabor de sorvete é uma abominação e não entrará em meu evento.')
        else:
            print('Compra Aprovada!')
            print('Itens de aniversário devem ser práticos, não uma distração do trabalho.')
    elif(valor > 50):
        print('Compra Aprovada com ressalvas!')
        print('Está dentro do orçamento, mas não quer dizer que não vou verificar!')
    elif(valor <= 50):
        print('Compra Aprovada!')
        print('Esta compra não viola nenhum regulamento... por enquanto.')