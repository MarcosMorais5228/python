# função calcculadora de dano
def damage(a, b, c, d):
    if (c == 'Fogo' and d == 'Grama') or (c == 'Água' and d == 'Fogo') or (c == 'Grama' and d == 'Água') or (c == 'Elétrico' and d == 'Água'):
        mult = 2
    
    elif (d == 'Fogo' and c == 'Grama') or (d == 'Água' and c == 'Fogo') or (d == 'Grama' and c == 'Água') or (d == 'Elétrico' and c == 'Água'):
        mult = 0.5
    
    else:
        mult = 1
    
    dano = (a - (b / 2)) * mult
    if dano < 1: dano = 1

    return dano

def turnos(e, f):
    t = 1
    while int(e[2]) > 0 and int(f[2] >0):
        print(f'-- Turno {t} --\n')
        
    

def rodada(g, h):
    num = 1
    print(f'--- Rodada {num} ---')
    print(f'{g[0]}, eu escolho você!')
    print(f'{h[0]}, vai!')
    print('--------------------\n')
    if int(g[7]) > int(h[7]):
        turnos(g, h)
    else:
        turnos(h, g)
    print('--------------------\n')



    

pokemons = []

# receber pokémons
for i in range(4):
    pok = input().split(' - ')
    pokemons.append(pok)

# esolher oponente 
oponente = input()

# definir pokémons do oponente
if oponente == 'lorelei':
    pokemons_inimigo = [
    ["Lapras", "agua", 220, 50, "Raio de Gelo", 60, "agua", 60],
    ["Blastoise", "agua", 180, 55, "Hidro Bomba", 65, "agua", 78],
    ["Victreebel", "grama", 160, 40, "Folha Navalha", 55, "grama", 70],
    ["Ninetales", "fogo", 170, 45, "Lança-chamas", 60, "fogo", 100]
]
elif oponente == 'bruno':
    pokemons_inimigo = [
    ["Charizard", "fogo", 190, 40, "Presa de Fogo", 70, "fogo", 100],
    ["Arcanine", "fogo", 180, 50, "Velocidade Extrema", 60, "fogo", 95],
    ["Kingler", "agua", 170, 60, "Caranguejo Martelo", 65, "agua", 75],
    ["Jolteon", "eletrico", 150, 35, "Choque do Trovão", 55, "eletrico", 130]
]
elif oponente == 'agatha':
    pokemons_inimigo = [
    ["Venusaur", "grama", 180, 50, "Raio Solar", 70, "grama", 80],
    ["Vileplume", "grama", 160, 45, "Pó do Sono", 50, "grama", 50],
    ["Raichu", "eletrico", 160, 40, "Investida Trovão", 65, "eletrico", 110],
    ["Poliwrath", "agua", 190, 55, "Soco Dinâmico", 60, "agua", 70]
]
elif oponente == 'lance':
    pokemons_inimigo = [
    ["Electabuzz", "eletrico", 180, 45, "Soco de Trovão", 75, "eletrico", 105],
    ["Jolteon", "eletrico", 170, 35, "Onda de Trovão", 60, "eletrico", 130],
    ["Exeggutor", "grama", 160, 40, "Bomba de Semente", 65, "grama", 55],
    ["Magmar", "fogo", 175, 40, "Giro de Fogo", 55, "fogo", 93]
]
    

print('''====================
A BATALHA VAI COMEÇAR!
====================''')