tentativas = int(input())
ana = 0
adrieli = 0
joab = 0
duda = 0
vencedores = 0

#Amarelinha de Ana
for a in range(0, tentativas):
    casa_ana = int(input())
    
    if(casa_ana > ana):
        ana = casa_ana
    
print(f'Ana tentou {tentativas} vezes e completou a última casa {ana}')

if(ana == 5):
    print('Ana completou a amarelinha!')
    vencedores += 1
    vencedor = 'Ana'

else:
    print('Ana não conseguiu completar a amarelinha!')

#Amarelinha de Adrieli
for a in range(0, tentativas):
    casa_adrieli = int(input())
    
    if(casa_adrieli > adrieli):
        adrieli = casa_adrieli
    
print(f'Adrieli tentou {tentativas} vezes e completou a última casa {adrieli}')

if(adrieli == 5):
    print('Adrieli completou a amarelinha!')
    vencedores += 1
    vencedor = 'Adrieli'

else:
    print('Adrieli não conseguiu completar a amarelinha!')

#Amarelinha de joab
for a in range(0, tentativas):
    casa_joab = int(input())
    
    if(casa_joab > joab):
        joab = casa_joab
    
print(f'Joab tentou {tentativas} vezes e completou a última casa {joab}')

if(joab == 5):
    print('Joab completou a amarelinha!')
    vencedores += 1
    vencedor = 'Joab'

else:
    print('Joab não conseguiu completar a amarelinha!')

#Amarelinha de Duda
for a in range(0, tentativas):
    casa_duda = int(input())
    
    if(casa_duda > duda):
        duda = casa_duda
    
print(f'Duda tentou {tentativas} vezes e completou a última casa {duda}')

if(duda == 5):
    print('Duda completou a amarelinha!')
    vencedores += 1
    vencedor = 'Duda'

else:
    print('Duda não conseguiu completar a amarelinha!')

#Resultado
if(vencedores == 1):
    print(f'O vencedor é {vencedor}!')

elif(vencedores == 2):
    if(ana == 5) and (adrieli == 5):
        print('Houve empate entre: Ana, Adrieli')
    
    elif(ana == 5) and (joab == 5):
        print('Houve empate entre: Ana, Joab')
    
    elif(ana == 5) and (duda == 5):
        print('Houve empate entre: Ana, Duda')

    elif(adrieli == 5) and (joab == 5):
        print('Houve empate entre: Adrieli, Joab')
    
    elif(adrieli == 5) and (duda == 5):
        print('Houve empate entre: Adrieli, Duda')

    elif(joab == 5) and (duda == 5):
        print('Houve empate entre: Joab, Duda')

elif(vencedores == 3):
    if(ana == 5) and (adrieli == 5) and (joab == 5):
        print('Houve empate entre: Ana, Adrieli, Joab')
    
    elif(ana == 5) and (adrieli == 5) and (duda == 5):
        print('Houve empate entre: Ana, Adrieli, Duda')
    
    elif(ana == 5) and (joab == 5) and (duda == 5):
        print('Houve empate entre: Ana, Joab, Duda')

    elif(adrieli == 5) and (joab == 5) and (duda == 5):
        print('Houve empate entre: Adrieli, Joab, Duda')

elif(vencedores == 4):
    print('Houve empate entre: Ana, Adrieli, Joab, Duda')