diamantes_necessarios = int(input())

if(diamantes_necessarios <= 10):
    print('Arthur')
else:
    if(diamantes_necessarios <= 30):
        print('Luiz')
    else:
        if(diamantes_necessarios <= 100):
            print('Pedro')
        else:
            print('Nenhum')