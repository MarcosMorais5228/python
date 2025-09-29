nome1 = input()
nome2 = input()
mome3 = input()
pontuacao1 = 0
pontuacao2 = 0
pontuacao3 = 0

print('Vai começar o esconde-esconde UFPE 2025!')

for i in range(0,3):
    if(i == 0):
        print(f'\n Prontos ou não, lá vai {nome1}.')
        for a in range(0,3):
            if(a == 0):
                print(f'Agora {nome1} procurará no CFCH.')
            elif(a == 1):
                print(f'Agora {nome1} procurará no CTG.')
            elif(a == 2):
                print(f'Agora {nome1} procurará no CIN.')
        
        resp = input()
        while resp == 'Achou uma pessoa!':
            print(f'{nome1} achou uma pessoa!')
            pontuacao1 +=1

    elif(i == 1):


    elif(i == 2):