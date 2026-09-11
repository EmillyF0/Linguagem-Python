#Controle de estoque por menu

estoque_inicial = 100
estoque_final = 100
entradas_realizadas = 0
saidas_realizadas = 0
qtd_operações = 0
estoque_minimo = 0

while True:
  print("1- Entrada de mercadoria")
  print("2- Saída de mercadoria")
  print("3- Consultar estoque")
  print("4- Definir estoque mínimo")
  print("5- Encerrar")
  resposta = int(input("Informe a opção escolhida:\n"))
  if resposta == 1:
    entrada = int(input("Informe a quantidade da entrada:\n"))
    if entrada <= 0:
      print("Entrada menor que o estoque ou igual a zero! Não será aceito!")
      continue
    else:
      print("Entrada realizada com sucesso!\n")
      estoque_final = estoque_final + entrada
      entradas_realizadas = entradas_realizadas + 1
      qtd_operações = qtd_operações + 1
      continue
  elif resposta == 2:
    saida_estoque = int(input("Informe a quantidade da saída:\n"))
    if saida_estoque > estoque_inicial:
      print("Saída ultrapassou o estoque! Não será aceito!\n")
      continue
    else:
      print("Saída realizada com sucesso!\n")
      estoque_final = estoque_final - saida_estoque
      saidas_realizadas = saidas_realizadas + 1
      qtd_operações = qtd_operações + 1
      continue
  elif resposta == 3:
    if estoque_final < estoque_minimo:
      status = "Abaixo do mínimo!"
      print("Estoque está abaixo do minimo!")
      print(f"Estoque: {estoque_final}\n")
      qtd_operações = qtd_operações + 1
      continue
    else:
      status = "Ok"
      print("Estoque está Ok!")
      print(f"Estoque: {estoque_final}")
      qtd_operações = qtd_operações + 1
      continue               
  elif resposta == 4:
    estoque_minimo = int(input("Qual será o estoque mínimo?\n"))
    qtd_operações = qtd_operações + 1
    continue
  elif resposta == 5:
    print(f"Estoque inicial: {estoque_inicial}\n")
    print(f"Total de entradas: {entradas_realizadas}\n")
    print(f"Total de saídas: {saidas_realizadas}\n")
    print(f"Estoque final: {estoque_final}\n")
    print(f"Quantidade de operações: {qtd_operações}\n")
    print(f"Status do estoque: {status}\n")
    break
  else:
    print("Inválido!")
    continue
  