#Análise de vendas de vendedores

qtd_vendedores = int(input("Qual será a quantidade de vendedores?\n"))
total_vendido_equipe = 0
soma_comissoes = 0
comissao = 0
maior_numero = 0
menor_numero = 0
remuneracao_final = 0
qtd_vendas_final = 0

for i in range(1, qtd_vendedores + 1):
  nome = input(f"Qual é o {i}° vendedor?\n")
  salario_base = float(input("Qual é seu salário?\n"))
  valor_total_vendido = float(input("Qual é o valor total vendido por esse vendedor?\n"))
  qtd_vendas = int(input("Qual foi a quantidade de vendas desse vendedor?\n"))

  if i == 1:
    maior_numero = valor_total_vendido
    menor_numero = valor_total_vendido
    maior_vendedor = nome
    menor_vendedor = nome
  else:
    if valor_total_vendido > maior_numero:
      maior_numero = valor_total_vendido
      maior_vendedor = nome
    if valor_total_vendido < menor_numero:
      menor_numero = valor_total_vendido
      menor_vendedor = nome
  
  if valor_total_vendido == 10000:
    comissao = 0.03 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 3%!")
  elif valor_total_vendido >= 10001 and valor_total_vendido <= 30000:
    comissao = 0.05 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 5%")
  elif valor_total_vendido > 30000:
    comissao = 0.08 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 8%")
  else:
    print("Inválido!\n")

  if qtd_vendas > 20:
    bonus = 500
    print("Bônus de R$500!")
  else:
    bonus = 0
    
  total_vendido_equipe = total_vendido_equipe + valor_total_vendido
  qtd_vendas_final = qtd_vendas + qtd_vendas_final
  remuneracao_final = salario_base + comissao + bonus
  print(f"Sua remuneração final: {remuneracao_final:.2f}\n")
  media = total_vendido_equipe / qtd_vendas_final

print(f"Total vendido pela equipe: {total_vendido_equipe:.2f}")
print(f"Total pago em comissões: {soma_comissoes:.2f}")
print(f"Maior vendedor: {maior_vendedor}")
print(f"Menor vendedor: {menor_vendedor}")
print(f"Média de vendas da equipe: {media:.2f}")