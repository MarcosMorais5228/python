niveis_dificuldade = input().split()

valido = True
for i in range(len(niveis_dificuldade)):
    niveis_dificuldade[i] = int(niveis_dificuldade[i])
    if niveis_dificuldade[i] > 20 or niveis_dificuldade[i] < 0:
        valido = False

if len(niveis_dificuldade) != 4 or not valido:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')

