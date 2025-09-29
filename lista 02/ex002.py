nome1 = input()
nome2 = input()
nome3 = input()
pontuacao1 = 0
pontuacao2 = 0
pontuacao3 = 0

print('Vai começar o esconde-esconde UFPE 2025!')

for i in range(0,3):
    if(i == 0):
        print(f'\nProntos ou não, lá vai {nome1}.')
        for a in range(0,3):
            if(a == 0):
                print(f'Agora {nome1} procurará no CFCH.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome1} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
            elif(a == 1):
                print(f'Agora {nome1} procurará no CTG.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome1} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
            elif(a == 2):
                print(f'Agora {nome1} procurará no CIN.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome1} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
        
    elif(i == 1):
        print(f'\nProntos ou não, lá vai {nome2}.')
        for a in range(0,3):
            if(a == 0):
                print(f'Agora {nome2} procurará no CFCH.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome2} achou uma pessoa!')
                    pontuacao2 +=1
                    resp = input()
            elif(a == 1):
                print(f'Agora {nome2} procurará no CTG.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome2} achou uma pessoa!')
                    pontuacao2 +=1
                    resp = input()
            elif(a == 2):
                print(f'Agora {nome2} procurará no CIN.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome2} achou uma pessoa!')
                    pontuacao2 +=1
                    resp = input()
        
    elif(i == 2):
        print(f'\nProntos ou não, lá vai {nome3}.')
        for a in range(0,3):
            if(a == 0):
                print(f'Agora {nome3} procurará no CFCH.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao3 +=1
                    resp = input()
            elif(a == 1):
                print(f'Agora {nome3} procurará no CTG.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao3 +=1
                    resp = input()
            elif(a == 2):
                print(f'Agora {nome3} procurará no CIN.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao3 +=1
                    resp = input()

if (pontuacao1 > pontuacao2) and (pontuacao1 > pontuacao3):
    print(f'\n{nome1} é o(a) melhor no esconde-esconde da UFPE!')
elif(pontuacao2 > pontuacao1) and (pontuacao2 > pontuacao3):
    print(f'\n{nome2} é o(a) melhor no esconde-esconde da UFPE!')
elif(pontuacao3 > pontuacao2) and (pontuacao3 > pontuacao1):
    print(f'\n{nome3} é o(a) melhor no esconde-esconde da UFPE!')
elif(pontuacao1 == 0) and (pontuacao2 == 0) and (pontuacao3 == 0):
    print('\nNinguém foi encontrado, nenhum dos buscadores ganhou a disputa.')