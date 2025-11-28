def permutacao(s, nome):
    if len(s) != len(nome):
        return False

    contagem = {}  # dicionário de contagem

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

cadastros = {}
n = 0

entrada = ''
while entrada != 'FIM DAS INSCRIÇÕES':
    entrada = input()
    tentou_burlar = False
    if entrada != 'FIM DAS INSCRIÇÕES':
        cantor, pais, grammy, popularidade, shows_brasil = entrada.split(' - ')
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
            
            elif cantor not in divas_estadunidenses:
                for diva in divas_estadunidenses:
                    if permutacao(cantor, diva):
                        tentou_burlar = True

                if tentou_burlar:
                    print(f'A CASA CAIU! A produção pegou {cantor} no pulo do gato tentando se livrar da penalidade! Por essa tentativa de malandragem, o preço veio dobrado.')
                    pontos -= 100
                
                elif pais == 'Brasil':
                    print(f'ESSA TEM O TEMPERO BRASILEIRO! Por jogar em casa, {cantor} já larga com 50 pontos de vantagem.')
                    pontos += 50

            cadastros.update({n:(cantor,pontos)})
            n += 1


        
        else: 
            print(f'Eita, climão! Parece que o histórico de polêmicas de {cantor} falou mais alto. A produção barrou a entrada e aqui no Brasil ela não canta!')

fase = 1
while len(cadastros) >= 2:
    print(f'=== PLACAR DA {fase}ª FASE ===')
    for i in range(len(cadastros)):
        print(f'{cadastros[i][0]} --- {cadastros[i][1]}')

    break