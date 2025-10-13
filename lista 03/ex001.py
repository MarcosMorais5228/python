# cria lista de convidados

num_convidados = int(input())

nome_convidado = []
comida_convidado = []
valor_comida = []
matriz = [] 
comida_mais_cara = 0

# testa se há convidados

if num_convidados == 0:
    print('Nenhum convidado marcou presença na festa do calabreso!')

else:
    # preenche lista de convidados

    for i in range(num_convidados):
        nome = input()
        comida = input()
        valor = int(input())

        # testa as restrições de convidados

        if nome == 'Maicon Kuster':
            print('você é convidado DE GUÊÊ???, sai da minha festa seu FOFOQUEIRO!!')
        
        elif comida in comida_convidado:
            print(f'Na Festa do Calabreso não pode comida Repetida SAI FORA {nome}')
        
        else:
            valor_comida.append(valor)
            valor_comida.sort()

            if valor in valor_comida:
                
            nome_convidado.insert(valor_comida.index(valor), nome)
            comida_convidado.insert(valor_comida.index(valor), comida)

    #testa número de convidados

    if len(nome_convidado) == 0:
        print('Nenhum convidado marcou presença na festa do calabreso!')

    else:
        # descobre comida mais cara

        for b in range(len(nome_convidado)):
            if comida_mais_cara < valor_comida[b]:
                comida_mais_cara = valor_comida[b]
                y = b

        # descobre comida mais barata
        for c in range(len(nome_convidado)):
            if c == 0:
                comida_mais_barata = valor_comida[c]
                z = c

            elif c > 0 and comida_mais_barata > valor_comida[c]:
                comida_mais_barata = valor_comida[c]
                z = c

            elif c > 0 and comida_mais_barata == valor_comida[c] and nome_convidado[z] < nome_convidado[c]:
                comida_mais_barata = valor_comida[c]
                z = c
                
        if len(nome_convidado) == 1:
            print(f'Obrigado para o(a) {nome_convidado[y]} pelo(a) excelente {comida_convidado[y]}')
        
        elif len(nome_convidado) > 1:
            print(f'Obrigado para o(a) {nome_convidado[y]} pelo(a) excelente {comida_convidado[y]}')
            print(f'Rapaz, {nome_convidado[z]} trouxe o(a) {comida_convidado[z]} que estava altamente mais ou menos!!!')
        
        # imprime nome convidados

        print('Lista de convidados do Calabreso')
        
        for i in range(len(nome_convidado)):
            print(f'{i+1}- {nome_convidado[i]}')


        



