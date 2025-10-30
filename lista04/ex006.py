# função de combate
def combate(vida_makoto, mana_makoto, sombras, atk_makoto, golpe_persona, custo_mana, nome_persona):
    turno = 1
    indice_sombra_ataca = 0
    qtd_sombras = len(sombras)
    uso_yukari = 0
    uso_junpei = 0

    vida_makoto += 50
    if vida_makoto > 300:
        vida_makoto = 300

    while vida_makoto > 0 and not todas_derrotadas(sombras):
        mais_um = True
        while mais_um and vida_makoto > 0 and not todas_derrotadas(sombras):
            if todas_derrubadas(sombras) and vida_makoto > 0:
                print('Mitsuru: Todos os inimigos cairam! Avancem com tudo!')
                print('MASS DESTRUCTION!')
                print('Mitsuru: Muito bem! Continuem a exploração.')
                vida_makoto += 50
                if vida_makoto > 300:
                    vida_makoto = 300
                return vida_makoto
            else:
                mais_um = False
                indice_sombra_makoto = 0
                while indice_sombra_makoto < qtd_sombras and (sombras[indice_sombra_makoto][1] <= 0 or sombras[indice_sombra_makoto][4]):
                    indice_sombra_makoto += 1

                else:
                    vida_makoto, mana_makoto, sombras, indice_sombra_makoto, mais_um, uso_yukari, uso_junpei = turno_makoto(
                        vida_makoto, mana_makoto, sombras, indice_sombra_makoto, atk_makoto,
                        golpe_persona, custo_mana, uso_yukari, uso_junpei, nome_persona
                    )


                if not todas_derrotadas(sombras) and mais_um and not todas_derrubadas(sombras):
                    print(f'TURNO {turno}:')
                    print(f'HP Makoto: {vida_makoto} / 300')
                    for i in range(len(sombras)):
                        if sombras[i][1] > 0:
                            print(f'HP {sombras[i][0]}: {sombras[i][1]} pontos de vida restantes')
                    turno += 1

        if vida_makoto > 0:
            encontrou = False
            tentativas = 0
            while not encontrou and tentativas < qtd_sombras:
                sombra = sombras[indice_sombra_ataca]
                if sombra[1] > 0:
                    vida_makoto, sombras = turno_sombra(vida_makoto, sombras, indice_sombra_ataca)
                    encontrou = True
                indice_sombra_ataca = (indice_sombra_ataca + 1) % qtd_sombras
                tentativas += 1
        if not todas_derrotadas(sombras) and vida_makoto > 0 and not todas_derrubadas(sombras):
            print(f'TURNO {turno}:')
            print(f'HP Makoto: {vida_makoto} / 300')
            for i in range(len(sombras)):
                if sombras[i][1] > 0:
                    print(f'HP {sombras[i][0]}: {sombras[i][1]} pontos de vida restantes')
            turno += 1
        
        else:
            if vida_makoto > 0:
                print('Mitsuru: Muito bem! Continuem a exploração.')


    if vida_makoto <= 0:
        print('Makoto: Argh...')
        print('Mitsuru: Líder? Aconteceu algo? Responda!')

    return vida_makoto

# testar se todas foram de arrasta
def todas_derrotadas(sombras):
    for s in sombras:
        if s[1] > 0:
            return False
    return True

# testar se todas foram de menino ney
def todas_derrubadas(sombras):
    for s in sombras:
        if s[4] == False:
            return False
    return True

# turno do makotinho
def turno_makoto(vida_makoto, mana_makoto, sombra, indice_s, atk_makoto, golpe, custo_mana, uso_yukari, uso_junpei, nome_persona):
    poder = poder_numero(golpe)
    print('Makoto: O que fazer...')
    escolha = input()
    mais_um = False

    if escolha == 'persona':
        if mana_makoto < custo_mana:
            print('Makoto: Estou cansado...')
        else:
            lista = [int(x) for x in input().split(' ')]
            resultado, dano = bubble_sort(lista, poder, atk_makoto)
            mana_makoto -= custo_mana

            if indice_s < len(sombra) and sombra[indice_s][1] > 0:
                if resultado == 'fraqueza':
                    dano = round(1.5 * dano)
                    print(f'Makoto: Venha {nome_persona}!')
                    print(f'Mitsuru: Makoto acertou {sombra[indice_s][0]} causando {dano} de dano!')
                    sombra[indice_s][4] = True
                    if not todas_derrubadas(sombras):
                        print('MAIS UM!')
                        print('Mitsuru: Você acertou uma fraqueza! Continue no ataque!')
                    sombra[indice_s][1] -= dano
                    mais_um = True
                    indice_s += 1
                elif resultado == 'acerto':
                    print('Makoto: Persona!')
                    print(f'Mitsuru: Makoto acertou {sombra[indice_s][0]} causando {dano} de dano!')
                    sombra[indice_s][1] -= dano
                else:
                    print('Makoto: O quê?!')
                    print('Mitsuru: Mais foco, Makoto!')

                if indice_s < len(sombra) and sombra[indice_s][1] <= 0:
                    sombra[indice_s][1] = 0
                    print(f'Mitsuru: {sombra[indice_s][0]} foi derrotado!')

    elif escolha == 'atacar':
        if indice_s < len(sombra) and sombra[indice_s][1] > 0:
            dano = damage(2, atk_makoto)
            sombra[indice_s][1] -= dano
            print(f'Mitsuru: Makoto acertou {sombra[indice_s][0]} causando {dano} de dano!')
            if sombra[indice_s][1] <= 0:
                sombra[indice_s][1] = 0
                print(f'Mitsuru: {sombra[indice_s][0]} foi derrotado!')

    elif escolha == 'yukari':
        if uso_yukari >= 2:
            print('Yukari: Estou exausta, foi mal!')
        else:
            cura = 100
            vida_makoto += cura
            if vida_makoto > 300:
                vida_makoto = 300
            uso_yukari += 1
            print('Yukari: Aguenta ai, líder!')
            print('Mitsuru: Bom trabalho, Yukari! Makoto se sente mais revigorado')

    elif escolha == 'junpei':
        if uso_junpei >= 1:
            print('Junpei: Cara, tô cansado!')
        else:
            if indice_s < len(sombra) and sombra[indice_s][1] > 0:
                dano = 100
                sombra[indice_s][1] -= dano
                print('Junpei: HOOOOOME RUUUUN!!')
                print(f'Mitsuru: Acerto CRÍTICO de Junpei! {sombra[indice_s][0]} sofreu 100 de dano!')
                if sombra[indice_s][1] <= 0:
                    sombra[indice_s][1] = 0
                    print(f'Mitsuru: {sombra[indice_s][0]} foi derrotado!')
                else:
                    sombra[indice_s][4] = True
                    indice_s += 1
                mais_um = True
            uso_junpei += 1
            if mais_um:
                if not todas_derrubadas(sombras):
                    print('MAIS UM!')
                    print('Mitsuru: Você acertou uma fraqueza! Continue no ataque!')

    return vida_makoto, mana_makoto, sombra, indice_s, mais_um, uso_yukari, uso_junpei

# turno das sombras
def turno_sombra(vida_makoto, sombras, indice):
    if indice < len(sombras):
        sombra = sombras[indice]
        if sombra[1] > 0 and vida_makoto > 0:
            ataque = int(sombra[2])
            dano = damage(sombra[3], ataque)
            vida_makoto -= dano
            if vida_makoto < 0:
                vida_makoto = 0
            print(f'Mitsuru: Makoto foi atacado por {sombra[0]} e recebeu {dano} de dano!')
            sombra[4] = False
    return vida_makoto, sombras

# calcular dano
def damage(poder, ataque):
    return int(((poder * 15) ** 0.5) * (ataque / 2))

# resolver os bagulhos da lista
def bubble_sort(lista, poder, ataque):
    crescente = list(lista)
    decrescente = list(lista)
    cont_crescente = 0
    cont_decrescente = 0

    for i in range(len(crescente) - 1):
        for j in range(len(crescente) - 1 - i):
            if crescente[j] > crescente[j + 1]:
                crescente[j], crescente[j + 1] = crescente[j + 1], crescente[j]
                cont_crescente += 1

    for i in range(len(decrescente) - 1):
        for j in range(len(decrescente) - 1 - i):
            if decrescente[j] < decrescente[j + 1]:
                decrescente[j], decrescente[j + 1] = decrescente[j + 1], decrescente[j]
                cont_decrescente += 1

    if crescente == lista or decrescente == lista:
        resultado = 'fraqueza'
        dano = damage(poder, ataque)
    elif min(cont_crescente, cont_decrescente) <= 5:
        resultado = 'acerto'
        dano = damage(poder, ataque)
    else:
        resultado = 'erro'
        dano = 0
    return resultado, dano

# transformar nome do golpe em numero
def poder_numero(golpe):
    if golpe in ['Zio', 'Garu', 'Agi', 'Bufu']:
        return 3
    elif golpe in ['Corte', 'Perfuração', 'Pancada']:
        return 4
    elif golpe in ['Zionga', 'Garula', 'Agilao', 'Bufula']:
        return 5


vida_max = 300
mana_max = 70
makoto = vida_max
mana = mana_max
andares_explorados = -1

print('Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.')

while makoto > 0:
    entrada = input().split(' - ')
    nome_persona = entrada[0]
    atk_makoto = int(entrada[1])
    golpe_persona = entrada[2]
    custo_mana = int(entrada[3])
    print(f'{nome_persona}: Eu sou tu e tu és eu...')

    sombras = []
    numero_sombras = int(input())
    for i in range(numero_sombras):
        s = input().split(' - ')
        s[1] = int(s[1])
        s[2] = int(s[2])
        s[3] = poder_numero(s[3])
        s.append(False)
        sombras.append(s)

    print('Mitsuru: Inimigos detectados, se preparem!')
    makoto = combate(makoto, mana, sombras, atk_makoto, golpe_persona, custo_mana, nome_persona)
    andares_explorados += 1

print("\nFIM DE JOGO")
print(f"Andares explorados: {andares_explorados}")
