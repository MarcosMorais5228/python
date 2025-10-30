def combate(vida_makoto, mana_makoto, sombras, atk_makoto, golpe_persona, custo_mana, nome_persona):

def todas_derrotadas(sombras):
    for s in sombras:
        if s[1] > 0:
            return False
    return True

def turno_makoto(vida_makoto, mana_makoto, sombra, indice_s, atk_makoto, golpe, custo_mana, uso_yukari, uso_junpei, nome_persona):
    poder = poder_numero(golpe)
    print('Makoto: O que fazer...')

    
def turno_sombra(vida_makoto, sombras, indice):
    

def damage(poder, ataque):
    return int(((poder * 15) ** 0.5) * (ataque / 2))

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
