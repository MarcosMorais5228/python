# função de Combate
def combate(vida_makoto, mana_makoto, sombras, atk_makoto, golpe_persona, custo_mana):
    turno = 1
    indice_sombra = 0
    qtd_sombras = len(sombras)
    uso_yukari = 0
    uso_junpei = 0

    while vida_makoto > 0 and not todas_derrotadas(sombras):
        print(f'\nTURNO: {turno}')
        print(f'Makoto: Vida={vida_makoto}, Mana={mana_makoto}')

        # turno de Makoto
        mais_um = True
        while mais_um and vida_makoto > 0 and not todas_derrotadas(sombras):
            vida_makoto, mana_makoto, sombras, mais_um, uso_yukari, uso_junpei = turno_makoto(
                vida_makoto, mana_makoto, sombras, atk_makoto, golpe_persona, custo_mana, uso_yukari, uso_junpei
            )

        # turno de 1 sombra
        if vida_makoto > 0 and not todas_derrotadas(sombras):
            vida_makoto, sombras = turno_sombra(vida_makoto, sombras, indice_sombra)
            indice_sombra += 1
            if indice_sombra >= qtd_sombras:
                indice_sombra = 0

        turno += 1

    if vida_makoto <= 0:
        print('Makoto foi derrotado...')
    else:
        print('Mitsuru: Vitória! Continuem a exploração.')

    return vida_makoto


# função verificar sombras vivas
def todas_derrotadas(sombras):
    for s in sombras:
        if s[1] > 0:
            return False
    return True


# função turno makoto
def turno_makoto(vida_makoto, mana_makoto, sombras, atk_makoto, golpe, custo_mana, uso_yukari, uso_junpei):

    escolha = input()
    mais_um = False

    if escolha == 'persona':
        if mana_makoto < custo_mana:
            print("Makoto: Mana insuficiente para usar a Persona!")
        else:
            lista = input().split(' ')
            poder = poder_numero(golpe)
            resultado, dano = bubble_sort(lista, poder, atk_makoto)
            mana_makoto -= custo_mana
            print(f'Makoto usou {golpe}! (Custo de mana: {custo_mana}) Mana restante: {mana_makoto}')
            atacou = False
            for i in range(len(sombras)):
                if sombras[i][1] > 0 and not atacou:
                    if resultado == 'fraqueza':
                        print(f'Mitsuru: {sombras[i][0]} foi atingida em sua fraqueza!')
                        sombras[i][1] -= dano
                    elif resultado == 'acerto':
                        print(f'Mitsuru: {sombras[i][0]} foi atingida!')
                        sombras[i][1] -= dano
                    else:
                        print(f'Mitsuru: Makoto errou o ataque em {sombras[i][0]}!')
                    if sombras[i][1] <= 0:
                        sombras[i][1] = 0
                        print(f'Mitsuru: {sombras[i][0]} foi derrotada!')
                    atacou = True

    elif escolha == 'atacar':
        atacou = False
        for i in range(len(sombras)):
            if sombras[i][1] > 0 and not atacou:
                dano = atk_makoto
                sombras[i][1] -= dano
                print(f'Makoto atacou {sombras[i][0]} com espada e causou {dano} de dano!')
                if sombras[i][1] <= 0:
                    sombras[i][1] = 0
                    print(f'Mitsuru: {sombras[i][0]} foi derrotada!')
                atacou = True

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
            atacou = False
            for i in range(len(sombras)):
                if sombras[i][1] > 0 and not atacou:
                    dano = 100
                    sombras[i][1] -= dano
                    if sombras[i][1] <= 0:
                        sombras[i][1] = 0
                        print(f'Junpei acertou {sombras[i][0]} e a derrubou!')
                    else:
                        print(f'Junpei causou {dano} de dano em {sombras[i][0]}')
                    atacou = True
            uso_junpei += 1
            mais_um = True  # concede ação extra

    else:
        print("Opção inválida! Perdeu a vez.")

    return vida_makoto, mana_makoto, sombras, mais_um, uso_yukari, uso_junpei


# função turno sombra
def turno_sombra(vida_makoto, sombras, indice):
    if indice < len(sombras):
        sombra = sombras[indice]
        if sombra[1] > 0 and vida_makoto > 0:
            print(f'{sombra[0]} ataca!')
            ataque = int(sombra[2])
            dano = damage(sombra[3], ataque)
            vida_makoto -= dano
            if vida_makoto < 0:
                vida_makoto = 0
            print(f'Mitsuru: Makoto foi atacado por {sombra[0]} e recebeu {dano} de dano!')
    return vida_makoto, sombras


# cálculo de dano
def damage(poder, ataque):
    return int(((poder*15)**0.5)*(ataque/2))


# função para Bubblesort
def bubble_sort(lista, poder, ataque):
    crescente = lista[:]
    decrescente = lista[:]

    cont_crescente = 0
    cont_decrescente = 0

    for i in range(len(crescente)-1):
        for j in range(len(crescente)-1-i):
            if crescente[j] > crescente[j+1]:
                crescente[j], crescente[j+1] = crescente[j+1], crescente[j]
                cont_crescente += 1

    for i in range(len(decrescente)-1):
        for j in range(len(decrescente)-1-i):
            if decrescente[j] < decrescente[j+1]:
                decrescente[j], decrescente[j+1] = decrescente[j+1], decrescente[j]
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



vida_max = 300
mana_max = 70
makoto = vida_max
mana = mana_max

print('Mitsuru: Vamos iniciar nossa exploração, tomem cuidado.')

while makoto > 0:
    entrada = input().split(' - ')
    atk_makoto = int(entrada[1])
    golpe_persona = entrada[2]
    custo_mana = int(entrada[3])
    print(f'{entrada[0]}: Eu sou tu e tu és eu...')

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
    makoto = combate(makoto, mana, sombras, atk_makoto, golpe_persona, custo_mana)
