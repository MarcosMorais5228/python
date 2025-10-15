entrada_inicial = input()
pessoas = True
bolha_influencers = ['Sofia Santino', 'Doarda', 'Ciclopin', 'Bruna Pinheiro']
bolha_cantores = ['Thiaguinho','Neiff','Veigh','Mc Loma','Mirella Santos','Mariely Santos', 'Little Thiago', 'Diferenciado']
convidados = []
influencers = 0
cantores = 0
pautas = ['Medo de ficar musculosa demais por causa da academia', 'O cara que eu gosto não me quer, mas eu continuo insistindo. Acha que eu consigo algo?', 'Meu chefe só me dá um dia de folga, mas eu precisava de dois.','Pessoas que adoram se fazer de coitadinhas','Essa história de que homem sofre calado']

# caso seja 0 mensagens
if entrada_inicial == 'WhatsApp: 0 mensagens.':
    print('I hate to tell you this BUT')
    print('Bia tava achando que ia fazer um mousse. O mousse virou uma piada, parceira')
    print('''\nComo a vida não precisa ser only fechos, a gente vai finalizar minha franja hoje:
Essa chapinha eu dei literalmente tipo 50 reais nela. Não é a mais potente, não é a mais mais... mas ela é algo. Às vezes a gente só precisa ser algo, não precisa ser tudo.
E o protetor térmico? Vei, a chapinha sabe que eu tô fazendo de coração, ela nunca queimaria meu cabelo.
Espera esfriar e você vai barbarizar quando tiver pronto
É isso, tchau meus amores''')

else:
    #pegando nome de convidados
    famoso = entrada_inicial.split('acabou de confirmar')[0].strip()
    convidados.append(famoso)

    # checando Mc Loma
    if famoso == 'Mc Loma':
        convidados.append('Mirella Santos')
        convidados.append('Mariely Santos')

    while pessoas == True:
        entrada = input()
        if entrada == 'CABOSSE! Bora simbora organizar essa festa.':
            pessoas = False
            famoso = ''
        
        else:
            famoso = entrada.split('acabou de confirmar')[0].strip()
            convidados.append(famoso)

        # checando Mc Loma
        if famoso == 'Mc Loma':
            convidados.append('Mirella Santos')
            convidados.append('Mariely Santos')

    # checagem de bolha
    for i in range(len(convidados)):
        if convidados[i] in bolha_influencers:
            influencers += 1
        
        elif convidados[i] in bolha_cantores:
            cantores += 1

    # mensagem tipo de festa
    if influencers != 0 and cantores != 0:
        print('''Cachaçaria na minha casa hoje, 21h.
Todo mundo lá em casa! Tem que ser uma festa que dure muito, tipo 27 anos e 3 meses!!''')
    
    elif influencers == 0 and cantores != 0:
        print(f'''<PLANOS PARA FESTA>
Convidados: {', '.join(convidados)}.
Tipo de comemoração: Paredão - Show na minha casa!!''')
    
    else: 
        print(f'''<TARDE DE FOFOCAS>
Convidados: {', '.join(convidados)}.''')
        
        # entrada de pauta dos fofoqueiros
        for i in range(len(convidados)):
            pauta = input()

            # comentario da Bia
            if pauta == pautas[0]:
                print('AMIGA, ouça: tem nem o P do PERIGO de você ficar grandona sem querer. Não se preocupe!')
            
            elif pauta == pautas[1]:
                print('Claro que consegue, amiga! Consegue virar uma palhaça, consegue perder a autoestima... Consegue várias coisas :)')

            elif pauta == pautas[2]:
                print('Tem que ter pelo menos dois dias de descanso. Se seu chefe tem uma empresa que não pode passar dois dias fechada porque vai quebrar, ele deveria fechar! Isso não é nem uma empresa, é um quiosque!')
            
            elif pauta == pautas[3]:
                print('Eu detesto quem gosta de ficar pagando de coitadinho(a). Se for chorar… Na verdade, não chora não, que eu não quero nem ouvir.')
            
            elif pauta == pautas[4]:
                print('Vocês ficam dizendo que homem sofre, que homem sofre calado… E por que eu ainda estou ouvindo? Por que eu ainda ouço???')
            
        # entrada de quantos concordam
        concordantes = int(input())

        if concordantes == 0:
            print('Apois me interne, me prenda, me jogue fora que eu tô maluca!')
        
        else:
            print('É isso, eu vejo tanta coisa errada nesse mundo… Mas é como dizem, né?! Life snake, a vida cobra em inglês.')