# dicionários
pessoa_musicas = {
    "Jake Gyllenhaal": ("All too Well", "We are never ever getting back together", "Red"),
    "Joe Jonas": ("Forever & Always", "Holy Ground"),
    "Taylor Lautner": ("Back to December", "I can see you", "Midnight rain"),
    "Tom Hiddleston": ("Getaway Car",),
    "Joe Alwyn": ("Paper Rings", "Lover", "So Long London"),
    "Harry Styles": ("Style", "Out of the Woods", "All You Had to Do Was Stay"),
    "Travis Kelce": ("The Fate of Ophelia", "The Alchemy", "Wi$h Li$t")
}

eras = {
    "Fearless": (
        "Fearless",
        "Ganhou o VMA 2009, porém Kanye West interrompeu seu discurso de vitória. Também ganhou o Grammy de Álbum do Ano (2010), sendo a artista mais jovem da história (na época) a receber esse prêmio."
    ),

    "Speak Now": (
        "Speak Now",
        "Teve uma turnê mundial massiva que consolidou seu status de superestrela global, o albúm Speak Now vendeu mais de 1 milhão de cópias na primeira semana, superando qualquer outro álbum dos últimos dois anos."
    ),

    "1989": (
        "1989",
        "“1989” tornou-se o primeiro álbum de Taylor exclusivamente pop; a artista emplacou dois hits mundiais: Blank Space e Bad Blood. Fun Fact: Taylor nasceu em 13 de dezembro de 1989."
    ),

    "Reputation": (
        "Reputation",
        "O álbum foi uma resposta à mídia, às traições públicas e ao controle da narrativa sobre sua imagem. Além disso, em 2019, Taylor tem os direitos autorais de seus álbuns roubados."
    ),

    "The Eras Tour": (
        "The Eras Tour",
        "The Eras Tour é uma turnê comemorativa, com detalhes que buscam fazer jus á tudo que Taylor Swift fez e alcançou em seus anos de carreira. No Brasil, aconteceram seis apresentações em novembro de 2023 em São Paulo e no Rio de Janeiro."
    )
}


relacionamentos = {
    2008: "Joe Jonas",
    2009: "Taylor Lautner",
    2010: "Jake Gyllenhaal",
    2012: "Harry Styles",
    2016: "Tom Hiddleston",
    2020: "Joe Alwyn",
    2023: "Travis Kelce"
}

eras_roubadas = []
entrada = ''

# começa aqui 
while entrada != 'Já chega de fatos sobre a Taylor, vai fazer a lista de IP':
    entrada = input()

    # perguntas que dependem da entrada
    if entrada == 'Qual a situação de relacionamento?':
        pessoa = input()
        ano = int(input())

        if relacionamentos[ano] == pessoa:
            print(f'{pessoa} e Taylor Swift estão namorando em {ano}')
        
        else: 
            print(f'{pessoa} e Taylor Swift não estão namorando em {ano}')
    
    elif entrada == 'Qual pessoa está relacionada essa música?':
        musica = input()
        for nome in pessoa_musicas:
            if musica in pessoa_musicas[nome]:
                print(f'A pessoa relacionada é {nome}, Taylor nunca erra em suas músicas')
    
    elif entrada == 'Quais são todas as músicas relacionadas a essa pessoa?':
        pessoa = input()
        print(f'Cartas de amor ou indiretas, as músicas dedicadas a {pessoa} são:', end = ' ')
        print(', '.join(pessoa_musicas[pessoa]))
    
    elif entrada == 'O que aconteceu nessa era?':
        era = input()
        print(eras[era][1])

    elif entrada == 'Wayne nunca deixará Taylor vencer! O CIn precisa manter o hate na diva pop, eu vou alterar as informações':
        print('Cuidado, há um impostor no guia... Informações comprometidas')
        era = input()
        alteração = eras[era][1] + ' Que grande mentira! Taylor Swift só mente'
        eras.update({era : (era, alteração)})
    
    elif entrada == 'Scooter não liga que ela comprou todos os álbuns de volta, ele vai roubar tudo dessa era':
        era = input()
        print(f'Para onde foi a história sobre {era}? Parece que alguém roubou tudo e não avisou a Taylor')
        eras.pop(era)
        eras_roubadas.append(era)

# se tiver roubo
if len(eras_roubadas) > 0:
    print('Big Machine Records roubou:')
    for i in range(len(eras_roubadas)):
        print(eras_roubadas[i])