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
                    pontuacao1 +=1
                    resp = input()
            elif(a == 1):
                print(f'Agora {nome2} procurará no CTG.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome2} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
            elif(a == 2):
                print(f'Agora {nome2} procurará no CIN.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome2} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
        
    elif(i == 2):
        print(f'\nProntos ou não, lá vai {nome3}.')
        for a in range(0,3):
            if(a == 0):
                print(f'Agora {nome3} procurará no CFCH.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
            elif(a == 1):
                print(f'Agora {nome3} procurará no CTG.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()
            elif(a == 2):
                print(f'Agora {nome3} procurará no CIN.')
                resp = input()
                while resp == 'Achou uma pessoa!':
                    print(f'{nome3} achou uma pessoa!')
                    pontuacao1 +=1
                    resp = input()