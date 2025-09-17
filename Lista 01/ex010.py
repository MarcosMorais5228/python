print('Ted se iludiu de novo. Esse é o momento que ele mais precisa dos amigos dele…')
print('Quantos dos amigos dele conseguirão ajudar dessa vez?')

quantidade_pessoas = int(input())
if(quantidade_pessoas > 0):
    print('Hora da lista dos amigos da vez!')
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
    if('Barney' == nome) and (lugar == 'Arena de Laser Tag'):
            print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
    if('Robin' == nome) and (lugar == 'Carmichael’s'):
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
        print(f'- Quantidade de cervejas bebidas pelo grupo: {cerveja*2} cervejas.')
    print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')
elif(quantidade_pessoas > 1):
    if(quantidade_pessoas == 2):
        nome1 = input()
        nome2 = input()
    elif(quantidade_pessoas == 3):
        nome1 = input()
        nome2 = input()
        nome3 = input()
    elif(quantidade_pessoas == 4):
        nome1 = input()
        nome2 = input()
        nome3 = input()
        nome4 = input()

    lugar = input()
    if(lugar == 'MacLaren’s Pub'):
            cerveja = int(input())
    
    if(quantidade_pessoas == 2):
        if(nome1 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome1 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome1 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome1 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome1 != 'Barney') and (nome1 != 'Lily') and (nome1 != 'Marshall') and (nome1 != 'Robin'):
            print(f'{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

        if(nome2 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome2 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome2 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome2 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome2 != 'Barney') and (nome2 != 'Lily') and (nome2 != 'Marshall') and (nome2 != 'Robin'):
            print(f'{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
        
        if((('Marshall' == nome1) and ('Lily' == nome2)) or (('Marshall' == nome2) and ('Lily' == nome1))):
            print('Nada melhor que um casal para dar conselhos de relacionamento.')
        elif((('Marshall' == nome1) and ('Barney' == nome2)) or (('Marshall' == nome2) and ('Barney' == nome1))):
            print('Sem dúvida os melhores amigos de Ted. Mas tomara que Barney não queira implicar com Marshall sobre quem realmente é o melhor amigo dele.')
        if(('Barney' == nome1) or ('Barney' == nome2)) and (lugar == 'Arena de Laser Tag'):
            print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
        if(lugar == 'MacLaren’s Pub') and ((('Marshall' == nome1) or ('Marshall' == nome2)) or (('Barney' == nome1) or ('Barney' == nome2)) or (('Lily' == nome1) or ('Lily' == nome2)) or (('Robin' == nome1) or ('Robin' == nome2))):
            print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
        if(lugar == 'MacLaren’s Pub') and (('Marshall' != nome1) and ('Marshall' != nome2)) and (('Barney' != nome1) and ('Barney' != nome2)) and (('Lily' != nome1) and ('Lily' != nome2)) and (('Robin' != nome1) and ('Robin' != nome2)):
            print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')
        print('\nRelatório da situação de Ted:')
        print(f'- Ted foi consolado por: {nome1} e {nome2}.')
        print(f'- O local de afogar as mágoas foi: {lugar}.')
        print('- Duas pessoas se compadeceram com a situação do pobre Ted.')
        if(lugar == 'MacLaren’s Pub'):
            total_cerveja = cerveja*(quantidade_pessoas+1)
            print(f'- Quantidade de cervejas bebidas pelo grupo: {total_cerveja} cervejas.')
        print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')

    if(quantidade_pessoas == 3):
        if(nome1 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome1 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome1 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome1 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome1 != 'Barney') and (nome1 != 'Lily') and (nome1 != 'Marshall') and (nome1 != 'Robin'):
            print(f'{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

        if(nome2 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome2 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome2 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome2 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome2 != 'Barney') and (nome2 != 'Lily') and (nome2 != 'Marshall') and (nome2 != 'Robin'):
            print(f'{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

        if(nome3 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome3 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome3 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome3 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome3 != 'Barney') and (nome3 != 'Lily') and (nome3 != 'Marshall') and (nome3 != 'Robin'):
            print(f'{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
        if(('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3)) and (lugar == 'Arena de Laser Tag'):
            print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
        if(lugar == 'MacLaren’s Pub') and ((('Marshall' == nome1) or ('Marshall' == nome2) or ('Marshall' == nome3)) or (('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3)) or (('Lily' == nome1) or ('Lily' == nome2) or ('Lily' == nome3)) or (('Robin' == nome1) or ('Robin' == nome2) or ('Robin' == nome3))):
            print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
        if(lugar == 'MacLaren’s Pub') and (('Marshall' != nome1) and ('Marshall' != nome2) and ('Marshall' != nome3)) and (('Barney' != nome1) and ('Barney' != nome2) and ('Barney' != nome3)) and (('Lily' != nome1) and ('Lily' != nome2) and ('Lily' != nome3)) and (('Robin' != nome1) and ('Robin' != nome2) and ('Robin' != nome3)):
            print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')
        print('\nRelatório da situação de Ted:')
        print(f'- Ted foi consolado por: {nome1}, {nome2} e {nome3}.')
        print(f'- O local de afogar as mágoas foi: {lugar}.')
        print('- Três pessoas! Ted conseguiu se divertir bastante.')
        if(lugar == 'MacLaren’s Pub'):
            total_cerveja = cerveja*(quantidade_pessoas+1)
            print(f'- Quantidade de cervejas bebidas pelo grupo: {total_cerveja} cervejas.')
        print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')

        
    if(quantidade_pessoas == 4):
        if(nome1 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome1 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome1 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome1 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome1 != 'Barney') and (nome1 != 'Lily') and (nome1 != 'Marshall') and (nome1 != 'Robin'):
            print(f'{nome1} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

        if(nome2 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome2 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome2 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome2 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome2 != 'Barney') and (nome2 != 'Lily') and (nome2 != 'Marshall') and (nome2 != 'Robin'):
            print(f'{nome2} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')

        if(nome3 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome3 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome3 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome3 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome3 != 'Barney') and (nome3 != 'Lily') and (nome3 != 'Marshall') and (nome3 != 'Robin'):
            print(f'{nome3} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
        
        
        if(nome4 == 'Barney'):
            print('Barney foi voluntário dessa vez. Tenho certeza que ele vai conseguir transformar toda essa tristeza de Ted em um rolê Legen… espera por isso… DÁRIO.')
        elif(nome4 == 'Robin'):
            print('Trompa azul na área! A repórter mais amada do Metro News 1 vai tentar ajudar. Tomara que ele não fique mais iludido ainda.')
        elif(nome4 == 'Marshall'):
            print('O melhor amigo de Ted com certeza estaria com ele em um momento tão difícil. Marshall realmente sabe o valor da irmandade.')
        elif(nome4 == 'Lily'):
            print('Lily adora fazer o papel da irmã mais velha. Com certeza ela irá consolar ele, mas só depois de dizer “Eu avisei”.')
        elif(nome4 != 'Barney') and (nome4 != 'Lily') and (nome4 != 'Marshall') and (nome4 != 'Robin'):
            print(f'{nome4} vai encarar essa com Ted. Às vezes a gente encontra apoio de quem menos espera.')
        if(quantidade_pessoas == 4) and (('Marshall' == nome1) or ('Marshall' == nome2) or ('Marshall' == nome3) or ('Marshall' == nome4)) and (('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3) or ('Barney' == nome4)) and (('Lily' == nome1) or ('Lily' == nome2) or ('Lily' == nome3) or ('Lily' == nome4)) and (('Robin' == nome1) or ('Robin' == nome2) or ('Robin' == nome3) or ('Robin' == nome4)):
            print('O quinteto estará reunido nessa jornada! É o momento perfeito pra brincar de “Você conhece o Ted?”.')
        if(('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3) or ('Barney' == nome4)) and (lugar == 'Arena de Laser Tag'):
            print('Com certeza a Arena de Laser Tag foi escolhida por influência de Barney. Se arrume Ted, é hora de botar um terno, tomar um whisky e partir pra diversão.')
        if(lugar == 'MacLaren’s Pub') and ((('Marshall' == nome1) or ('Marshall' == nome2) or ('Marshall' == nome3) or ('Marshall' == nome4)) or (('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3) or ('Barney' == nome4)) or (('Lily' == nome1) or ('Lily' == nome2) or ('Lily' == nome3) or ('Lily' == nome4)) or (('Robin' == nome1) or ('Robin' == nome2) or ('Robin' == nome3) or ('Robin' == nome4))):
            print('Não tem erro, né? Estar no MacLaren’s é como estar em casa.')
        if(lugar == 'MacLaren’s Pub') and (('Marshall' != nome1) and ('Marshall' != nome2) and ('Marshall' != nome3) and ('Marshall' != nome4)) and (('Barney' != nome1) and ('Barney' != nome2) and ('Barney' != nome3) and ('Barney' != nome4)) and (('Lily' != nome1) and ('Lily' != nome2) and ('Lily' != nome3) and ('Lily' != nome4)) and (('Robin' != nome1) and ('Robin' != nome2) and ('Robin' != nome3) and ('Robin' != nome4)):
            print('Um lugar habitual, mas com uma galera diferente. Será estranho, mas Ted vai.')
        print('\nRelatório da situação de Ted:')
        print(f'- Ted foi consolado por: {nome1}, {nome2}, {nome3} e {nome4}.')
        print(f'- O local de afogar as mágoas foi: {lugar}.')
        if(('Marshall' == nome1) or ('Marshall' == nome2) or ('Marshall' == nome3) or ('Marshall' == nome4)) and (('Barney' == nome1) or ('Barney' == nome2) or ('Barney' == nome3) or ('Barney' == nome4)) and (('Lily' == nome1) or ('Lily' == nome2) or ('Lily' == nome3) or ('Lily' == nome4)) and (('Robin' == nome1) or ('Robin' == nome2) or ('Robin' == nome3) or ('Robin' == nome4)):
            print('- O quinteto junto consegue resolver qualquer problema!')
        else:
            print('- Saiu um quinteto um pouco diferente do que a gente tá acostumado, mas no fim conseguiram deixar Ted alegre.')
        if(lugar == 'MacLaren’s Pub'):
            total_cerveja = cerveja*(quantidade_pessoas+1)
            print(f'- Quantidade de cervejas bebidas pelo grupo: {total_cerveja} cervejas.')
        print('Pelo visto todo mundo já sabe como funciona a cabeça dele, né? Depois do rolê Ted conseguiu esfriar a cabeça e já tá pronto pra quebrar mais a cara. Quem será que serão os próximos a consolar o querido Ted Mosby?')
