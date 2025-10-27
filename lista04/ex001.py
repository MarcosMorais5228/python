def batalha(a):
    # ataques
    if a == 'Você não tem o que é necessário para escalar.':
        print('Eu nunca vou conseguir chegar ao topo :(')
    
    elif a == 'NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!':
        print('NAAÃO EU NUNCA DEVERIA TER INVENTADO DE ESCALAR ESSA MONTANHA!')
    
def subtracao(a,c):
    if a == 'Você não tem o que é necessário para escalar.':
        c = -20
    
    elif a == 'NÓS NUNCA DEVERÍAMOS TER SAÍDO DE CASA! VAMOS MORRER NESSA MONTANHA!':
        c= -50
    
    return c

def soma(b, c):
    if b == 'Calma Badeline, nós vamos conseguir.':
        c = 25

    elif b == 'Eu sei que somos capazes! Vamos em frente!':
        respiracoes = int(input())
        c = respiracoes*10
    
    elif b == 'Madeline, nós estamos com você. Continue!':
        c = 60
    
    return c

vida = 100

while vida > 0 and vida < 150:
    ataque = input()
    batalha(ataque)
    res = subtracao(ataque, vida)
    vida += res

    if vida > 0 and vida < 150:
        reacao = input()
        res = soma(reacao, vida)
        vida += res

if vida >= 150:
    print('Madeline chegou ao topo! Ela se senta em um banco para descansar e apreciar a vista.')

if vida <= 0:
    print('Madeline e Badeline não conseguiram se entender... parece que elas nunca vão ver a cidade de cima.')
