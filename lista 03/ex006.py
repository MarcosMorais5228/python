# print inicial
print('Senhoras e senhores, o desfile de gala do CIn vai começar!')

# primeiras entradas
numero_desfilantes = int(input())
marca_patrocinador = input()

# relacionamarca com subcelebridade
if marca_patrocinador == 'Tha Beauty':
    subcelebridade = 'Thais Linares'

elif marca_patrocinador == 'DeGuê?':
    subcelebridade = 'Davi Brito'

elif marca_patrocinador == 'Diva Depressão':
    subcelebridade = 'Edu e Fih'

# lista de monitores
monitores = ['Adrieli Queiroz','Arthur Jorge', 'César Cavalcanti','Elisson Oliveira','Filipe Moreira','Gabriela Alves','Joab Henrique','Maria Fernanda','Miriam Gonzaga','Sofia Remindes']

#começa desfile
desfilante = []
tentativa = []
substitutos = ['Adrieli Queiroz','Arthur Jorge', 'César Cavalcanti','Elisson Oliveira','Filipe Moreira','Gabriela Alves','Joab Henrique','Maria Fernanda','Miriam Gonzaga','Sofia Remindes']
invasao = 0

for i in range(numero_desfilantes):
    tentativa.append(input())
    if tentativa[i] in substitutos:
        substitutos.remove(tentativa[i])

for i in range(numero_desfilantes):
    # entrada monitor
    if tentativa[i] in monitores:
        desfilante.append(tentativa[i])
        monitores.remove(tentativa[i])
        print(f'Desfilante de n° {desfilante.index(desfilante[-1])+1}: {desfilante[-1]}!')

    # entrada subcelebridade
    elif tentativa[i] == subcelebridade:
        print('Invasão tolerada por motivos de patrocínio!')
        desfilante.append(tentativa[i])
        print(f'Desfilante de n° {desfilante.index(desfilante[-1])+1}: {desfilante[-1]}!')
        
    else:
        print(f'{tentativa[i]} invadiu a passarela! Segurem ele(a), produção!')

        # entrada substituto
        if len(substitutos) > 0:
            desfilante.append(substitutos[0])
            substitutos.remove(substitutos[0])
            invasao += 1
            print(f'Desfilante de n° {desfilante.index(desfilante[-1])+1}: {desfilante[-1]}!')
        
        # entrada invasor
        else: 
            desfilante.append(tentativa)
            invasao += 1
            print(f'Desfilante de n° {desfilante.index(desfilante[-1])+1}: {tentativa[i]}?! Pelo visto não havia como substituir...')
            # entrada Core
        if invasao == 3:
            print('Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!')
            desfilante.append('Core')
            print(f'Desfilante de n° {desfilante.index(desfilante[-1])+1}: {desfilante[-1]}!')

# outputs especiais
if 'Gretchen' in tentativa or 'Tulla Luana' in tentativa or 'Inês Brasil' in tentativa:
    print('Nas arquibancadas do CIn, sussurros indignados agitam a multidão...')

    if 'Gretchen' in tentativa:
        print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
    
    if 'Tulla Luana' in tentativa:
        print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')

    if 'Inês Brasil' in tentativa:
        print('"É aquele ditado... Vamo fazer o quê?"')
