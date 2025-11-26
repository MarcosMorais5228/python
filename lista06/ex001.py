print('Phil, querido... Você tem certeza que essa música é literalmente sobre... casas?')
print('A própria Sabrina disse que nada na música é uma metáfora! Além disso, o sobrenome dela é carpinteira, acho que ela tem lugar de fala…\n')

N = int(input())
catalogo_phill = {}
vendas = 0

for i in range(N):
    bairro, endereco, quartos, preco = input().split('-')


    catalogo_phill.update({
        endereco.strip() : {
            'bairro' : bairro.strip(),
            'quartos' : quartos.strip(),
            'preco' : preco.strip(),
        }
    })


print('Catálogo concluído! Quem será que irá comprar uma casa de Phil?\n')

nome_cliente = 0
while nome_cliente != 'FIM':
    score_atual = 0
    endereco_final = 0
    nome_cliente = input()
    
    if nome_cliente != 'FIM':
        requisitos = (input().split('-'))
        for i in catalogo_phill:
            if int(catalogo_phill[i]['quartos']) >= int(requisitos[0]) and int(catalogo_phill[i]['preco']) <= int(requisitos[1]):
                score_total = int(catalogo_phill[i]['quartos'])*10
                
                if score_total > score_atual:
                    score_atual = score_total
                    endereco_final = i
        
        if score_atual > 0:
            print(f'🎤 Bem-vindo ao House Tour de {catalogo_phill[endereco_final]["bairro"]}, {nome_cliente}!')
            print(f'➡ Casa: {endereco_final}')
            print(f'💖 Score: {score_atual} pontos\n')
        
        elif score_atual == 0:
            print(f'Puxa, {nome_cliente}, vou te avisar se algo aparecer. Não tenho nada com esses requisitos.\n')
        
        if score_atual >= 40:
            if nome_cliente == 'Sabrina Carpenter':
                print('"Uau, Phil! Acho que finalmente encontrei o cenário perfeito para o clipe de House Tour!"\n')
            elif nome_cliente == 'Taylor Swift':
                print('"Essa casa é perfeita para passar as férias na praia!"\n')
            else:
                print(f'"{nome_cliente} ficou encantado(a)! Phil comemora mais uma venda de sucesso!"\n')
            
            print('Venda concluída! Phil dança triunfante ao som de "House Tour"!\n')
            vendas += 1

        elif score_atual < 40 and score_atual > 0:
            if nome_cliente == 'Sabrina Carpenter':
                print('"Hmm... Sabe Phil, a letra não era tão literal assim…"\n')
            elif nome_cliente == 'Taylor Swift':
                print('"Nós nunca vamos comprar essa casa juntos, Phil!"\n')
            else: 
                print('"Parece que a música não ajudou nas vendas dessa vez…"\n')
            
            print('Talvez a Sabrina realmente não estivesse falando de imóveis…\n')

print('===== RELATÓRIO DE VENDAS =====')
print(f'Total de casas vendidas: {vendas}')
print('===============================')