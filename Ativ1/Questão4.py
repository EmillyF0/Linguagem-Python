peso_encomenda = float(input("Informe o peso da entrega:\n"))
distancia_km = float(input("Informe a distância (km):\n"))
tipo_entrega = input("Informe o tipo de entrega (normal, expressa ou urgente):\n")
cliente_assinante = float(input("É assinante? (responda em porcentagem)\n"))
assinante = 100
valor_compra = float(input("Informe o valor da compra:\n"))
taxa_por_peso = peso_encomenda * 2.50
taxa_por_distância = distancia_km * 0.30
adicional = 0

if cliente_assinante == assinante and valor_compra == 2000 and tipo_entrega == "normal" and peso_encomenda <= 10:
    print("Frete gratuito!")
elif:
else:

print(f"Taxa por peso: {taxa_por_peso} \n")
print(f"Taxa por distância: {taxa_por_distancia}")