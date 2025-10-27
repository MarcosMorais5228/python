def great(a):
    if a == 'Golpe Carregado':
        res = -165
    elif a == 'Corte Largo':
        res = -120
    elif a == 'Divisor de Mundos':
        res = -200
    
    return res

def glaive(a):
    if a == 'Corte Aéreo':
        res = -100
    elif a == 'Descida Carregada':
        res = -120
    elif a == 'Kinseto':
        cor = input()
        if cor == 'Vermelho':
            res = -40
        elif cor == 'Amarelo':
            res = -15
        elif cor == 'Verde':
            res = 40
    
    return res

def fuzi(a):
    if a == 'Tiro Carregado':
        res = -90
    elif a == 'Bala de Penetração':
        res = -120
    elif a == 'Tiro Devastador':
        res = -150
    
    return res

def fatalis(a):
    if a == 'Ataque com Cauda':
        res = -55
    elif a == 'Bola de Fogo':
        res = -65
    elif a == 'Mar de Chamas Negras':
        res = 'Mar'
    
    return res

vida_fatalis = 1800
vida_great = 200
vida_glaive = 200
vida_fuzi = 200

print('Hora de Lutar contra a Historia!\n')
for i in range(4):
    if vida_great > 0 and vida_fatalis > 0:
        acao = input()
        dano = great(acao)
        vida_fatalis += dano
    
    if vida_glaive > 0 and vida_fatalis > 0:
        acao = input()
        dano = glaive(acao)
        if dano < 0:
            vida_fatalis += dano
        else:
            vida_glaive += dano
    
    if vida_fuzi > 0 and vida_fatalis > 0:
        acao = input()
        dano = fuzi(acao)
        vida_fatalis += dano

    if vida_fatalis > 0 and (vida_fuzi > 0 or vida_glaive > 0 or vida_great > 0):
        acao = input()
        dano = fatalis(acao)
        if dano == 'Mar':
            status_great = input()
            status_glaive = input()
            status_fuzi = input()

            if status_great == 'Desprotegido':
                vida_great = 0
            if status_glaive == 'Desprotegido':
                vida_glaive = 0
            if status_fuzi == 'Desprotegido':
                vida_fuzi = 0    
        else:
            vida_great += dano
            vida_glaive += dano
            vida_fuzi += dano

if vida_fatalis > 0:
    print('O Fatalis conseguiu sobreviver ao combate...')
    print('O mundo corre perigo!')
else:
    print('Eu não acredito, vocês conseguiram!')
    print('Obrigado caçadores! O mundo está salvo.')