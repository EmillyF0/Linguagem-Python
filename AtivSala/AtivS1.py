vendas = [ 1200.0, 850.0, 230.0, 450.0, 1800, 3200.0, 950.0]
total_itens = len(vendas)
total_vendas = sum(vendas)
media_vendas = total_vendas / total_itens
maior = max(vendas)
menor = min(vendas)
acima_media = []

for venda in vendas:
    if venda > media_vendas:
        acima_media.append(venda)

print(f"Quantidade: {total_itens}")
print(f"Total: {total_vendas:.2f}")
print(f"Média: {media_vendas:.2f}")
print(f"Maior venda: {maior}")
print(f"Menor venda: {menor}")
print(f"Vendas acima da média: {len(acima_media)}")
print(acima_media)