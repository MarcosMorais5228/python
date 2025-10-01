print('Que comece o jogo! Adivinhe a palavra, mas cuidado para não cair na armadilha.')

rodadas = int(input())

for i in range(0, rodadas):
    print(f"Rodada {i+1}/{rodadas}:")
    vidas = 6
    palavra = input()
    fantasma = input()
    comum = ""
        
    for letra in palavra.lower():
        if (letra in fantasma.lower()) and (letra not in comum):
            comum = comum + letra
    
    while len(comum) >= 3:
        print("A palavra fantasma possui 3 letras presentes na palavra secreta. Tente uma com menos de 3 letras iguais.")
        comum = ""
        fantasma = input()
        
        for letra in palavra.lower():
            if (letra in fantasma.lower()) and (letra not in comum):
                comum = comum + letra

    while (vidas == 6):
        letra = input()
        testadas = ""
        
        if (letra.lower() in testadas.lower()):
            print(f"A letra '{letra}' já foi testada antes!")
            
        else:
                
            if letra.lower() in palavra.lower():
                print(f"A letra '{letra}' está no texto.")
                
            else:
                print(f"A letra '{letra}' NÃO está no texto.")
                
            if(testadas == ""):
                testadas = testadas + letra
                
            else:
                testadas = testadas + ", " + letra

        print("Letras já testadas:", testadas)
        continuar = input("Quer testar outra letra? (s/n): ")