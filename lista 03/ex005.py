nome_projeto = input()
matriz = []
componente = ''

# itens possiveis 
redstone = 0
repetidores = 0
tochas_redstone = 0
lampadas_redstone = 0
blocos_notas = 0
observadores = 0
comparadores = 0
pistoes = 0
pistoes_aderentes = 0


# checa itens necessarios
if nome_projeto == 'Memória ROM Simples':
    redstone_n = 256
    repetidores_n = 64
    tochas_redstone_n = 128

elif nome_projeto == 'Calculadora de 4 bits':
    redstone_n = 512
    repetidores_n = 128
    tochas_redstone_n = 64
    lampadas_redstone_n = 256

elif nome_projeto == 'Sequenciador Musical':
    redstone_n = 1024
    repetidores_n = 256
    blocos_notas_n = 64
    observadores_n = 128

elif nome_projeto == 'Processador de 8 Bits':
    redstone_n = 4096
    repetidores_n = 1024
    lampadas_redstone_n = 2048
    pistoes_aderentes_n = 512

elif nome_projeto == 'Display de Vídeo 8x8':
    redstone_n = 2048
    repetidores_n = 512
    comparadores_n = 256
    pistoes_n = 128

elif nome_projeto == 'Supercomputador V13':
    redstone_n = 8192
    repetidores_n = 2048
    comparadores_n = 1024
    pistoes_aderentes_n = 1024


# inicia a entrada e componentes
while componente != 'Construir!':
    componente = input()

    # testa comando 
    if componente != 'Construir!':
        matriz.append(componente.rsplit(' ', 1))
        
    

    

    
