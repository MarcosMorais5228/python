print('Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!')

time_atacante = input()
back = 6
front = 6
morto_back = 0
morto_front = 0

while (time_atacante != 'Front-End') and (time_atacante != 'Back-End'):
    print('Entrada inválida!')
    time_atacante = input()

while (back > 0) and (front > 0):

    ataque = input()
    while (ataque != 'acertou') and (ataque != 'errou'):
        print('Entrada inválida!')
        ataque = input()

    if ataque == 'acertou':
        if time_atacante == 'Back-End':
            front -= 1
            morto_front += 1
            print('Back-End acertou um jogador!')
        elif time_atacante == 'Front-End':
            back -= 1
            morto_back += 1
            print('Front-End acertou um jogador!')
        elif time_atacante == 'Morto-Back':
            front -= 1
            morto_front += 1
            morto_back -= 1
            back += 1
            print('O morto do Back-End acertou um jogador!')
        elif time_atacante == 'Morto-Front':
            back -= 1
            morto_back += 1
            morto_front -= 1
            front += 1
            print('O morto do Front-End acertou um jogador!')

        print(f'Back-End: {back} dev(s) em campo. | Front-End: {front} dev(s) em campo.')

        if back == 0:
            print(f'Vitória do Front-End! Restaram {front} devs ainda segurando o layout!')
        elif front == 0:
            print(f'Vitória do Back-End! Restaram {back} devs ainda mantendo o servidor de pé!')

        if time_atacante == 'Back-End':
            time_atacante = 'Morto-Front'
        elif time_atacante == 'Front-End':
            time_atacante = 'Morto-Back'
        elif time_atacante == 'Morto-Back':
            time_atacante = 'Morto-Front'
        elif time_atacante == 'Morto-Front':
            time_atacante = 'Morto-Back'

    elif ataque == 'errou':
        if time_atacante == 'Back-End':
            if morto_back == 0:
                time_atacante = 'Front-End'
            else:
                resultado_defesa = input()
                while (resultado_defesa != 'pegou') and (resultado_defesa != 'deixou'):
                    print('Entrada inválida!')
                    resultado_defesa = input()

                if resultado_defesa == 'pegou':
                    time_atacante = 'Front-End'
                else:
                    time_atacante = 'Morto-Back'

        elif time_atacante == 'Front-End':
            if morto_front == 0:
                time_atacante = 'Back-End'
            else:
                resultado_defesa = input()
                while (resultado_defesa != 'pegou') and (resultado_defesa != 'deixou'):
                    print('Entrada inválida!')
                    resultado_defesa = input()

                if resultado_defesa == 'pegou':
                    time_atacante = 'Back-End'
                else:
                    time_atacante = 'Morto-Front'

        elif time_atacante == 'Morto-Back':
            resultado_defesa = input()
            while (resultado_defesa != 'pegou') and (resultado_defesa != 'deixou'):
                print('Entrada inválida!')
                resultado_defesa = input()

            if resultado_defesa == 'pegou':
                time_atacante = 'Front-End'
            else:
                time_atacante = 'Back-End'

        elif time_atacante == 'Morto-Front':
            resultado_defesa = input()
            while (resultado_defesa != 'pegou') and (resultado_defesa != 'deixou'):
                print('Entrada inválida!')
                resultado_defesa = input()

            if resultado_defesa == 'pegou':
                time_atacante = 'Back-End'
            else:
                time_atacante = 'Front-End'
