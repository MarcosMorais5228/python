print("Don't sleep, don't eat, just do it on repeat! Keep bumpin' that!!!\n")

# definit variáveis iniciais
atos = {1 : ('Hyperpop','Pop', 600), 2 : ('Sentimental','Ballad', 480), 3 : ('Hyperpop','Banger', 720)}
tempo = [0, 0, 0]
setlist1 = {}
setlist2 = {}
setlist3 = {}
a = 0
b = 0
c = 0
descartadas = 0

# começar atos
for i in range(1, 4):
    print(f'Iniciando montagem do Ato {i} ({atos[i][0]} e {atos[i][1]}):\n')

    entrada = ''
    # pegar músicas
    while entrada != 'FIM_ATO_1' and entrada != 'FIM_ATO_2' and entrada != 'FIM_SHOW':
        entrada = input()
        if entrada != 'FIM_ATO_1' and entrada != 'FIM_ATO_2' and entrada != 'FIM_SHOW':
            musica, genero, duracao = entrada.split(', ')
            print(f'Música em análise: {musica}')

            # músicas especiais
            if musica == 'Talk Talk featuring troye sivan':
                print('A MAIOR AMIZADE DO POP NO PALCO? Talk to them in your own made-up language!')
            
            elif musica == 'Von dutch a. g. cook remix featuring addison rae':
                print("‘CAUSE THEY’RE JUST LIVING THAT LIFE! Addison Rae, a maior revelação do pop desde Britney Spears, no palco ao lado da sua amiga Charli XCX!")
            
            elif musica == 'Guess featuring billie eilish':
                print('Hey, Billie, you there?')

            # testar música proibida
            if musica != "Actually Romantic":
                if genero == atos[i][0] or genero == atos[i][1]:
                    duracao = duracao.split(':')
                    duracao = int(duracao[0])*60 + int(duracao[1])

                    if int(tempo[i-1]) + duracao <= atos[i][2]:
                        tempo[i-1] = int(tempo[i-1]) + duracao
                        print(f'{musica} adicionada ao Ato {i} ;).')
                        if i == 1:
                            setlist1.update({a : (musica, genero)})
                            a += 1
                        elif i == 2:
                            setlist2.update({b : (musica, genero)})
                            b += 1
                        elif i == 3:
                            setlist3.update({c : (musica, genero)})
                            c += 1

                    else: 
                        print(f'Muito longa! O Ato {i} já está com {tempo[i-1]} segundos e essa música tem {duracao} segundos.')
                        descartadas += 1
                
                else: 
                    print('Gênero errado para esse ato! Cuidado, uma música deslocada mata a vibe de um show…')
                    descartadas += 1
        
            else:
                print('Já não basta ter exposto a Charli nessa música, agora a Taylor quer que a própria cante? GOLPE BAIXÍSSIMO!!!')
                descartadas += 1

    print()

# testar se não teve menor que 70%
if int(tempo[0])/int(atos[1][2]) < 0.7 or int(tempo[1])/int(atos[2][2]) < 0.7 or int(tempo[2])/int(atos[3][2]) < 0.7: 
    print('Tem certeza que isso é um show? Rápido desse jeito, a Charli XCX deve estar pensando nos doces do backstage…\n')

# print relatório de atos
print(f'--- Ato 1 (Abertura) ---')
if int(tempo[0]) > 0:
    for i in range(a):
        print(f'{setlist1[i][0]} ({setlist1[i][1]})')
else:
    print('Nenhuma música adicionada a este Ato.')
print(f'Duração total do ato: {tempo[0]} segundos.')
print()

print(f'--- Ato 2 (Sentimental) ---')
if int(tempo[1]) > 0:
    for i in range(b):
        print(f'{setlist2[i][0]} ({setlist2[i][1]})')
else: 
    print('Nenhuma música adicionada a este Ato.')
print(f'Duração total do ato: {tempo[1]} segundos.')
print()

print(f'--- Ato 3 (Encerramento) ---')
if int(tempo[2]) > 0:
    for i in range(c):
        print(f'{setlist3[i][0]} ({setlist3[i][1]})')
else: 
    print('Nenhuma música adicionada a este Ato.')
print(f'Duração total do ato: {tempo[2]} segundos.')
print()

# relatório final
print('=== RESUMO DO SHOW (BRAT APPROVED) ===')
print(f'Total de músicas na setlist: {a+b+c}')
print(f'Total de músicas barradas: {descartadas}')