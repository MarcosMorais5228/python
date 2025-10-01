print('Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.')

rodadas = int(input())

for i in range(0, rodadas):
    print(f"Rodada {i+1}/{rodadas}:")
    tentativas = 0
    vidas = 6
    palavra = input().lower()
    fantasma = input().lower()
    comum = ""
        
    for letra in palavra:
        if (letra in fantasma) and (letra not in comum):
            comum = comum + letra
    
    while len(comum) >= 3:
        print(f"A palavra fantasma possui {len(comum)} letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
        comum = ""
        fantasma = input().lower()
        
        for letra in palavra:
            if (letra in fantasma) and (letra not in comum):
                comum = comum + letra
        
    testadas = ""
    letras_chutadas = ""
    x = True
    while (vidas > 0) and (x == True):
        x = False

        if(len(testadas) == 0):
            print("Palavra:", end = " ")
            for i in range(0, len(palavra)):
                
                if(i == len(palavra) - 1):
                    print("_")
                
                else:
                    print("_", end = " ")
        
        else:
            print("=====================")
            print("Palavra:", end=" ")
            
            for i in range(0, len(palavra)):
                l = palavra[i]
                if (l in testadas):
                    if(i == len(palavra) - 1):
                        print(l)
                    else:
                        print(l, end=" ")
                else:
                    if(i == len(palavra) - 1):
                        print("_")
                    else:
                        print("_", end=" ")
            
            print(f"Vidas restantes: {vidas}")
            print(f"Letras chutadas: {testadas}")
            print("=====================")

        letra = input().lower()
        
        if (letra in testadas.lower()):
            while(letra in testadas.lower()):
                print(f"Você já tentou a letra '{letra}'. Tente outra.")
                letra = input().lower() 
        
        letras_chutadas += letra 

        for i in range(0, len(palavra)):
            if(palavra[i] not in letras_chutadas):
                x = True
        
        tentativas += 1   

        if (letra in palavra):
            print(f"Boa! A letra '{letra}' está na palavra.")
                        
        elif(letra not in palavra) and (letra not in fantasma):
            print(f"Naao! A letra '{letra}' não está na palavra. Você perdeu 1 vida.")

            vidas -= 1
                    
        elif(letra not in palavra) and(letra in fantasma):
            print(f"CUIDADO! A letra '{letra}' é uma armadilha! Você perdeu 2 vidas.")

            vidas -= 2
                        
        if(testadas == ""):
            testadas = testadas + letra
                                     
        else:
            testadas = testadas + ", " + letra
                          
    if(vidas <= 0):
        print(f"Fim de jogo! A forca está completa e o Adivinho perdeu. A palavra secreta era: {palavra.capitalize()}.")

    elif(x == False):
        print(f"Parabéns, Adivinho! Você descobriu a palavra secreta: {palavra.capitalize()}.")
        print(f"Total de tentativas: {tentativas}")