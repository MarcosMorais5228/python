# função que verifica as horas
def verificar(a, b):
    if a > b:
        return True
    else:  
        return False

# função que verifica Elisson nas digitais
def digitalE(a):
    if 'Elisson' in a:
        return True
    else:
        return False

def digitalJ(a):
    if 'João Guilherme' in a:
        return True
    else:
        return False

conf = False

# abertura
print('TRIBUNAL EM SESSÃO')
print('Juiz: Que comece o julgamento do caso em pauta.\n')

# diálogo inicial
print('Promotor Edgeworth: A promotoria está pronta, Meritíssimo.')
print('Phoenix Wright: (Lá vamos nós... A reputação do escritório está em jogo.) A defesa está pronta.\n')

# sala devisitas
print('''--- SALA DE VISITAS DO TRIBUNAL ---
João Guilherme: Sr. Wright, eu juro, eu não o matei! Eu estive lá, mas... é só isso!
Phoenix Wright: (Eu sinto que ele está escondendo algo... Devo pressioná-lo por mais detalhes ou confiar no que ele me disse?)\n''')

escolha_inicial = input()

# tribunal
print('''--- DE VOLTA AO TRIBUNAL ---
Juiz: Promotoria, apresente as evidências.
Promotor Edgeworth: A promotoria acusa este homem pelo crime de assassinato...
Promotor Edgeworth: ...João Guilherme!
Promotor Edgeworth: Comecemos com a evidência virtual chave, o registro da última modificação no computador da vítima.''')

hora_modificacao =int(input())

# hora da morte
print('Promotor Edgeworth: E, de acordo com o legista, a hora exata da morte.')

hora_morte = int(input())
verificacao = verificar(hora_modificacao, hora_morte)

# número digitais
print('Promotor Edgeworth: Finalmente, a prova irrefutável. O relatório de digitais da arma do crime, o troféu.')

numero_digitais = int(input())

# leitura
print('Promotor Edgeworth: Que o escrivão leia os nomes encontrados na arma...\n')

# nomes digitais
nomes_digitais = []
for i in range(numero_digitais):
    nome = input()
    nomes_digitais.append(nome)

digitais1 = digitalE(nomes_digitais)
digitais2 = digitalJ(nomes_digitais)

# final
print('ARGUMENTOS FINAIS\n')

if escolha_inicial == 'pressionar':
    print('''--- FLASHBACK: SALA DE VISITAS ---
Phoenix Wright: HOLD IT! João, não é só isso! Eu não posso te defender se você não me contar tudo. O que realmente aconteceu naquela noite?
João Guilherme: (soluço)... Certo... Eu vou contar. Não era sobre a rixa... era sobre o 'Ticket Fantasma'.
João Guilherme: Um bug impossível no sistema da faculdade. Eu criei um código que o resolvia. Era a minha chance de conseguir o estágio dos sonhos.
João Guilherme: Eu... eu confiei em Arthur. Mostrei o código a ele para uma revisão. E ele... ele o roubou. Apresentou como se fosse dele, levou todo o crédito.
João Guilherme: E o pior, Sr. Wright... eu cometi o erro de comentar sobre meu progresso com o Elisson, o 'monitor do povo'. Ele era o único, além de mim e de Arthur, que sabia da história toda. Ele observava nossa agilidade com os tickets com um sentimento sombrio! Se houver dedo dele nisso, ele certamente tentará depôr para contar do roubo do meu código por Arthur para me incriminar!
--- FIM DO FLASHBACK ---\n''')
    print('''Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, suas digitais estão na arma, e a perícia mostra que o arquivo do 'Ticket Fantasma' foi modificado após a morte, provando que ele permaneceu na cena do crime!
Phoenix Wright: OBJEÇÃO!\n''')
    
    # se houver contradição
    if verificacao:
        print('''Phoenix Wright: A sua lógica tem uma falha fatal, promotor! É impossível que meu cliente tenha modificado aquele arquivo!
Phoenix Wright: Pois a defesa pode provar que, no exato momento da modificação, João Guilherme estava a quilômetros de distância, comprando um café na 'Cafeteria Byte'! Temos o registro da transação e uma testemunha ocular!
Phoenix Wright: A contradição temporal, combinada com este álibi, prova apenas uma coisa: a existência de uma terceira pessoa na cena do crime!''')
        veredito = 'INOCENTE'
    
        # Elisson está nas digitais?
        if digitais1:
            print('''Phoenix Wright: Se meu cliente tem um álibi, quem poderia ser? Quem alteraria o arquivo do 'Ticket Fantasma' para incriminar João Guilherme?
Phoenix Wright: Só poderia ser alguém que conhecia a história... alguém que meu cliente confessou ter contado!
Phoenix Wright: A defesa descobriu que apenas UMA outra pessoa sabia da história do código... uma pessoa cujas digitais, convenientemente, também estão na arma do crime!
Phoenix Wright: A pessoa que matou Arthur Sean para eliminar um rival e incriminar o outro foi você...
Phoenix Wright: ELISSON!!!

Elisson: N-NÃÃÃÃÃOOOOO! COMO... ELE TE CONTOU?! MEU PLANO ERA PERFEITO!''')
            conf = True
            veredito = 'INOCENTE'
    else:
        if not digitais2:
            print('''Phoenix Wright: A promotoria não pode sequer provar que meu cliente tocou na arma do crime! Não há digitais dele!''')
            veredito = 'INOCENTE'
        
        elif digitais2:
            print('''Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Não tenho objeções...)''')
            veredito = 'CULPADO'

elif escolha_inicial == 'confiar':
    print('''(Voz da Consciência de Phoenix: Eu confiei em João... mas agora, essa 'hora da modificação' não faz sentido para mim. Não tenho como usar essa evidência!)\n''')
    print('''Promotor Edgeworth: A lógica é simples. O acusado tinha o motivo, e suas digitais estão na arma. O caso está encerrado.
Phoenix Wright: OBJEÇÃO!\n''')
    
    # digitais Jõao
    if not digitais2:
        print('''Phoenix Wright: A promotoria não pode provar que meu cliente tocou na arma do crime! Não há digitais dele!''')
        veredito = 'INOCENTE'
    elif digitais2:
        print('''Phoenix Wright: (Droga... As digitais estão na arma e a linha do tempo da promotoria é sólida... Estou sem argumentos!)''')
        veredito = 'CULPADO'
    
# Anúncio e veredito
print()
print(f'''Juiz: ...Compreendo. Após analisar todas as evidências e os argumentos...
Juiz: O veredito para o caso de João Guilherme é: {veredito}!\n''')

if veredito == 'INOCENTE':
    if conf:
        print('''Juiz: Que esta corte jamais esqueça o dia em que a verdade foi revelada contra todas as probabilidades.''')
    print('''A reputação do escritório Fey & Co. continua impecável.''')

else: 
    print('''Edgeworth... Você ainda não venceu o debate final.''')
