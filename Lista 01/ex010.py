print('Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…')
print('Quantos dos amigos dele conseguirão ajudar dessa vez?')
print('Hora da lista dos amigos da vez!')
quantidade_pessoas = int(input())
if(quantidade_pessoas == 0):
    cerveja = int(input())
    print(f'\nRelatório da situação de Ted:')
    print('Ted foi para o MacLaren’s… Olhe em volta, Ted, você está sozinho.')
    print(f'- Quantidade de cervejas bebidas por Ted: {cerveja} cervejas.')

elif(quantidade_pessoas == 1):
    nome = input()
    lugar = input()
    if(lugar == 'MacLaren’s Pub'):
            cerveja = int(input())
    if('Barney' == nome):
        print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
    elif('Robin' == nome):
        print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
    elif('Marshall' == nome):
        print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
    elif('Lily' == nome):
        print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
    else:
        print(f'{nome} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if('Barney' == nome) and (lugar == 'Arena Laser Tag'):
        print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
    elif('Robin' == nome) and (lugar == 'Carmichael’s'):
        print('Acho que Ted e Robin vão sair em um date… Tomara que Ted não roube aquela trompa azul da parede de novo.')
    elif(lugar == 'MacLaren’s Pub') and (('Barney' == nome) or ('Marshall' == nome) or ('Robin' == nome) or ('Lily' == nome)):
        print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
    elif(lugar != 'MacLaren’s Pub') and ('Barney' != nome) and ('Marshall' != nome) and ('Robin' != nome) and ('Lily' != nome):
        print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')
    print('\nRelatório da situação de Ted:')
    print(f'- Ted foi consolado por: {nome}.')
    print(f'- O local de afogar as mágoas foi: {lugar}.')
    print('- Saideira de um pra um. Nada melhor do que uma pessoa pra ouvir seus problemas.')
    if(lugar == 'MacLaren’s Pub'):
        print(f'- Quantidade de cervejas bebidas pelo grupo: {cerveja} cervejas.')
    print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')
elif(quantidade_pessoas > 1):
    nome = []
    for i in range (0, quantidade_pessoas):
        nome.append(input())
    lugar = input()
    if(lugar == 'MacLaren’s Pub'):
            cerveja = int(input())
    
    for a in range(0, quantidade_pessoas):
        if(nome[a] == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome[a] == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome[a] == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome[a] == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome[a] != 'Barney') and (nome[a] != 'Lily') and (nome[a] != 'Marshall') and (nome[a] != 'Robin'):
            print(f'{nome[a]} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
    if(quantidade_pessoas == 2) and ('Marshall' in nome) and ('Lily' in nome):
        print('Nada melhor que um casal para dar conselhos de relacionamento.')
    elif(quantidade_pessoas == 2) and ('Marshall' in nome) and ('Barney' in nome):
        print('Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.')
    elif(quantidade_pessoas == 4) and ('Marshall' in nome) and ('Barney' in nome) and ('Lily' in nome) and ('Robin' in nome):
        print('O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.')
    if('Barney' in nome) and (lugar == 'Arena de Laser Tag'):
        print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
    elif(lugar == 'MacLaren’s Pub') and (('Marshall' in nome) or ('Barney' in nome) or ('Lily' in nome) or ('Robin' in nome)):
        print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
    elif(lugar == 'MacLaren’s Pub') and ('Marshall' not in nome) and ('Barney' not in nome) and ('Lily' not in nome) and ('Robin' not in nome):
        print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')

    print('\nRelatório da situação de Ted:')
    if(quantidade_pessoas == 2):
        print(f'- Ted foi consolado por: {nome[0]} e {nome[1]}.')
    elif(quantidade_pessoas == 3):
        print(f'- Ted foi consolado por: {nome[0]}, {nome[1]} e {nome[2]}.')
    elif(quantidade_pessoas == 4):
        print(f'- Ted foi consolado por: {nome[0]}, {nome[1]}, {nome[2]} e {nome[3]}.')
    print(f'- O local de afogar as mágoas foi: {lugar}.')
    if(quantidade_pessoas == 2):
        print('- Duas pessoas se compadeceram com a situação do pobre Ted.')
    elif(quantidade_pessoas == 3):
        print('- Três pessoas! Ted conseguiu se divertir bastante.')
    elif(quantidade_pessoas == 4) and ('Marshall' in nome) and ('Barney' in nome) and ('Lily' in nome) and ('Robin' in nome):
        print('- O quinteto junto consegue resolver qualquer problema!')
    elif(quantidade_pessoas == 4) and (('Marshall' not in nome) or ('Barney' not in nome) or ('Lily' not in nome) or ('Robin' not in nome)):
        print('- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.')
    if(lugar == 'MacLaren’s Pub'):
        total_cerveja = cerveja*quantidade_pessoas
        print(f'- Quantidade de cervejas bebidas pelo grupo: {total_cerveja} cervejas.')
    print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')