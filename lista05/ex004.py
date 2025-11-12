# função que monta a lista e posições (excluindo a primeira para não ser 0-based) e chamada função para resolver
def cemiterio(n, tumulo):
    tabuleiro = [0] * (n + 1)
    return resolver(tabuleiro, 1, n, tumulo)

# essa aqui tenta resolver
def resolver(tabuleiro, linha, n, tumulo):
    if linha > n:
        return 1  

    total = 0
    for coluna in range(1, n + 1):
        if (tumulo != (linha, coluna)) and bota(tabuleiro, linha, coluna):
            tabuleiro[linha] = coluna
            total += resolver(tabuleiro, linha + 1, n, tumulo)
            tabuleiro[linha] = 0
    return total

# essa aqui vê se pode botar
def bota(tabuleiro, linha, coluna):
    for i in range(1, linha):
        if tabuleiro[i] == coluna:
            return False

        if abs(tabuleiro[i] - coluna) == abs(i - linha):
            return False
    return True

# receber entradas
n = int(input())
tum1 = int(input())
tum2 = int(input())

# guardar a posição do túmulo
tum = (tum1, tum2)

# iniciar o jogo (é um N-queens com restrição rsrsrs)
posicoes = cemiterio(n, tum)

# aqui só acaba msm
print(f'Rogério e Chaguinha conseguiram encontrar o túmulo ocupado em {tum}!\n')
print(f'Rogério e Chaguinha conseguiram encontrar {posicoes} possíveis posições para as almas se posicionarem sem conflitos!')

if posicoes == 0:
    print('Não existe nenhuma configuração segura para as almas... Rogério e Chaguinha estão presos no meio da guerra das almas!')

elif posicoes >= 1 and posicoes <= 10:
    print('Os amigos vão precisar tomar muito cuidado para não pegar um caminho errado!')

elif posicoes > 10 and posicoes <= 50:
    print('Uau! São tantas opções que eles até se perderam contando!')

else:
    print('Em pleno Halloween e as almas descansando em paz! Rogério e Chaguinha vão conseguir sair logo do cemitério.')