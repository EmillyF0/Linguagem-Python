qtd_vendedores = int(input("Qual será a quantidade de vendedores?\n"))
total_vendido_equipe = 0
total_pago_comissao = 0
soma_comissoes = 0

for i in range(1, qtd_vendedores + 1):
  nome = input(f"Qual é o {i}° vendedor?\n")
  salario_base = float(input("Qual é seu salário?\n"))
  valor_total_vendido = float(input("Qual é o valor total vendido por esse vendedor?\n"))
  qtd_vendas = int(input("Qual foi a quantidade de vendas desse vendedor?\n"))
  
  total_vendido_equipe = total_vendido_equipe + valor_total_vendido
  maior_vendedor = 0
  menor_vendedor = 0
  
  if valor_total_vendido == 10000:
    comissao = 0.03 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 3%!\n")
  elif valor_total_vendido >= 10001 and valor_total_vendido <= 30000:
    comissao = 0.05 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 5%\n")
  elif valor_total_vendido >= 30000:
    comissao = 0.08 * valor_total_vendido
    soma_comissoes = soma_comissoes + comissao
    print("Comissão de 8%\n")
  else:
    print("Inválido!\n")

  if qtd_vendas > 20:
    bonus = 500
  else:
    bonus = 0

    media = total_vendido_equipe / qtd_vendas
    remuneracao_final = salario_base + comissão + bonus

print(f"Total vendido pela equipe: {total_vendido_equipe}")
print(f"Total pago em comissões: {soma_comissoes}")
print(f"Maior vendedor: {maior_vendedor}")
print(f"Menor vendedor: {menor_vendedor}")
print(f"Média de vendas da equipe: {media}")
  
    