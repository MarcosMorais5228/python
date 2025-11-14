# receber tudin
niveis_dificuldade = input().split()
golden_freddy = False
sequencia = ''
n1789 = [False, False, False, False]
continuar = True

# vê se tá válido
valido = True
for i in range(len(niveis_dificuldade)):
    niveis_dificuldade[i] = int(niveis_dificuldade[i])
    if niveis_dificuldade[i] > 20 or niveis_dificuldade[i] < 0:
        valido = False

# vê se tem 4 números
if len(niveis_dificuldade) != 4 or not valido:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')
    valido = False

# vê se tem o Golden Francisco
elif sorted(niveis_dificuldade) == [1, 7, 8, 9]:
    golden_freddy = True

# se tiver 0 tlvz seja It´s me
elif 0 in niveis_dificuldade:
    continuar = False
    for i in range(len(niveis_dificuldade)):
        sequencia = sequencia + str(niveis_dificuldade[i])
    
    for caractere in sequencia:
        if caractere == '1':
            n1789[0] = True
        elif caractere == '7':
            n1789[1] = True
        elif caractere == '8':
            n1789[2] = True
        elif caractere == '9':
            n1789[3] = True
    
    for i in range(4):
        if n1789[i] == False:
            continuar = True

# perdemo
if not continuar: 
    print('''"IT'S ME"''')

# ainda não perdemo
elif valido: 
    # vagabundos e preguiçosos
    if sum(niveis_dificuldade) == 0:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    
    # vieram
    else:
        def jogo(niveis_dificuldade, golden_freddy):
            Bonnie = niveis_dificuldade[0]
            Chica  = niveis_dificuldade[1]
            Freddy = niveis_dificuldade[2]
            Foxy   = niveis_dificuldade[3]

            sequencia = []
            
            def jogar(hora, energia):
                if energia <= 0:
                    return None, 0

                # acabô
                if hora == 6:
                    return sequencia, energia

                # decisões iniciais da hora
                pe = 0
                pd = 0
                lz = 0
                cam = 0

                # energia mínima por hora
                gasto = 1  # decremento base

                # ataques por hora
                ataques = []

                if hora == 0:
                    if Bonnie > 0:
                        ataques.append('Bonnie')
                if hora == 1:
                    if Chica > 0:
                        ataques.append('Chica')
                if hora == 2:
                    pass
                if hora == 3:
                    if Bonnie > 0:
                        ataques.append('Bonnie')
                if hora == 4:
                    if Chica > 0:
                        ataques.append('Chica')
                    if Foxy > 0 and energia > 50:
                        ataques.append('Foxy')
                if hora == 5:
                    if Freddy > 0:
                        ataques.append('Freddy')
                    if golden_freddy:
                        ataques.append('Golden')

                # Tomando decisões para frustrar ataques com menor gasto (dessa vez sem backtracking, só análise por hora)
                i = 0
                while i < len(ataques):
                    atk = ataques[i]
                    # Bonnie cueio
                    if atk == 'Bonnie':
                        gasto_pe = 7
                        gasto_lz = 5
                        if gasto_lz <= gasto_pe:
                            lz = 1
                            cam = 0
                        else:
                            pe = 1
                    # Chica galinha
                    if atk == "Chica":
                        gasto_pd = 7
                        gasto_cam = 9
                        if gasto_cam <= gasto_pd:
                            cam = 1
                        else:
                            pd = 1
                    # Foxy pirata
                    if atk == "Foxy":
                        pe = 1
                    # Freddy ursão amigo
                    if atk == "Freddy":
                        gasto_pepd = 14
                        gasto_cam = 9
                        if gasto_cam <= gasto_pepd:
                            cam = 1
                        else:
                            pe = 1
                            pd = 1
                    # Golden Frantchesco (se tiver ativo)
                    if atk == 'Golden':
                        cam = 1
                    i = i + 1


                # calcula o gasto da energia por hora
                if pe == 1:
                    gasto = gasto + 7
                if pd == 1:
                    gasto = gasto + 7
                if lz == 1:
                    gasto = gasto + 5
                if cam == 1:
                    gasto = gasto + 9

                energia2 = energia - gasto
                # calcula energia dos ataques frustrados
                i = 0
                while i < len(ataques):
                    atk = ataques[i]
                    if atk == 'Bonnie':
                        energia2 = energia2 - (3 + Bonnie * 0.25)
                    if atk == 'Chica':
                        energia2 = energia2 - (2 + Chica * 0.35)
                    if atk == 'Foxy':
                        energia2 = energia2 - (5 + Foxy * 0.15)
                    if atk == 'Freddy':
                        energia2 = energia2 - (3 + Freddy * 0.35)
                    if atk == 'Golden':
                        energia2 = energia2 - (10 + Freddy * 1.95)
                    i = i + 1

                # salva a decisão da hora pra dar aquela printada no fim
                sequencia.append([pe, pd, lz, cam])

                return jogar(hora + 1, energia2)

            # inicia o jogo
            seq_final, energia_final = jogar(0, 100)

            # perdemo msm
            if seq_final is None or energia_final <= 0:
                print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')
                return

            # não perdemo
            print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_final:.2f}% de energia. Eu sabia que você conseguiria."')

            for h in range(6):
                pe = seq_final[h][0]
                pd = seq_final[h][1]
                lz = seq_final[h][2]
                cam = seq_final[h][3]

                if pe == 1: txt_pe  = 'SIM' 
                else: txt_pe = 'NÃO'
                if pd == 1: txt_pd  = 'SIM' 
                else: txt_pd = 'NÃO'
                if lz == 1: txt_lz  = 'SIM' 
                else: txt_lz = 'NÃO'
                if cam == 1: txt_cam  = 'SIM' 
                else: txt_cam = 'NÃO'

                print(f'0{h}:00 AM -> PE: {txt_pe} | PD: {txt_pd} | LZ: {txt_lz} | CAM: {txt_cam}')

        # chama a função jogo
        jogo(niveis_dificuldade, golden_freddy)
