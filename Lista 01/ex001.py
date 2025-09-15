nome_competidor1 = input()
pasteis_competidor1 = int(input())
nome_competidor2 = input()
pasteis_competidor2 = int(input())
nome_competidor3 = input()
pasteis_competidor3 = int(input())


if(pasteis_competidor1 > pasteis_competidor2) and (pasteis_competidor1 > pasteis_competidor3):
    nome_campeao = nome_competidor1
    pasteis_campeao = pasteis_competidor1
elif(pasteis_competidor2 > pasteis_competidor1) and (pasteis_competidor2 > pasteis_competidor3):
    nome_campeao = nome_competidor2
    pasteis_campeao = pasteis_competidor2
elif(pasteis_competidor3 > pasteis_competidor1) and (pasteis_competidor3 > pasteis_competidor2):
    nome_campeao = nome_competidor3
    pasteis_campeao = pasteis_competidor3


if(nome_competidor1 == 'Lineu') or (nome_competidor2 == 'Lineu') or (nome_competidor3 == 'Lineu'):
    nome_campeao = 'Lineu comeu um pastel com gosto estranho e usou sua autoridade na vigilancia sanitaria para acabar com a competição, Beiçola tá desolado!'
    print(nome_campeao)
elif(nome_competidor1 == 'Floriano') or (nome_competidor2 == 'Floriano') or (nome_competidor3 == 'Floriano') and (nome_campeao != 'Floriano'):
    print(f'A(O) campeã(o) é {nome_campeao}, com {pasteis_campeao} pastéis consumidos!')
    print(f'Anos comendo pastel e perdeu justo para {nome_campeao}, lastimável, Sr. Flor!')
elif(nome_campeao == 'Agostinho') and (pasteis_campeao > 100):
    print('Acho que o Agostinho deve ter escondido alguns pastéis na calça, pilantra!')
elif(nome_campeao == 'Agostinho') and (100 > pasteis_campeao > 50):
    print('Agostinho madrugou no taxi e veio cheio de fome para a competição!')
else:
    print(f'A(O) campeã(o) é {nome_campeao}, com {pasteis_campeao} pastéis consumidos!')