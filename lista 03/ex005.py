nome_projeto = input()
itens_coletados_uteis = []
quantidades_coletadas_uteis = []
itens_coletados_inuteis = []
quantidades_coletadas_inuteis = []
componente = ''
construir = False
frase = 0
repeticao = 0

# checa itens necessarios
if nome_projeto == 'Memória ROM Simples':
    itens_necessarios = ['Redstone','Repetidores','Tochas de Redstone']
    quantidades_necessarias = [256, 64, 128]

elif nome_projeto == 'Calculadora de 4 bits':
    itens_necessarios = ['Redstone','Repetidores','Tochas de Redstone','Lâmpadas de Redstone']
    quantidades_necessarias = [512, 128, 64, 256]

elif nome_projeto == 'Sequenciador Musical':
    itens_necessarios = ['Redstone','Repetidores','Blocos de Notas','Observadores']
    quantidades_necessarias = [1024, 256, 64, 128]

elif nome_projeto == 'Processador de 8 Bits':
    itens_necessarios = ['Redstone','Repetidores','Lâmpadas de Redstone','Pistões Aderentes']
    quantidades_necessarias = [4096, 1024, 2048, 512]

elif nome_projeto == 'Display de Vídeo 8x8':
    itens_necessarios = ['Redstone','Repetidores','Comparadores','Pistões']
    quantidades_necessarias = [2048, 512, 256, 128]

elif nome_projeto == 'Supercomputador V13':
    itens_necessarios = ['Redstone','Repetidores','Comparadores','Pistões Aderentes']
    quantidades_necessarias = [8192, 2048, 1024, 1024]

while construir == False:
    construir = True
    # inicia a entrada e componentes
    while componente != 'Construir!':
        componente = input()

        # testa comando 
        if componente != 'Construir!':
            partes = componente.split()
            quantidade = int(partes[-1])
            nome = " ".join(partes[:-1])

            # adiciona item na lista
            if nome not in itens_coletados_uteis and nome not in itens_coletados_inuteis:
                if nome in itens_necessarios:
                    itens_coletados_uteis.append(nome)
                    quantidades_coletadas_uteis.append(quantidade)
                else:
                    itens_coletados_inuteis.append(nome)
                    quantidades_coletadas_inuteis.append(quantidade)
            
            else:
                if nome in itens_necessarios:
                    x = int(itens_coletados_uteis.index(nome))
                    quantidades_coletadas_uteis[x] = int(quantidades_coletadas_uteis[x]) + int(quantidade)
                else:
                    x = int(itens_coletados_inuteis.index(nome))
                    quantidades_coletadas_inuteis[x] = int(quantidades_coletadas_inuteis[x]) + int(quantidade)

            #imprime mensagem item
            if repeticao > 0:
                print()
                repeticao = 0
            if nome not in itens_necessarios:
                print(f'Hmm, {nome} não parece ser útil para este projeto.')
            elif nome == 'Redstone':
                print(f'Mais redstone! A energia que move o progresso! (+{quantidade} Redstone)')
            elif nome == 'Repetidores':
                print(f'Repetidores para garantir que o sinal chegue longe! Perfeito! (+{quantidade} Repetidores)')
            elif nome == 'Tochas de Redstone':
                print(f'Tochas de Redstone! Ótimo para inverter um sinal ou energizar o sistema. (+{quantidade} Tochas de Redstone)')
            elif nome == 'Lâmpadas de Redstone':
                print(f'Lâmpadas para o display! O resultado vai ficar bem visível. (+{quantidade} Lâmpadas de Redstone)')
            elif nome == 'Blocos de Notas':
                print(f'Blocos de Notas! Quem sabe não rola uma musiquinha no final? (+{quantidade} Blocos de Notas)')
            elif nome == 'Observadores':
                print(f'Observadores a postos! Nenhuma atualização de bloco passará despercebida. (+{quantidade} Observadores)')
            elif nome == 'Comparadores':
                print(f'Comparadores para a lógica! A precisão é a alma do negócio. (+{quantidade} Comparadores)')
            elif nome == 'Pistões':
                print(f'Pistões para mover as coisas de lugar. Isso vai ser útil! (+{quantidade} Pistões)')
            elif nome == 'Pistões Aderentes':
                print(f'Pistões Aderentes! Perfeitos para criar mecanismos retráteis. (+{quantidade} Pistões Aderentes)')

    # descobrir se tem material necessário
    for i in range(len(itens_necessarios)):
        if itens_necessarios[i] in itens_coletados_uteis:
            idx = itens_coletados_uteis.index(itens_necessarios[i])

            if quantidades_coletadas_uteis[idx] < quantidades_necessarias[i]:
                if frase == 0:
                    print(f'\nAinda não é possível construir o {nome_projeto}! Faltam:\n')
                    frase = 1

                qtd_faltante = int(quantidades_necessarias[i]) - int(quantidades_coletadas_uteis[idx]) 

                qtd_faltante = qtd_faltante//64
                if qtd_faltante == 0:
                    qtd_faltante = 1
                
                print(f'{qtd_faltante} pack(s) de {itens_coletados_uteis[idx]}')

                construir = False
                componente = ' '
                repeticao += 1
        else:
            if frase == 0:
                print(f'\nAinda não é possível construir o {nome_projeto}! Faltam:\n')
                frase = 1
            qtd_faltante = int(quantidades_necessarias[i])

            qtd_faltante = qtd_faltante//64
            if qtd_faltante == 0:
                qtd_faltante = 1
                
            print(f'{qtd_faltante} pack(s) de {itens_necessarios[i]}')

            construir = False
            componente = ' '
            repeticao += 1

    frase = 0
                
print(f'\nViniccius13 conseguiu construir o {nome_projeto}! Partiu programar!\n')
print(f'Para construirmos a(o) {nome_projeto}, utilizamos:\n')

for i in range(len(itens_coletados_uteis)):
    print(f'{itens_coletados_uteis[i]} : {quantidades_coletadas_uteis[i]}')

if len(itens_coletados_inuteis) > 0:                    
    print()
    print('Mas, em nossa jornada, também coletamos:\n')
    for i in range(len(itens_coletados_inuteis)):
        print(f'{itens_coletados_inuteis[i]} : {quantidades_coletadas_inuteis[i]}')