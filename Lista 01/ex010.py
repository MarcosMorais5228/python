print('Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…')
print('Quantos dos amigos dele conseguirão ajudar dessa vez?')
print('Hora da lista dos amigos da vez!')
quantidade_pessoas = int(input())
if(quantidade_pessoas == 0):
    cerveja = int(input())
    print(f'\nRelatório da situação de Ted:')
    print('Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.')
    print(f'- Quantidade de cervejas bebidas por Ted: {cerveja} cervejas.')
else:
    if(quantidade_pessoas == 1):
        nome = input()
        lugar = input()
        if(lugar == 'MacLaren’s Pub'):
            cerveja = int(input())
    elif(quantidade_pessoas > 1):
        nome = []
        for i in range (0, quantidade_pessoas):
            nome.append(input())
        lugar = input()
        if(lugar == 'MacLaren’s Pub'):
            cerveja = int(input())
    elif(quantidade_pessoas == 0):
        cerveja = int(input())

    if('Barney' in nome):
        print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
    if('Robin' in nome):
        print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
    if('Marshall' in nome):
        print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
    if('Lily' in nome):
        print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
    if('Barney' not in nome) and ('Robin' not in nome) and ('Marshall' not in nome) and ('Lily' not in nome):
        print(f'{nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if(quantidade_pessoas == 2) and ('Marshall' in nome) and ('Lily' in nome):
        print('Nada melhor que um casal para dar conselhos de relacionamento.')
    elif(quantidade_pessoas == 2) and ('Marshall' in nome) and ('Barney' in nome):
        print('Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.')
    elif(quantidade_pessoas == 4) and ('Marshall' in nome) and ('Barney' in nome) and ('Lily' in nome) and ('Robin' in nome):
        print('O quinteto junto consegue resolver qualquer problema!')
    elif(quantidade_pessoas == 4) and (('Marshall' not in nome) or ('Barney' not in nome) or ('Lily' not in nome) or ('Robin' not in nome)):
        print('Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.')
    
    print('\nRelatório da situação de Ted:')
    if(quantidade_pessoas == 1):
        print(f'- Ted foi consolado por: {nome}.')
    elif(quantidade_pessoas == 2):
        print(f'- Ted foi consolado por: {nome[0]} e {nome[1]}.')
    elif(quantidade_pessoas == 3):
        print(f'- Ted foi consolado por: {nome[0]}, {nome[1]} e {nome[2]}.')
    elif(quantidade_pessoas == 4):
        print(f'- Ted foi consolado por: {nome[0]}, {nome[1]}, {nome[2]} e {nome[3]}.')
    print(f'- O local de afogar as mágoas foi: {lugar}.')
    print(f'- {quantidade_pessoas} pessoas se compadeceram com a situação do pobre Ted.')
    if(lugar == 'MacLaren’s Pub'):
        total_cerveja = cerveja*quantidade_pessoas
        print(f'- Quantidade de cervejas bebidas pelo grupo: {total_cerveja} cervejas.')
    print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')
    

