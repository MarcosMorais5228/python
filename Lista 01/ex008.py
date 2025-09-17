casos, dias, assistencias, operacoes, especial = int(input()), int(input()), int(input()), int(input()), input()

media = float(casos/dias)

if(especial ==  'sim'):
    tipo_especial = input()

bairro = input()

if(bairro != 'Manhattan') and (bairro != 'Brooklyn'):
    print('Os casos não são nas áreas designadas por Holt. Peralta está desclassificado!')
elif(bairro == 'Manhattan') or (bairro == 'Brooklyn'):
    print('Pelo menos nos bairros corretos Jake está!')
    if(casos < 20):
        print('Vishh, Jake já foi eliminado por não ter o mínimo de casos necessários.')
    else:
        print('Detetive Peralta bateu o mínimo de casos, ele ainda está dentro da competição.')
        if(media < 0.5):
            print('A média diária de casos tá muito baixa, Peralta foi desclassificado.')
        else:
            print('Parece que Jake é bem consistente na sua média diária de casos.')
            if(assistencias < 5):
                print('Desclassificado! Jake precisa ajudar mais os companheiros.')
            else:
                print('Peralta ajudou bastante outros detetives, ele ainda está na competição!')
                if(operacoes < 20):
                    print('Peralta precisa sair mais da delegacia, está faltando ação em campo!')
                else:
                    print('Jake ainda sobrevive por sua participação em campo, será que ele vai levar pra casa o prêmio?')
                    if(especial != 'sim'):
                        print('Para que operação especial quando se tem números, não é?')
                        pontuacao = (casos*2 + assistencias*1.5 +operacoes*0.5)*1.1
                        if(pontuacao >= 70):
                            print('Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?')
                        elif( 40 <= pontuacao < 70):
                            print('Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.')
                        else:
                            print('Muito difícil de Jake ganhar o prêmio.')
                    else:
                        print('Minha nossa! Jake Peralta é realmente um detetive diferenciado.')
                        if(tipo_especial == 'Infiltração'):
                            pontuacao = (casos*2 + assistencias*1.5 +operacoes*0.5)*1.5
                        elif(tipo_especial == 'Escuta'):
                            pontuacao = (casos*2 + assistencias*1.5 +operacoes*0.5)*1.3
                        elif(tipo_especial == 'Invasão'):
                            pontuacao = (casos*2 + assistencias*1.5 +operacoes*0.5)*1.2
                        if(pontuacao >= 70):
                            print('Jake é candidato forte ao prêmio. Será que Holt vai premiá-lo?')
                        elif( 40 <= pontuacao < 70):
                            print('Muito bem! Mas ainda é incerto se vai ser suficiente para ganhar o prêmio.')
                        else:
                            print('Muito difícil de Jake ganhar o prêmio.')    
                
                        