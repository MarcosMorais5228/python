def permutacao(s, nome):
    if len(s) != len(nome):
        return False

    contagem = {}

    # conta caracteres de s
    for caractere in s:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    # subtrai usando nome
    for caractere in nome:
        if caractere not in contagem:
            return False
        contagem[caractere] -= 1
        if contagem[caractere] < 0:
            return False

    return True

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

print('A BATALHA DAS DIVAS começa... AGORA!')

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
            print(f'{cantor} acaba de entrar na Batalha das Divas!')
            if not permutacao('Azealia Banks', cantor):
                pontos = int(grammy)*15 + int(popularidade)*10 + int(shows_brasil)*5

                if cantor in divas_estadunidenses:
                    if pais == 'EUA':
                        print(f'Por excesso de "estrelas e listras", {cantor} recebe uma penalidade de 50 pontos.')
                        pontos -= 50
                
                    elif pais == 'Brasil':
                        print(f'A CASA CAIU! A produção pegou {cantor} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                        pontos -= 100
                
                else: 
                    for diva in divas_estadunidenses:
                        if permutacao(cantor, diva):
                            tentou_burlar = True
                            cantor = diva

                    if tentou_burlar:
                        print(f'A CASA CAIU! A produção pegou {cantor} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                        pontos -= 100
                    
                    elif pais == 'Brasil':
                        print(f'ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {cantor} já larga com 50 pontos de vantagem.')
                        pontos += 50
                
                cadastros[cantor] = {
                    'pais': pais,
                    'grammys': int(grammy),
                    'popularidade': int(popularidade),
                    'shows': int(shows_brasil),
                    'pontos': int(pontos)
                    }
                
            else: 
                print(f'Eita, climão! Parece que o histórico de polêmicas de {cantor} falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!')


placar = gerar_placar(cadastros)
dueladoras = ()
for i in range(len(placar)):
    dueladoras += (placar[i][0],)
print(dueladoras)
print('\n=== PLACAR DA 1ª FASE ===')
for diva, pontos, x in placar:
    print(f'{diva} --- {pontos}')
print()

divas_para_duelo = ()
for diva in dueladoras:
    if diva in conflitos:
        for rival in conflitos[diva]:
            if rival in dueladoras and (rival, diva) not in divas_para_duelo:
                divas_para_duelo += ((diva, rival),)
print(divas_para_duelo)

if len(divas_para_duelo) > 0:
    print('SALTO ALTO NO TABLADO! HORA DO DUELO!')

    n = 0
    while len(divas_para_duelo) > 0:
        if divas_para_duelo[n][0] in cadastros and divas_para_duelo[n][1] in cadastros: 
            print(f'DRAMA! A rivalidade entre {divas_para_duelo[n][0]} e {divas_para_duelo[n][1]} vai ser resolvida no palco, AGORA!')
            
            if cadastros[divas_para_duelo[n][0]]['pontos'] > cadastros[divas_para_duelo[n][1]]['pontos']:
                print(f'Eliminada(s): {divas_para_duelo[n][1]}')
                cadastros.pop(divas_para_duelo[n][1])
                for i in range(len(divas_para_duelo)):
                    if divas_para_duelo[n][1] in divas_para_duelo[i]:
                        a =1
            
            elif cadastros[divas_para_duelo[n][0]]['pontos'] < cadastros[divas_para_duelo[n][1]]['pontos']:
                print(f'Eliminada(s): {divas_para_duelo[n][0]}')
                cadastros.pop(divas_para_duelo[n][0])
            
            elif cadastros[divas_para_duelo[n][0]]['pontos'] == cadastros[divas_para_duelo[n][1]]['pontos']:
                print(f'Eliminada(s): {divas_para_duelo[n][0]} e  {divas_para_duelo[n][1]}')
                cadastros.pop(divas_para_duelo[n][1])