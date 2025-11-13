def jogo():
    



niveis_dificuldade = input().split()
golden_freddy = False
sequencia = ''
n1789 = [False, False, False, False]
continuar = True

valido = True
for i in range(len(niveis_dificuldade)):
    niveis_dificuldade[i] = int(niveis_dificuldade[i])
    if niveis_dificuldade[i] > 20 or niveis_dificuldade[i] < 0:
        valido = False

if len(niveis_dificuldade) != 4 or not valido:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')
    valido = False

elif sorted(niveis_dificuldade) == [1, 7, 8, 9]:
    golden_freddy = True

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

if not continuar: 
    print('''"IT'S ME"''')

elif valido: 
    if sum(niveis_dificuldade) == 0:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    else:
        