qtd_numeros = int(input("Qual será a quantidade de numeros que serão inseridos?\n"))
qtd_positivos = 0
qtd_negativos = 0
zero = 0
qtd_pares = 0
qtd_impares = 0
soma = 0
maior_numero = 0
menor_numero = 0

for i in range(1, qtd_numeros + 1):
  numeros = int(input(f"Informe o {i} número:\n"))

  if i == 0:
    maior_numero = numeros
    menor_numero = numeros
  else:
      if numeros > maior_numero:
        maior_numero = numeros
      if numeros < menor_numero:
        menor_numero = numeros
  
  if numeros > 0:
    qtd_positivos = qtd_positivos + 1
  elif numeros < 0:
    qtd_negativos = qtd_negativos + 1
  else:
    zero = zero + 1

  if numeros % 2 == 0:
    qtd_pares = qtd_pares + 1
  else:
    qtd_impares = qtd_impares + 1
    
  soma = soma + numeros
  media = soma / qtd_numeros
  percentual_positivos = (qtd_positivos / qtd_numeros) * 100
  percentual_pares = (qtd_pares / qtd_numeros) * 100

print(f"Maior valor: {maior_numero}")
print(f"Menor valor: {menor_numero}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Quantidade de positivos: {qtd_positivos}")
print(f"Quantidade de negativos: {qtd_negativos}")
print(f"Quantidade de zeros: {zero}")
print(f"Quantidade de pares: {qtd_pares}")
print(f"Quantidade de ímpares: {qtd_impares}")
print(f"Percentual de números positivos: {percentual_positivos:.2f}%")
print(f"Percentual de números pares: {percentual_pares:.2f}%")