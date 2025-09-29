print('Vai começar a brincadeira! Será que a palavra vai ficar igual até o fim?')

numero_participantes = int(input())
palavras_diferentes = 0

for i in range(0,numero_participantes):
    nome_participante = input()
    palavra_falada = input()
    if(i == 0):
        primeira_palavra = palavra_falada
        palavra_atual = palavra_falada
    elif(i == numero_participantes-1):
        ultima_palavra = palavra_falada
    
    if(i > 0) and (palavra_falada != palavra_atual):
        print(f'Parece que {nome_participante} não conseguiu ouvir muito bem e acabou passando pra frente uma palavra diferente da que escutou…')
        palavras_diferentes +=1
        
        if(palavras_diferentes == 1):
            jogador_errou = nome_participante
            palavra_errada = palavra_falada
        if(palavras_diferentes == 2):
            jogador2_errou = nome_participante
        
        palavra_atual = palavra_falada
        if(palavras_diferentes == 5) and (primeira_palavra != palavra_atual):
            print(f'Caramba, que confusão! A palavra {primeira_palavra} já tá toda embaralhada e virou {palavra_falada}!')

if(palavras_diferentes == 0) and (primeira_palavra == ultima_palavra):
    print(f'Impressionante, todos os jogadores ouviram e falaram perfeitamente a palavra {primeira_palavra}! Talvez os telefones modernos comecem a perder espaço pra moda antiga.')
elif(palavras_diferentes > 0) and (primeira_palavra == ultima_palavra):
    print(f'Parece que ocorreram {palavras_diferentes} trocas durante o processo, mas mesmo com essa pequena confusão, a palavra {primeira_palavra} conseguiu chegar no fim do telefone sem fio.')

if(palavras_diferentes == 1) and (primeira_palavra != ultima_palavra):
    print(f'Poxa, foi por pouco, só quem errou foi {jogador_errou} que disse {palavra_errada} ao invés de {primeira_palavra}…')
elif(palavras_diferentes == 2) and (primeira_palavra != ultima_palavra):
    print(f'Se não fosse pelos erros de {jogador_errou} e {jogador2_errou} a palavra {primeira_palavra} poderia ter chegado até o fim, talvez eles devessem tentar de novo.')
elif(palavras_diferentes > 2) and (primeira_palavra != ultima_palavra):
    print(f'É, parece que os alunos se confundiram bastante durante a brincadeira e a palavra {primeira_palavra} acabou virando {ultima_palavra}. No total, ocorreram {palavras_diferentes} trocas.')