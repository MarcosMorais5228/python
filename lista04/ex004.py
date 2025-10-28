# função calculadora de dano
def damage(ataque, defesa, tipo_atacante, tipo_alvo):
    # super efetivo
    if (tipo_atacante == 'fogo' and tipo_alvo == 'grama') or (tipo_atacante == 'agua' and tipo_alvo == 'fogo') or (tipo_atacante == 'grama' and tipo_alvo == 'agua') or (tipo_atacante == 'eletrico' and tipo_alvo == 'agua'):
        mult = 2
        proporcao = 'é super efetivo!'

    # não muito efetivo...
    elif (tipo_alvo == 'fogo' and tipo_atacante == 'grama') or (tipo_alvo == 'agua' and tipo_atacante == 'fogo') or (tipo_alvo == 'grama' and tipo_atacante == 'agua') or (tipo_alvo == 'eletrico' and tipo_atacante == 'agua'):
        mult = 0.5
        proporcao = 'não é muito efetivo...'

    else:
        mult = 1
        proporcao = 'N/A'

    dano = (int(ataque) - (int(defesa) / 2)) * mult
    if dano < 1:
        dano = 1

    return [int(dano), proporcao]

# função turnos
def turnos(equipe, inimigos, ii, jj):
    turno = 1
    while int(equipe[ii][2]) > 0 and int(inimigos[jj][2]) > 0:
        print(f'-- Turno {turno} --\n')

        # equipe ataca primeiro
        if int(equipe[ii][7]) >= int(inimigos[jj][7]):
            if int(equipe[ii][2]) > 0:
                print(f'{equipe[ii][0]} usa {equipe[ii][4]}!')
                dano = damage(equipe[ii][5], inimigos[jj][3], equipe[ii][1], inimigos[jj][1])
                inimigos[jj][2] = max(0, inimigos[jj][2] - dano[0])
                if dano[1] != 'N/A':
                    print(f'{equipe[ii][4]} {dano[1]}')
                print(f'Causou {dano[0]} de dano. HP de {inimigos[jj][0]} agora é {inimigos[jj][2]}/{inimigos[jj][8]}.\n')

            if int(inimigos[jj][2]) > 0:
                print(f'{inimigos[jj][0]} do oponente usa {inimigos[jj][4]}!')
                dano = damage(inimigos[jj][5], equipe[ii][3], inimigos[jj][1], equipe[ii][1])
                equipe[ii][2] = max(0, int(equipe[ii][2]) - dano[0])
                if dano[1] != 'N/A':
                    print(f'{inimigos[jj][4]} {dano[1]}')
                print(f'Causou {dano[0]} de dano. HP de {equipe[ii][0]} agora é {equipe[ii][2]}/{equipe[ii][8]}.\n')

        # inimigo ataca primeiro
        else:
            if int(inimigos[jj][2]) > 0:
                print(f'{inimigos[jj][0]} do oponente usa {inimigos[jj][4]}!')
                dano = damage(inimigos[jj][5], equipe[ii][3], inimigos[jj][1], equipe[ii][1])
                equipe[ii][2] = max(0, int(equipe[ii][2]) - dano[0])
                if dano[1] != 'N/A':
                    print(f'{inimigos[jj][4]} {dano[1]}')
                print(f'Causou {dano[0]} de dano. HP de {equipe[ii][0]} agora é {equipe[ii][2]}/{equipe[ii][8]}.\n')

            if int(equipe[ii][2]) > 0:
                print(f'{equipe[ii][0]} usa {equipe[ii][4]}!')
                dano = damage(equipe[ii][5], inimigos[jj][3], equipe[ii][1], inimigos[jj][1])
                inimigos[jj][2] = max(0, int(inimigos[jj][2]) - dano[0])
                if dano[1] != 'N/A':
                    print(f'{equipe[ii][4]} {dano[1]}')
                print(f'Causou {dano[0]} de dano. HP de {inimigos[jj][0]} agora é {inimigos[jj][2]}/{inimigos[jj][8]}.\n')

        # mensagem derrota
        if int(equipe[ii][2]) == 0:
            print(f'{equipe[ii][0]} foi derrotado!\n')
        if int(inimigos[jj][2]) == 0:
            print(f'{inimigos[jj][0]} do oponente foi derrotado!\n')

        turno += 1

# função rodadas
def rodada(equipe, inimigos):
    i = 0
    j = 0
    num = 1
    vitorias_jogador = 0
    vitorias_inimigo = 0

    while i < len(equipe) and j < len(inimigos):
        print(f'--- Rodada {num} ---')
        print(f'{equipe[i][0]}, eu escolho você!')
        print(f'{inimigos[j][0]}, vai!')
        print('--------------------\n')

        turnos(equipe, inimigos, i, j)

        # placar
        if int(equipe[i][2]) == 0:
            i += 1
            vitorias_inimigo += 1
        if int(inimigos[j][2]) == 0:
            j += 1
            vitorias_jogador += 1

        num += 1
        print('--------------------\n')
        print(f'Placar: {vitorias_jogador} X {vitorias_inimigo}\n')

    # resultado
    print('========================================')
    if vitorias_jogador > vitorias_inimigo:
        print('Parabéns! Você venceu a batalha Pokémon!')
    else:
        print('Que pena! Você foi derrotado.')
    print('========================================')


# pokémons equipe
pokemons = []
print('Hora de montar seu time Pokémon!\n')
for k in range(4):
    pok = input().split(' - ')
    # criei mais um HP pra servir de HP máximo nas impressões de vida
    pok.append(pok[2])
    pokemons.append(pok)

# oponente
print('Qual membro da Elite Four você deseja enfrentar?\n')
oponente = input()

# pokémons oponente
if oponente == 'lorelei':
    pokemons_inimigo = [
        ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60, 220],
        ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78, 180],
        ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70, 160],
        ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100, 170]
    ]
elif oponente == 'bruno':
    pokemons_inimigo = [
        ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100, 190],
        ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95, 180],
        ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75, 170],
        ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130, 150]
    ]
elif oponente == 'agatha':
    pokemons_inimigo = [
        ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80, 180],
        ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50, 160],
        ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110, 160],
        ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70, 190]
    ]
elif oponente == 'lance':
    pokemons_inimigo = [
        ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105, 180],
        ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130, 170],
        ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55, 160],
        ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93, 175]
    ]

# início
print('''====================
A BATALHA VAI COMEÇAR!
====================\n''')

rodada(pokemons, pokemons_inimigo)
