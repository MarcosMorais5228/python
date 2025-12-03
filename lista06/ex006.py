# pra essa questão eu usei 1 como true e 0 como false pra não ter que ficar digitndo true/false o tempo todo pq são 600 LINHAS

eras = {
    "Future Nostalgia": {"Diva": "Dua Lipa", "Musicas": ("Future Nostalgia", "Don't Start Now", "Cool", "Physical", "Levitating", "Pretty Please", "Hallucinate", "Love Again", "Break My Heart", "Good in Bed", "Boys Will Be Boys", "Fever")},
    "Radical Optimism": {"Diva": "Dua Lipa", "Musicas": ("End of an Era", "Houdini", "Training Season", "These Walls", "Whatcha Doing", "French Exit", "Illusion", "Falling Forever", "Anything for Love", "Maria", "Happy for You")},
    "SOUR": {"Diva": "Olivia Rodrigo", "Musicas": ("Brutal", "Traitor", "Drivers License", "1 Step Forward, 3 Back", "Deja Vu", "Good 4 U", "Enough For You", "Happier", "Jealousy, Jealousy", "Favorite Crime", "Hope Ur Ok")},
    "GUTS": {"Diva": "Olivia Rodrigo", "Musicas": ("All-American Bitch", "Bad Idea Right?", "Vampire", "Lacy", "Ballad Of A Homeschooled Girl", "Making The Bed", "Logical", "Get Him Back!", "Love Is Embarrassing", "The Grudge", "Pretty Isn't Pretty", "Teenage Dream")},
    "Teenage Dream": {"Diva": "Katy Perry", "Musicas": ("Teenage Dream", "Last Friday Night (T.G.I.F.)", "California Gurls", "Firework", "Peacock", "Circle the Drain", "The One That Got Away", "E.T.", "Who Am I Living For?", "Pearl", "Hummingbird Heartbeat", "Not Like the Movies")},
    "Prism": {"Diva": "Katy Perry", "Musicas": ("Roar", "Legendary Lovers", "Birthday", "Walking on Air", "Unconditionally", "Dark Horse", "This Is How We Do", "International Smile", "Ghost", "Love Me", "This Moment", "Double Rainbow", "By theGrace of God")}
}

divas_musicas = {
    'Dua Lipa' : ("Future Nostalgia",
"Don't Start Now",
"Cool","Physical",
"Levitating",
"Pretty Please",
"Hallucinate",
"Love Again",
"Break My Heart",
"Good in Bed",
"Boys Will Be Boys",
"Fever", "End of an Era",
"Houdini",
"Training Season",
"These Walls",
"Whatcha Doing",
"French Exit",
"Illusion",
"Falling Forever",
"Anything for Love",
"Maria",
"Happy for You"),
    'Olivia Rodrigo' : ("Brutal","Traitor",
"Drivers License",
"1 Step Forward, 3 Steps Back",
"Deja Vu",
"Good 4 U",
"Enough For You",
"Happier",
"Jealousy, Jealousy",
"Favorite Crime",
"Hope Ur Ok", "All-American Bitch",
"Bad Idea Right?", 
"Vampire", 
"Lacy", 
"Ballad Of A Homeschooled Girl",
 "Making The Bed", 
"Logical", 
"Get Him Back!", 
"Love Is Embarrassing", 
"The Grudge", 
"Pretty Isn't Pretty", 
"Teenage Dream"),
    'Katy Perry' : ("Teenage Dream", 
"Last Friday Night (T.G.I.F.)", 
"California Gurls", 
"Firework", 
"Peacock", 
"Circle the Drain", 
"The One That Got Away", 
"E.T.", 
"Who Am I Living For?", 
"Pearl", 
"Hummingbird Heartbeat", 
"Not Like the Movies", "Roar", 
"Legendary Lovers", 
"Birthday", 
"Walking on Air", 
"Unconditionally", 
"Dark Horse", 
"This Is How We Do", 
"International Smile", 
"Ghost", 
"Love Me", 
"This Moment", 
"Double Rainbow", 
"By theGrace of God")
}

divas = ("Dua Lipa", "Olivia Rodrigo", "Katy Perry")
divas_conjunto = {}
i = 0
while i < len(divas):
    divas_conjunto[divas[i]] = 1
    i = i + 1

dados_divas = {}
i = 0
while i < len(divas):
    diva = divas[i]
    dados_divas[diva] = {"Streams": 0, "Musicas_Contadas": 0, "Musicas_Aceitas": {}}
    i = i + 1

# variáveis do estado inicial
musicas_aceitas_parte1 = {} 
contador_musicas_por_era = {}
i = 0
chaves_eras = tuple(eras.keys())
while i < len(chaves_eras):
    contador_musicas_por_era[chaves_eras[i]] = 0
    i = i + 1

total_musicas_validas = 0
diva_campea_podio = ""
sistema_parado = 0 
votos_musicas_parte2 = {} 
musica_campea = ""
diva_musica_campea = ""
votos_popular = {}
votos_por_fa = {}

def numerico(s):

    if len(s) == 0:
        return 0 
    
    i = 0
    numero = 1
    while i < len(s):
        char_code = ord(s[i])
        if char_code < 48 or char_code > 57:
            numero = 0 
        i = i + 1
    return numero

def descriptografar_cesar(texto_cifrado, chave):
    texto_descriptografado = ""
    chave_descripto = chave % 26
    
    i = 0
    while i < len(texto_cifrado):
        caractere = texto_cifrado[i]
        
        if ord('A') <= ord(caractere) <= ord('Z'):
            novo_ord = ((ord(caractere) - ord('A') - chave_descripto) % 26) + ord('A')
            texto_descriptografado = texto_descriptografado + chr(novo_ord)
        elif ord('a') <= ord(caractere) <= ord('z'):
            novo_ord = ((ord(caractere) - ord('a') - chave_descripto) % 26) + ord('a')
            texto_descriptografado = texto_descriptografado + chr(novo_ord)
        else:
            texto_descriptografado = texto_descriptografado + caractere
        
        i = i + 1
    return texto_descriptografado

def separar_e_limpar(linha):

    partes_lista = linha.split(' - ')
    
    partes_limpas_tupla = () 
    i = 0
    while i < len(partes_lista):
        parte = partes_lista[i]
        inicio = 0
        fim = len(parte)
        
        while inicio < fim and parte[inicio] == ' ':
            inicio = inicio + 1
        
        while fim > inicio and parte[fim-1] == ' ':
            fim = fim - 1
            
        parte_limpa = parte[inicio:fim]
        
        partes_limpas_tupla = partes_limpas_tupla + (parte_limpa,)
        i = i + 1
        
    return partes_limpas_tupla


def simular_troca_em_tupla(dados_tupla, j):
    
    elem_a = dados_tupla[j]
    elem_b = dados_tupla[j+1]
    
    prefixo = dados_tupla[:j]
    
    trocado = (elem_b, elem_a)
    
    sufixo = dados_tupla[j + 2:]
    
    return prefixo + trocado + sufixo

def ordenar_podio(dados_tupla):
    
    n = len(dados_tupla)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            d1 = dados_tupla[j]
            d2 = dados_tupla[j+1]

            menor = d1[0] < d2[0] 
            menor_igual_1 = (d1[0] == d2[0]) and (d1[1] < d2[1]) 
            menor_igual_2 = (d1[0] == d2[0]) and (d1[1] == d2[1]) and (d1[2] > d2[2]) 


            if menor or menor_igual_1 or menor_igual_2:
                dados_tupla = simular_troca_em_tupla(dados_tupla, j)
            
            j = j + 1
        i = i + 1
        
    return dados_tupla

def ordenar_musica(dados_tupla):
    
    n = len(dados_tupla)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            m1 = dados_tupla[j]
            m2 = dados_tupla[j+1]
            
            menor = m1[0] < m2[0]
            menor_igual_1 = (m1[0] == m2[0]) and (m1[1] < m2[1])
            menor_igual_2 = (m1[0] == m2[0]) and (m1[1] == m2[1]) and (m1[2] < m2[2])
            menor_igual_3 = (m1[0] == m2[0]) and (m1[1] == m2[1]) and (m1[2] == m2[2]) and (m1[3] > m2[3])
            menor_igual_4 = (m1[0] == m2[0]) and (m1[1] == m2[1]) and (m1[2] == m2[2]) and (m1[3] == m2[3]) and (m1[4] > m2[4])

            if menor or menor_igual_1 or menor_igual_2 or menor_igual_3 or menor_igual_4:

                dados_tupla = simular_troca_em_tupla(dados_tupla, j)
            
            j = j + 1
        i = i + 1
        
    return dados_tupla

def ordenar_diva_final(dados_tupla):
    
    n = len(dados_tupla)
    i = 0
    while i < n - 1:
        j = 0
        while j < n - i - 1:
            d1 = dados_tupla[j]
            d2 = dados_tupla[j+1]

            menor = d1[0] < d2[0]
            menor_igual_1 = (d1[0] == d2[0]) and (d1[1] < d2[1])
            menor_igual_2 = (d1[0] == d2[0]) and (d1[1] == d2[1]) and (d1[2] < d2[2])
            menor_igual_3 = (d1[0] == d2[0]) and (d1[1] == d2[1]) and (d1[2] == d2[2]) and (d1[3] > d2[3])

            if menor or menor_igual_1 or menor_igual_2 or menor_igual_3:

                dados_tupla = simular_troca_em_tupla(dados_tupla, j)
            
            j = j + 1
        i = i + 1
        
    return dados_tupla


def processar_parte1(eras, divas_conjunto, dados_divas, contador_musicas_por_era):
    
    print("Vai começar a disputa das DIVAS")

    total_musicas_validas = 0
    sistema_parado = 0
    musicas_aceitas_parte1 = {} 
    
    continuar_lendo = 1
    while continuar_lendo:
        linha = input()
        
        if linha == "FIM":
            continuar_lendo = 0
        
        if continuar_lendo:
            partes = separar_e_limpar(linha)
            formato_entrada_valido = (len(partes) == 4)
            valido = formato_entrada_valido
            
            musica = ""
            diva = ""
            era = ""
            streams_str = ""
            streams = 0

            if formato_entrada_valido:
                musica = partes[0]
                diva = partes[1]
                era = partes[2]
                streams_str = partes[3]
                
                stream_numerico = numerico(streams_str)
                if stream_numerico:
                    streams = int(streams_str)
                else:
                    valido = 0
            
            # validação da era em disputa
            if valido:
                if era not in eras:
                    print("Essa Era não esta na disputa, tente novamete!")
                    valido = 0

            # validação da música na era
            if valido:
                musicas_da_era = eras[era]['Musicas']
                musica_encontrada = 0
                i = 0
                while i < len(musicas_da_era):
                    if musica == musicas_da_era[i]:
                        musica_encontrada = 1
                    i = i + 1
                
                if musica_encontrada == 0:
                    print('Essa musica não pertence a essa ERA, tente novamente!')
                    valido = 0

            # validação da diva
            if valido:
                if diva not in divas_conjunto:
                    print("Diva errada, tente novamente!")
                    valido = 0
            
            
            # validação da diva da era
            if valido:
                if diva != eras[era]['Diva']:
                    print("Diva errada, tente novamente!")
                    valido = 0
                
            # validação de limite de músicas por era
            if valido:
                if contador_musicas_por_era.get(era, 0) >= 3:
                    print("Quantidade maxima de musicas dessa era atingida")
                    valido = 0

            # validação se repete músia
            if valido:
                if musica in musicas_aceitas_parte1 and musica != 'Teenage Dream':
                    print("A musica ja foi mencionada")
                    valido = 0

            if valido:
                total_musicas_validas = total_musicas_validas + 1
                
                # atualiza dados da diva
                dados_divas[diva]['Streams'] = dados_divas[diva]['Streams'] + streams
                dados_divas[diva]['Musicas_Contadas'] = dados_divas[diva]['Musicas_Contadas'] + 1
                
                # atualiza contadores e catálogo
                contador_musicas_por_era[era] = contador_musicas_por_era[era] + 1
                musicas_aceitas_parte1[musica] = diva
                dados_divas[diva]['Musicas_Aceitas'][musica] = streams

    # impressão do pódio e veredito
    if total_musicas_validas == 0:
        print("Essa batalha foi 'Houdini', sumiu! Sem músicas, sem disputa.")
        sistema_parado = 1
    
    diva_campea_podio = ""
    if sistema_parado == 0:
        diva_campea_podio = imprimir_podio_parte1(divas, dados_divas)
        
    return (total_musicas_validas, sistema_parado, musica_campea, diva_campea_podio, dados_divas, musicas_aceitas_parte1)


def imprimir_podio_parte1(divas, dados_divas):
    
    podio_bruto_tupla = ()
    i = 0
    while i < len(divas):
        diva = divas[i]
        dados = dados_divas[diva]
        streams = dados['Streams']
        musicas = dados['Musicas_Contadas']
        
        media = 0
        if musicas > 0:
            media = streams // musicas
        
        novo_item = (media, musicas, diva)
        podio_bruto_tupla = podio_bruto_tupla + (novo_item,)
        i = i + 1
        
    podio_ordenado = ordenar_podio(podio_bruto_tupla)

    # impressão do pódio
    print("===== Pódio =====")
    i = 0
    while i < len(podio_ordenado):
        media = podio_ordenado[i][0]
        diva = podio_ordenado[i][2]
        print(f"{i+1}° {diva} com {media} Streams por música")
        i = i + 1

    # veredito da campeã
    diva_campea_podio = podio_ordenado[0][2]
    
    if diva_campea_podio == "Katy Perry":
        print("Katy Perry 'ruge'! Os KatyCats provam que 'Teenage Dream' e 'Prism' são eternos!")
    elif diva_campea_podio == "Olivia Rodrigo":
        print("É 'brutal' aqui! Os Livies mostraram a força de 'SOUR' e 'GUTS'.")
    elif diva_campea_podio == "Dua Lipa":
        print("Ela está 'Levitating', se voce não quer me ver ganhando, não aparece, não venha! Dua Lipa e seu 'Future Nostalgia' dominaram o pop.")
        
    return diva_campea_podio

def processar_parte2(sistema_parado, musicas_aceitas_parte1, dados_divas, diva_campea_podio):

    musica_campea = ""
    diva_musica_campea = ""
    votos_musicas_parte2 = {}
    total_votos_validos = 0
    
    if sistema_parado == 0:
        continuar_lendo = 1
        while continuar_lendo:
            linha = input()

            if linha == "FIM":
                continuar_lendo = 0
            
            if continuar_lendo:
                partes = separar_e_limpar(linha)
                formato_entrada_valido = (len(partes) == 2)
                valido = formato_entrada_valido
                
                musica = ""
                diva_bruta = ""

                if formato_entrada_valido:
                    musica = partes[0]
                    diva_bruta = partes[1]
                    
                    if musica not in musicas_aceitas_parte1 or musica not in divas_musicas[diva_bruta]:
                        print("Essa musica não pertence ao catálogo, tente outra")
                        valido = 0

                if valido:
                    total_votos_validos = total_votos_validos + 1
                    votos_musicas_parte2[musica] = votos_musicas_parte2.get(musica, 0) + 1

    if sistema_parado == 0:
        if total_votos_validos == 0:
            print('Nenhuma música foi mencionada, acho que no fim elas estão sem hype')
            sistema_parado = 1
        
        if sistema_parado == 0:
            musica_campea, diva_musica_campea = definir_musica_campea(votos_musicas_parte2, musicas_aceitas_parte1, dados_divas)
            sistema_parado = verificar_dominio(diva_musica_campea, diva_campea_podio, sistema_parado)

    return (sistema_parado, musica_campea, diva_musica_campea, votos_musicas_parte2)

def definir_musica_campea(votos_musicas_parte2, musicas_aceitas_parte1, dados_divas):

    musicas_vencedoras_bruto_tupla = () 

    chaves = tuple(votos_musicas_parte2.keys())
    i = 0
    while i < len(chaves):
        musica = chaves[i]
        votos = votos_musicas_parte2[musica]
        
        diva_dona = musicas_aceitas_parte1[musica]
        dados_diva = dados_divas[diva_dona]
        musicas_diva = dados_diva['Musicas_Contadas']
        streams_diva = dados_diva['Streams']
        
        media_diva = 0
        if musicas_diva > 0:
            media_diva = streams_diva // musicas_diva

        novo_item = (votos, media_diva, musicas_diva, diva_dona, musica)

        musicas_vencedoras_bruto_tupla = musicas_vencedoras_bruto_tupla + (novo_item,)
        i = i + 1

    musicas_ordenadas = ordenar_musica(musicas_vencedoras_bruto_tupla)

    musica_campea = musicas_ordenadas[0][4]
    diva_musica_campea = musicas_ordenadas[0][3]

    print(f"E a música campeã foi {musica_campea}!")
    return musica_campea, diva_musica_campea

def verificar_dominio(diva_musica_campea, diva_campea_podio, sistema_parado):

    if diva_musica_campea == diva_campea_podio:
        print(f"Domínio completo! {diva_musica_campea} levou o pódio e a melhor música")
        sistema_parado = 1
    else:
        print(f"Apesar da {diva_campea_podio} ter vencido no Pódio, a melhor música ficou com {diva_musica_campea}")
        print(f"Por isso teremos uma segunda chance para {diva_musica_campea}")
        print("A decisão será feita por votação popular, mas aparentemente faltou verba para o Spotify, pois os nomes vieram bagunçados, Quem será a Campeã?")
        
    return sistema_parado

def processar_parte3(sistema_parado, divas_conjunto, divas, dados_divas, diva_campea_podio, diva_musica_campea):
    
    total_votos_validos = 0
    votos_popular = {}
    votos_por_fa = {}
    
    if sistema_parado == 0:
        continuar_lendo = 1
        while continuar_lendo:
            linha = input()
            
            if not linha:
                continuar_lendo = 0

            if continuar_lendo:
                partes = separar_e_limpar(linha)
                formato_entrada_valido = (len(partes) == 4)
                valido = formato_entrada_valido
                
                fa_cripto = ""
                chave_fa_str = ""
                diva_cripto = ""
                chave_diva_str = ""
                chave_fa = 0
                chave_diva = 0
                
                if formato_entrada_valido:
                    fa_cripto = partes[0]
                    chave_fa_str = partes[1]
                    diva_cripto = partes[2]
                    chave_diva_str = partes[3]
                    
                    chave_numerica = numerico(chave_fa_str)
                    chave_numerica = chave_numerica and numerico(chave_diva_str)

                    if chave_numerica:
                        chave_fa = int(chave_fa_str)
                        chave_diva = int(chave_diva_str)
                    else:
                        valido = 0

                if valido:
                    # descriptograficar
                    fa_descriptografado = descriptografar_cesar(fa_cripto, chave_fa)
                    diva_descriptografada = descriptografar_cesar(diva_cripto, chave_diva)
                    
                    # fim e fim
                    fa_fim = (fa_descriptografado == "fim") 
                    diva_fim = (diva_descriptografada == "fim") 
                    condicao_parada = fa_fim and diva_fim
                    
                    if condicao_parada:
                        continuar_lendo = 0
                        valido = 0 

                    if valido:
                        diva_descriptografada = diva_descriptografada.title()
                        fa_descriptografado = fa_descriptografado.title()
                        if diva_descriptografada not in divas_conjunto:
                            valido = 0

                if valido:
                    total_votos_validos = total_votos_validos + 1

                    # Contagem de votos por diva
                    votos_popular[diva_descriptografada] = votos_popular.get(diva_descriptografada, 0) + 1
                    print(f"Voto de {fa_descriptografado} computado para {diva_descriptografada}")

                    # contagem de votos por fã
                    if diva_descriptografada not in votos_por_fa:
                        votos_por_fa[diva_descriptografada] = {}

                    votos_fa = votos_por_fa[diva_descriptografada]
                    votos_fa[fa_descriptografado] = votos_fa.get(fa_descriptografado, 0) + 1
    
    if sistema_parado == 0:
        determinar_campea_final(total_votos_validos, divas, dados_divas, diva_campea_podio, diva_musica_campea, votos_popular, votos_por_fa)
        
    return sistema_parado


def determinar_campea_final(total_votos_validos, divas, dados_divas, diva_campea_podio, diva_musica_campea, votos_popular, votos_por_fa):

    if total_votos_validos == 0:
    
        diva_wo = ""
        diva_wo_encontrada = 0
        i = 0
        while i < len(divas):
            diva = divas[i]
            excluido = 0
            if diva == diva_campea_podio:
                excluido = 1
            if diva == diva_musica_campea:
                excluido = 1
            
            if excluido == 0:

                if diva_wo_encontrada == 0:
                    diva_wo = diva
                diva_wo_encontrada = diva_wo_encontrada + 1
            i = i + 1
        
        if diva_wo_encontrada == 1:
            print("Aparentemente os Streams das duas foram comprados, a vencedora só pode ser a que não comprou nenhum voto")
            print(f"Parabéns {diva_wo}, a campeã final!")
        
    if total_votos_validos > 0:

        divas_final_bruto_tupla = () 
        i = 0
        while i < len(divas):
            diva = divas[i]
            votos = votos_popular.get(diva, 0)
            
            # dados para desempate
            dados_diva = dados_divas[diva]
            musicas_diva = dados_diva['Musicas_Contadas']
            streams_diva = dados_diva['Streams']
            
            media_diva = 0
            if musicas_diva > 0:
                media_diva = streams_diva // musicas_diva

            novo_item = (votos, media_diva, musicas_diva, diva)

            divas_final_bruto_tupla = divas_final_bruto_tupla + (novo_item,)
            i = i + 1
            
        divas_ordenadas = ordenar_diva_final(divas_final_bruto_tupla)
        campea_final = divas_ordenadas[0][3]

        maior_fa = ""
        max_votos_fa = -1
        votos_fas_campea = votos_por_fa.get(campea_final, {})

        chaves_fas = tuple(votos_fas_campea.keys())
        j = 0
        while j < len(chaves_fas):
            fa = chaves_fas[j]
            votos = votos_fas_campea[fa]
            
            if max_votos_fa == -1:
                 max_votos_fa = votos
                 maior_fa = fa

            elif votos > max_votos_fa:
                max_votos_fa = votos
                maior_fa = fa
            elif votos == max_votos_fa:
                if fa < maior_fa:
                    maior_fa = fa
            j = j + 1


        # imprime os resultados finais
        print(f"A campeã final é {campea_final}")
        print(f"E o(A) maior fã da diva {campea_final} é {maior_fa}")

# inicia o estado para a execução
estado = {
    'total_musicas_validas': 0,
    'sistema_parado': 0,
    'musica_campea': "",
    'diva_campea_podio': "",
    'diva_musica_campea': "",
    'dados_divas': dados_divas,
    'musicas_aceitas_parte1': musicas_aceitas_parte1,
    'votos_musicas_parte2': votos_musicas_parte2,
    'votos_popular': votos_popular,
    'votos_por_fa': votos_por_fa
}

# parte 1
(estado['total_musicas_validas'], estado['sistema_parado'], _, estado['diva_campea_podio'], estado['dados_divas'], estado['musicas_aceitas_parte1']) = processar_parte1(eras, divas_conjunto, estado['dados_divas'], contador_musicas_por_era)

# parte 2
if estado['sistema_parado'] == 0:
    (estado['sistema_parado'], estado['musica_campea'], estado['diva_musica_campea'], estado['votos_musicas_parte2']) = processar_parte2(estado['sistema_parado'], estado['musicas_aceitas_parte1'], estado['dados_divas'], estado['diva_campea_podio'])

# parte 3
if estado['sistema_parado'] == 0:
    processar_parte3(estado['sistema_parado'], divas_conjunto, divas, estado['dados_divas'], estado['diva_campea_podio'], estado['diva_musica_campea'])