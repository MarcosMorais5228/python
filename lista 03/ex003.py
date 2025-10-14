print("RECEBA! É hoje que eu me torno o melhor dos melhores.")

sessoes = int(input())
habilidade = int(input())
especiais = ["Rokenedy", "IShowSpeed", "Sérgio Soares", "Neymar Jr", "Gabriel Vasconcelos"]

if 0 <= habilidade <= 5:
    print("A gente tem que começar de algum lugar, né? RECEBA!")
elif 6 <= habilidade <= 15:
    print("Não tem jeito, vou ser o melhor do mundo!")
elif habilidade > 16:
    print("O Pai tá estourado! RECEBA!")

sequencia = input().split('-')
meta = (100 - habilidade) / sessoes
print(f"Meta por Partida: {meta}")

i = 0
while i < sessoes and habilidade <= 100:
    tipo = sequencia[i * 2]
    goleiro = sequencia[i * 2 + 1]

    print(f"TIPO DE PARTIDA: {tipo}")
    print(f"Nome do Goleiro: {goleiro}")

    if goleiro not in especiais:
        hab_goleiro = int(input())

    matriz = eval(input())
    x = int(input())
    y = int(input())

    acertou = matriz[x][y] == 1
    pontos = 0

    if not acertou:
        print("A jornada ainda não acabou!")
    else:
        if goleiro == "Rokenedy":
            print("Aí não dá, impossível de fazer gol no maior do mundo.")
            print("A jornada ainda não acabou!")

        elif goleiro == "IShowSpeed":
            print("REBECA? Is that you?\nIspidi mai friand, recieve!")
            pontos = 1.5 * meta
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

        elif goleiro == "Sérgio Soares":
            print("DALE DALE, PROFESSOR! Quero ver se esse tal de Python é bom mesmo…")
            if tipo == "Batida de Pênalti":
                pontos = meta
                print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")
            else:
                print("A jornada ainda não acabou!")

        elif goleiro == "Neymar Jr":
            print("Ele nem sabe agarrar! A arma dele é a sua fragilidade…")
            pontos = meta / 2
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

        elif goleiro == "Gabriel Vasconcelos":
            print("HAHAHA! Eu pedi um desafio, não uma barra sem goleiro…")
            pontos = 2 * meta
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")

        else:
            # Goleiro comum
            if habilidade > hab_goleiro:
                pontos = habilidade - hab_goleiro
            print("RECEBA! GOLAÇO! É O MELHOR DO MUNDO!")


    habilidade += pontos

    if habilidade > 100:
        print("NÃO TEM JEITO! EU SEMPRE SOUBE QUE IA SER O MELHOR DO MUNDO! RECEBA!")
    

    # Mensagem de meta 
    if habilidade <= 100:
        if pontos >= meta:
            print(f"VAMO! PARTIDA {i+1} DE {sessoes}!")
        else:
            print("Dá pra recuperar depois! Vamo seguindo!")

    i += 1

if habilidade < 100:
    print("Ano que vem tem InterCIn de novo! É só eu treinar mais…")
elif habilidade == 100:
        print("O trono do futebol hoje tem dois reis. Eu e Pelé! Não podia estar com alguém melhor!")