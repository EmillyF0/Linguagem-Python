# Talvez haja problema de espaçamento por causa do "programa" que testo os códigos (houve atualização)
candidato_a = 0
candidato_b = 0
candidato_c = 0
voto_branco = 0
voto_nulo = 0
total_votos = 0

while True:
  print("1- Candidato A")
  print("2- Candidato B")
  print("3- Candidato C")
  print("4- Voto Branco")
  print("5- Voto Nulo")
  print("0- Encerrar votação")
  resposta = int(input("Qual opção vai escolher?\n"))
  
  if resposta == 1:
    candidato_a = candidato_a + 1
    total_votos = total_votos + 1
    continue
  elif resposta == 2:
    candidato_b = candidato_b + 1
    total_votos = total_votos + 1
    continue
  elif resposta == 3:
    candidato_c = candidato_c + 1
    total_votos = total_votos + 1
    continue
  elif resposta == 4:
    voto_branco = voto_branco + 1
    total_votos = total_votos + 1
    continue
  elif resposta == 5:
    voto_nulo = voto_nulo + 1
    total_votos = total_votos + 1
    continue
  elif resposta == 0:
    percentual_a = (candidato_a / total_votos) * 100
    percentual_b = (candidato_b / total_votos) * 100
    percentual_c = (candidato_c / total_votos) * 100
    percentual_válidos = ((candidato_a + candidato_b + candidato_c) * 100) / total_votos
    percentual_inválidos = ((voto_branco + voto_nulo) * 100) / total_votos
    if percentual_a > percentual_b and percentual_a > percentual_c:
      vencedor = "Candidato A"
    elif percentual_b > percentual_a and percentual_b > percentual_c:
      vencedor = "Candidato B"
    else:
      vencedor = "Candidato C"

    if percentual_a == percentual_b == percentual_c:
      empate = "Possível empate"
    else:
      empate = "Não há"
    print(f"Candidato A: {candidato_a}")
    print(f"Candidato B: {candidato_b}")
    print(f"Candidato C: {candidato_c}")
    print(f"Votos em branco: {voto_branco}")
    print(f"Votos nulos: {voto_nulo}")
    print(f"Total de votos: {total_votos}")
    print(f"Percentual candidato A: {percentual_a:.1f}%")
    print(f"Percentual candidato B: {percentual_b:.1f}%")
    print(f"Percentual candidato C: {percentual_c:.1f}%")
    print(f"Percentual voto válidos: {percentual_válidos:.1f}%")
    print(f"Percentual voto inválidos: {percentual_inválidos:.1f}%")
    print(f"Vencendor: {vencedor}")
    print(f"Empate: {empate}")
    break
  else:
    print("Inválido!")
    continue