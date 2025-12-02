# checar permutação
def permutacao(s, nome):
    s = s.lower()
    s = s.replace(' ', '')
    nome = nome.lower()
    nome = nome.replace(' ', '')
    if len(s) != len(nome):
        return False

    contagem = {}

    for caractere in s:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    for caractere in nome:
        if caractere not in contagem:
            return False
        contagem[caractere] -= 1
        if contagem[caractere] < 0:
            return False

    return True

# gerar placar com base nos competidores atuais
def gerar_placar(cadastros):
    placar = ()
    for diva in cadastros:
        placar += ((diva, cadastros[diva]['pontos'], cadastros[diva]['popularidade']),)
    
    placar_ordenado = ()
    for item in placar:
        inseriu = False
        nova_placar = ()
        for existente in placar_ordenado:
            if (item[1] > existente[1]) or (item[1]==existente[1] and item[2]>existente[2]) or (item[1]==existente[1] and item[2] == existente[2] and item[0] < existente[0]):
                if not inseriu:
                    nova_placar += (item,)
                    inseriu = True
                nova_placar += (existente,)
            else:
                nova_placar += (existente,)
        if not inseriu:
            nova_placar += (item,)
        placar_ordenado = nova_placar
    return placar_ordenado

# meus dicionários
divas_estadunidenses = (
    'Olivia Rodrigo',
    'Sabrina Carpenter',
    'Beyoncé', 
    'Taylor Swift',  
    'Lady Gaga', 
    'Azealia Banks', 
    'Katy Perry', 
    'Madonna',
    'Ariana Grande',
    'Mariah Carey',
    'Whitney Houston',
    'Britney Spears',
    'Christina Aguilera',
    'Janet Jackson',
    'Cher',
    'Nicki Minaj',
    'Cardi B',
    'Doja Cat',
    'Billie Eilish'
)

conflitos = {
    'Katy Perry': ('Taylor Swift',),
    'Taylor Swift': ('Katy Perry', 'Ariana Grande', 'Olivia Rodrigo', 'Dua Lipa'),
    'Madonna': ('Lady Gaga',),
    'Lady Gaga': ('Madonna',),
    'Mariah Carey': ('Jennifer Lopez',),
    'Jennifer Lopez': ('Mariah Carey',),
    'Christina Aguilera': ('Britney Spears',),
    'Britney Spears': ('Christina Aguilera',),
    'Nicki Minaj': ('Doja Cat'),
    'Anitta': ('Ludmilla',),
    'Ludmilla': ('Anitta',),
    'Ariana Grande': ('Taylor Swift', 'Cynthia Erivo'),
    'Sabrina Carpenter': ('Camila Cabello', 'Olivia Rodrigo', 'Doja Cat'),
    'Camila Cabello': ('Sabrina Carpenter',),
    'Olivia Rodrigo': ('Taylor Swift', 'Sabrina Carpenter'),
    'Dua Lipa': ('Taylor Swift',),
    'Doja Cat': ('Nicki Minaj', 'Sabrina Carpenter'),
}

# início
print('A BATALHA DAS DIVAS começa... AGORA!\n')

cadastros = {}
entrada = ''
while entrada != 'FIM DAS INSCRIÇÕES':
    entrada = input()
    tentou_burlar = False
    if entrada != 'FIM DAS INSCRIÇÕES':
        cantor, pais, grammy, popularidade, shows_brasil = entrada.split(' - ')
        
        if cantor in cadastros:
            print(f'Só pode ter uma {cantor} na arena. Inscrição duplicada negada!')
        
        else:
            
            if not permutacao('Azealia Banks', cantor):
                pontos = int(grammy)*15 + int(popularidade)*10 + int(shows_brasil)*5

                if cantor in divas_estadunidenses:
                    if pais == 'EUA':
                        print(f'{cantor} acaba de entrar na Batalha das Divas!')
                        print(f'Por excesso de "estrelas e listras", {cantor} recebe uma penalidade de 50 pontos.')
                        pontos -= 50
                
                    elif pais == 'Brasil':
                        print(f'{cantor} acaba de entrar na Batalha das Divas!')
                        print(f'A CASA CAIU! A produção pegou {cantor} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                        pontos -= 100
                
                else: 
                    for diva in divas_estadunidenses:
                        if permutacao(cantor, diva):
                            tentou_burlar = True
                            cantor = diva
                            pais =  'EUA'

                    if tentou_burlar:
                        print(f'{cantor} acaba de entrar na Batalha das Divas!')
                        print(f'A CASA CAIU! A produção pegou {cantor} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                        pontos -= 100
                    
                    elif pais == 'Brasil':
                        print(f'{cantor} acaba de entrar na Batalha das Divas!')
                        print(f'ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {cantor} já larga com 50 pontos de vantagem.')
                        pontos += 50

                if pais != 'EUA' and pais != 'Brasil':
                    print(f'{cantor} acaba de entrar na Batalha das Divas!')
                
                cadastros[cantor] = {
                    'pais': pais,
                    'grammys': int(grammy),
                    'popularidade': int(popularidade),
                    'shows': int(shows_brasil),
                    'pontos': int(pontos)
                    }
                
            else: 
                print(f'Eita, climão! Parece que o histórico de polêmicas de Azealia Banks falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!')

if len(cadastros) > 1:
    # primeira fase
    placar = gerar_placar(cadastros)
    dueladoras = ()
    for i in range(len(placar)):
        dueladoras += (placar[i][0],)
    print('\n=== PLACAR DA 1ª FASE ===')
    for diva, pontos, x in placar:
        print(f'{diva} --- {pontos}')
    print()

    # segunda fase
    divas_para_duelo = ()
    for diva in dueladoras:
        if diva in conflitos:
            for rival in conflitos[diva]:
                if rival in dueladoras and (rival, diva) not in divas_para_duelo:
                    divas_para_duelo += ((diva, rival),)

    if len(divas_para_duelo) > 0:
        print('SALTO ALTO NO TABLADO! HORA DO DUELO!')

        n = 0
        while len(divas_para_duelo) > n:
            if divas_para_duelo[n][0] in cadastros and divas_para_duelo[n][1] in cadastros: 
                print(f'DRAMA! A rivalidade entre {divas_para_duelo[n][0]} e {divas_para_duelo[n][1]} vai ser resolvida no palco, AGORA!')
                
                if cadastros[divas_para_duelo[n][0]]['pontos'] > cadastros[divas_para_duelo[n][1]]['pontos']:
                    print(f'Eliminada(s): {divas_para_duelo[n][1]}')
                    cadastros.pop(divas_para_duelo[n][1])
                
                elif cadastros[divas_para_duelo[n][0]]['pontos'] < cadastros[divas_para_duelo[n][1]]['pontos']:
                    print(f'Eliminada(s): {divas_para_duelo[n][0]}')
                    cadastros.pop(divas_para_duelo[n][0])
                
                elif cadastros[divas_para_duelo[n][0]]['pontos'] == cadastros[divas_para_duelo[n][1]]['pontos']:
                    print(f'Eliminada(s): {divas_para_duelo[n][0]} e {divas_para_duelo[n][1]}')
                    cadastros.pop(divas_para_duelo[n][1])
                    cadastros.pop(divas_para_duelo[n][0])

            n += 1

        # resultado segunda fase
        if len(cadastros) > 0:
            placar = gerar_placar(cadastros)
            print('\n=== PLACAR DA 2ª FASE ===')
            for diva, pontos, x in placar:
                print(f'{diva} --- {pontos}')

    else:
        print('O palco estava montado. Os holofotes, ligados. Mas o conflito não apareceu. Fase 2 cancelada: as divas escolheram reinar em paz.')

    if len(cadastros) != 0:
        # terceira fase
        habilidades_ativas = False
        for diva, x, x in placar:
            if diva in ('Lady Gaga', 'Beyoncé', 'Anitta'):
                habilidades_ativas = True

        if habilidades_ativas and len(cadastros) > 0:
            print('\nO PALCO VAI TREMER! HORA DAS JOGADAS ESPECIAIS!')

            # Lady Gaga - Poker Face
            if 'Lady Gaga' in cadastros:
                placar_atual = gerar_placar(cadastros)
                top3 = ()
                i = 0
                while i < len(placar_atual) and i < 3:
                    top3 += (placar_atual[i][0],)
                    i += 1
                if 'Lady Gaga' not in top3:
                    alvo_encontrado = False
                    j = len(placar_atual) - 1
                    while j >= 0:
                        diva_nome, pontos, pop = placar_atual[j]
                        condicao_pop = pop <= 1.25 * cadastros['Lady Gaga']['popularidade']
                        if diva_nome != 'Lady Gaga' and condicao_pop and not alvo_encontrado:
                            alvo = diva_nome
                            alvo_encontrado = True
                            cadastros['Lady Gaga']['pontos'] += cadastros[alvo]['pontos']
                            print(f'ARRASOU! O blefe de Lady Gaga funcionou! Ela enganou os jurados com seu "Poker Face" e roubou a cena de {alvo}!')
                            cadastros.pop(alvo)
                        j -= 1
                    if not alvo_encontrado:
                        print('QUE REVIRAVOLTA! O público não caiu no "Poker Face" de Lady Gaga! A farsa foi descoberta e ela está eliminada!')
                        cadastros.pop('Lady Gaga')

            # Beyoncé - Formation
            if 'Beyoncé' in cadastros and len(cadastros) >= 3:
                placar_atual = gerar_placar(cadastros)
                mais_fracas = ()
                j = len(placar_atual) - 1
                while j >= 0 and len(mais_fracas) < 2:
                    diva_nome, pontos, pop = placar_atual[j]
                    if diva_nome != 'Beyoncé':
                        mais_fracas += ((diva_nome, pontos),)
                    j -= 1
                soma = mais_fracas[0][1] + mais_fracas[1][1]
                if soma <= cadastros['Beyoncé']['pontos']:
                    k = 0
                    while k < 2:
                        diva_nome, _ = mais_fracas[k]
                        cadastros[diva_nome]['pontos'] = float(cadastros[diva_nome]['pontos']*1.1)
                        k += 1
                    cadastros['Beyoncé']['pontos'] += float(soma*0.1)
                    print('PAREM TUDO! Queen Bey ativou a "Formation"! Ela reorganizou o jogo, elevou as novatas e saiu ainda mais forte!')
                else:
                    print('CHOQUE! A estratégia de Beyoncé foi ousada demais! A "Formation" não convenceu e ela foi desclassificada por manipulação!')
                    cadastros.pop('Beyoncé')

            # Anitta - Envolver
            if 'Anitta' in cadastros and len(cadastros) > 1:
                placar_atual = gerar_placar(cadastros)
                lider = placar_atual[0][0]
                i = 0
                condicao = False
                while i < len(placar_atual) and not condicao:
                    if lider != 'Anitta' and cadastros['Anitta']['popularidade'] >= 0.9 * cadastros[lider]['popularidade']:
                        condicao = True
                    i += 1
                if condicao:
                    diff = cadastros[lider]['pontos'] - cadastros['Anitta']['pontos']
                    pontos_transferidos = float(0.25 * diff)
                    cadastros['Anitta']['pontos'] += float(pontos_transferidos)
                    cadastros[lider]['pontos'] -= float(pontos_transferidos)
                    print(f'A PATROA TÁ ON! Anitta usou "Envolver" e fez {lider} dançar conforme sua música, virando o placar a seu favor!')
                else:
                    print('DEU RUIM! A tentativa de "Envolver" de Anitta não funcionou! O público não comprou a ideia.')

            # resultado terceira fase
            placar_final = gerar_placar(cadastros)
            print('\n=== PLACAR DA 3ª FASE ===')
            for diva, pontos, x in placar_final:
                print(f'{diva} --- {int(pontos)}')

        else:
            placar_final = gerar_placar(cadastros)
            if len(cadastros) > 1:
                print()
                print('Silêncio no palco... Nenhuma habilidade especial foi ativada.')

else: 
    placar_final = gerar_placar(cadastros)
    
# Resultado final
print()
if len(cadastros) == 0:
    print('INACREDITÁVEL! A Batalha das Divas terminou em caos, sem nenhuma vencedora! O palco está vazio... MAS O CALOR DA BRIGA FEZ O IMPOSSÍVEL! O Rei descongelou, subiu ao palco, olhou para a confusão e disse:')
    print('Obrigado pela ajuda, meninas, mas o show já tem atração... e Esse Cara Sou Eu.')
    print('O RÉVEILLON ESTÁ SALVO!')
else:
    vencedora = placar_final[0][0]
    print('=== HABEMUS DIVAM! ===')
    print('A GUERRA ACABOU! A nova dona do palco, a chefe do Réveillon, a única... é ELA!')

    top3 = ()
    i = 0
    while i < len(placar_final) and i < 3:
        top3 += (placar_final[i][0],)
        i += 1
    
    if 'Taylor Swift' in top3 and vencedora != 'Taylor Swift':
        print(f'PARABÉNS, {vencedora[:3].upper()}... TAYLOR SWIFT!!!')
        print('MAS O QUE É ISSO?! Uma reviravolta de última hora! O conselheiro Filipe Moreira acaba de invadir a sala de controle! Alegando fazer parte de uma "comissão cinterna" de Swifties, ele anulou o resultado final e declarou que a verdadeira Era do Réveillon pertence à Taylor Swift! O show está garantido... e a rainha dele também!')
    else:
        print(f'PARABÉNS, {vencedora.upper()}!!! O Rei pode descansar em paz (no gelo), pois o show está garantido!')