# função de Combate
def combate(vida_makoto, mana_makoto, sombras, atk_makoto, golpe_persona, custo_mana, nome_persona):
    turno = 1
    indice_sombra_makoto = 0
    indice_sombra_ataca = 0
    qtd_sombras = len(sombras)
    uso_yukari = 0
    uso_junpei = 0

    while vida_makoto > 0 and not todas_derrotadas(sombras):
        # turno de Makoto
        mais_um = True
        while mais_um and vida_makoto > 0 and not todas_derrotadas(sombras):
            # encontra próxima sombra viva para Makoto atacar
            while indice_sombra_makoto < qtd_sombras and sombras[indice_sombra_makoto][1] <= 0:
                indice_sombra_makoto += 1
            if indice_sombra_makoto < qtd_sombras:
                vida_makoto, mana_makoto, sombras[indice_sombra_makoto], mais_um, uso_yukari, uso_junpei = turno_makoto(
                    vida_makoto, mana_makoto, sombras[indice_sombra_makoto], atk_makoto,
                    golpe_persona, custo_mana, uso_yukari, uso_junpei, nome_persona
                )
            else:
                mais_um = False  # nenhuma sombra viva para atacar

            if mais_um:
                print(f'TURNO {turno}:')
                print(f'HP Makoto: {vida_makoto} / 300')
                for i in range(len(sombras)):
                    print(f'HP {sombras[i][0]}: {sombras[i][1]} pontos de vida restantes')
                turno += 1

        # turno de uma sombra atacar Makoto
        if vida_makoto > 0 and not todas_derrotadas(sombras):
            # encontra próxima sombra viva para atacar Makoto
            while indice_sombra_ataca < qtd_sombras and sombras[indice_sombra_ataca][1] <= 0:
                indice_sombra_ataca += 1
            if indice_sombra_ataca < qtd_sombras:
                vida_makoto, sombras = turno_sombra(vida_makoto, sombras, indice_sombra_ataca)
                indice_sombra_ataca += 1
                if indice_sombra_ataca >= qtd_sombras:
                    indice_sombra_ataca = 0

        if vida_makoto > 0 and not todas_derrotadas(sombras):
            print(f'TURNO {turno}:')
            print(f'HP Makoto: {vida_makoto} / 300')
            for i in range(len(sombras)):
                print(f'HP {sombras[i][0]}: {sombras[i][1]} pontos de vida restantes')

        turno += 1

    if vida_makoto <= 0:
        print('Makoto: Argh...')
        print('Mitsuru: Líder? Aconteceu algo? Responda!')
    else:
        print('Mitsuru: Muito bem! Continuem a exploração.')
        vida_makoto += 50
        if vida_makoto > 300:
            vida_makoto = 300

    return vida_makoto


# função verificar sombras vivas
def todas_derrotadas(sombras):
    for s in sombras:
        if s[1] > 0:
            return False
    return True


# função turno makoto
def turno_makoto(vida_makoto, mana_makoto, sombra, atk_makoto, golpe, custo_mana, uso_yukari, uso_junpei, nome_persona):
    poder = poder_numero(golpe)
    print('Makoto: O que fazer...')

    escolha = input()
    mais_um = False

    if escolha == 'persona':
        if mana_makoto < custo_mana:
            print("Makoto: Mana insuficiente para usar a Persona!")
        else:
            lista = input().split(' ')
            resultado, dano = bubble_sort(lista, poder, atk_makoto)
            mana_makoto -= custo_mana

            if sombra[1] > 0:
                if resultado == 'fraqueza':
                    dano = int(1.5 * dano)
                    print(f'Makoto: Venha {nome_persona}!')
                    print(f'Mitsuru: Makoto acertou {sombra[0]} causando {dano} de dano!')
                    print('MAIS UM!')
                    print('Mitsuru: Você acertou uma fraqueza! Continue no ataque!')
                    sombra[1] -= dano
                    mais_um = True
                elif resultado == 'acerto':
                    print('Makoto: Persona!')
                    print(f'Mitsuru: Makoto acertou {sombra[0]} causando {dano} de dano!')
                    sombra[1] -= dano
                else:
                    print('Makoto: O quê?!')
                    print('Mitsuru: Mais foco, Makoto!')

                if sombra[1] <= 0:
                    sombra[1] = 0
                    print(f'Mitsuru: {sombra[0]} foi derrotado!')

    elif escolha == 'atacar':
        if sombra[1] > 0:
            dano = damage(2, atk_makoto)
            sombra[1] -= dano
            print(f'Mitsuru: Makoto acertou {sombra[0]} causando {dano} de dano!')
            if sombra[1] <= 0:
                sombra[1] = 0
                print(f'Mitsuru: {sombra[0]} foi derrotado!')

    elif escolha == 'yukari':
        if uso_yukari >= 2:
            print("Yukari não pode ser chamada novamente neste combate!")
        else:
            cura = 100
            vida_makoto += cura
            if vida_makoto > 300:
                vida_makoto = 300
            uso_yukari += 1
            print(f'Yukari curou Makoto em {cura} pontos de vida! Vida atual: {vida_makoto}')

    elif escolha == 'junpei':
        if uso_junpei >= 1:
            print("Junpei já foi chamado neste combate!")
        else:
            for i in range(len(sombra)):
                if sombra[1] > 0:
                    dano = 100
                    sombra[1] -= dano
                    if sombra[1] <= 0:
                        sombra[1] = 0
                        print(f'Junpei acertou {sombra[0]} e a derrubou!')
                    else:
                        print(f'Junpei causou {dano} de dano em {sombra[0]}')
                    mais_um = True
            uso_junpei += 1
            if mais_um:
                print('MAIS UM!')

    else:
        print("Opção inválida! Perdeu a vez.")

    return vida_makoto, mana_makoto, sombra, mais_um, uso_yukari, uso_junpei


# função turno sombra
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
    return vida_makoto, sombras


# cálculo de dano
def damage(poder, ataque):
    return int(((poder * 15) ** 0.5) * (ataque / 2))


# função para bubble sort
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


# função substituir tipo de golpe por número
def poder_numero(golpe):
    if golpe in ['Zio', 'Garu', 'Agi', 'Bufu']:
        return 3
    elif golpe in ['Corte', 'Perfuração', 'Pancada']:
        return 4
    elif golpe in ['Zionga', 'Garula', 'Agilao', 'Bufula']:
        return 5


# --- MAIN ---

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

    # sombras
    sombras = []
    numero_sombras = int(input())
    for i in range(numero_sombras):
        s = input().split(' - ')
        s[1] = int(s[1])
        s[2] = int(s[2])
        s[3] = poder_numero(s[3])
        sombras.append(s)

    print('Mitsuru: Inimigos detectados, se preparem!')
    makoto = combate(makoto, mana, sombras, atk_makoto, golpe_persona, custo_mana, nome_persona)

    andares_explorados += 1

print("\nFIM DE JOGO")
print(f"Andares explorados: {andares_explorados}")
