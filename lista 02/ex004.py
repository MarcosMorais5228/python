numero_camadas = int(input())

espacos = 2*numero_camadas - 1

numero1 = int((espacos - 1)/2)
numero2 = 1

for i in range(0, numero_camadas):
    for a in range(0, numero1+1):
        print('⠀', end = '')
    
    for b in range(0, numero2):
        if(b != numero2-1):
            print('#', end = '')
        else:
            print('#')
           
    numero1 -= 1
    numero2 += 2