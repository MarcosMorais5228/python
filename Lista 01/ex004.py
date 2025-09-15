artigos_sheldon = int(input())
artigos_leonard = int(input())
artigos_raj = int(input())
artigos_howard = int(input())
experimentos_sheldon = int(input())
experimentos_leonard = int(input())
experimentos_raj = int(input())
experimentos_howard = int(input())

pontuacao_sheldon = (artigos_sheldon*2) + (experimentos_sheldon*3)
pontuacao_leonard = (artigos_leonard*2) + (experimentos_leonard*3)
pontuacao_raj = (artigos_raj*2) + (experimentos_raj*3)
pontuacao_howard = (artigos_howard*2) + (experimentos_howard*3)

print('Pontuação final:')
print(f'Sheldon: {pontuacao_sheldon}')
print(f'Leonard: {pontuacao_leonard}')
print(f'Raj: {pontuacao_raj}')
print(f'Howard: {pontuacao_howard}\n')

vencedor = max(pontuacao_sheldon, pontuacao_leonard, pontuacao_raj, pontuacao_howard)

if(vencedor == pontuacao_sheldon):
    print('O cientista da semana é: Sheldon')
    print('Não é atoa que ele ganhou o prêmio Nobel')
elif(vencedor == pontuacao_leonard):
    print('O cientista da semana é: Leonard')
    print('A vitória dele prova que aguentar o Sheldon já é um experimento científico por si só.')
elif(vencedor == pontuacao_raj):
    print('O cientista da semana é: Raj')
    print('Ele comemora... mas ainda precisa da ajuda do cachorro para falar com mulheres.')
elif(vencedor == pontuacao_howard):
    print('O cientista da semana é: Howard')
    print('Um pequeno passo para a ciência, um grande salto para alguém com mestrado.')