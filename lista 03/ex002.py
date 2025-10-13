# cria lista de convidados

num_convidados = int(input())
matriz = [] 
comidas_trazidas = []

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
        
        elif comida in comidas_trazidas:
            print(f'Na Festa do Calabreso não pode comida Repetida SAI FORA {nome}')
        
        else:
            matriz.append([valor,nome,comida])
            comidas_trazidas.append(comida)

    #testa número de convidados
    matriz.sort()
    
    if len(matriz) == 0:
        print('Nenhum convidado marcou presença na festa do calabreso!')

    else:            
        if len(matriz) == 1:
            print(f'Obrigado para o(a) {matriz[len(matriz)-1][1]} pelo(a) excelente {matriz[len(matriz)-1][2]}')
        
        elif len(matriz) > 1:
            print(f'Obrigado para o(a) {matriz[len(matriz)-1][1]} pelo(a) excelente {matriz[len(matriz)-1][2]}')
            print(f'Rapaz, {matriz[0][1]} trouxe o(a) {matriz[0][2]} que estava altamente mais ou menos!!!')
        
        # imprime nome convidados

        print('Lista de convidados do Calabreso')
        
        for i in range(len(matriz)):
            print(f'{i+1}- {matriz[i][1]}')


        



