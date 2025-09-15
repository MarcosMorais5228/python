print('Ativando a máquina...')

nome = input()
ano = int(input())

capitalized_nome = nome.capitalize()
letras_nome = int(len(nome))

if(capitalized_nome == 'Frink'):
    if(ano % letras_nome == 0):
        print('Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!')
    elif(ano % letras_nome != 0):
        print('Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!')
elif(ano % letras_nome == 0):
    print(f'Previsão confiável! O rebigulador será real em {ano}!')
elif(ano % letras_nome != 0):
    print(f'Previsão instável! {capitalized_nome} também deve achar que o rebigulador é ridículo...')
