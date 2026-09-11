qtd_alunos = int(input("Informe a quantidade de alunos:\n"))
soma_individual = 0
soma_geral = 0
qtd_aprovacao = 0
qtd_recuperacao = 0
qtd_reprovacao = 0
maior_media = 0
menor_mdeia = 0

for i in range(1, qtd_alunos + 1):
  nome = input("Informe o seu nome:\n")
  nota1 = float(input(f"Informe sua primeira nota:\n"))
  nota2 = float(input(f"Informe sua segunda nota:\n"))
  nota3 = float(input(f"Informe sua terceira nota:\n"))
  frequencia = float(input(f"Informe sua frequência:\n"))

  soma_individual = soma_individual + nota1 + nota2 + nota3
  soma_geral = soma_geral + soma_individual
  media_individual = soma_individual / 3
  media_geral_turma = soma_geral / (qtd_alunos * 3)

  if i == 1:
    maior_media = media_individual
    menor_media = media_individual
    melhor_aluno = nome
    pior_aluno = nome
  else:
    if media_individual > maior_media:
      maior_media = media_individual
      melhor_aluno
    if media_individual < menor_media:
      menor_media = media_individual
      pior_aluno = nome

  if media_individual > 7 and frequencia > 75:
    situacao_individual = "Aprovado"
    qtd_aprovacao = qtd_aprovacao + 1
  elif media_individual > 7 and frequencia < 75:
    situacao_individual = "Reprovado"
    qtd_reprovacao = qtd_reprovacao + 1
  elif media_individual < 7 and media_individual >= 6:
    situacao_individual = "Recuperação"
    qtd_recuperacao = qtd_recuperacao + 1
  elif media_individual < 5 or frequencia < 75:
    situacao_individual= "Reprovado"
    qtd_reprovacao = qtd_reprovacao + 1

  percentual_aprovacao = (qtd_aprovacao / qtd_alunos) * 100

  print(f"Nome: {nome}")
  print(f"Média: {media_individual}")
  print(f"Frequência: {frequencia}")
  print(f"Situação: {situacao_individual}")

print(f"Média geral da turma: {media_geral_turma}")
print(f"Maior Média: {maior_media}")
print(f"Menor Média: {menor_media}")
print(f"Melhor aluno: {melhor_aluno}")
print(f"Pior aluno: {pior_aluno}")
print(f"Quantidade de alunos aprovados: {qtd_aprovacao}")
print(f"Quantidade de alunos em recuperação: {qtd_recuperacao}")
print(f"Quantidade de alunos reprovados: {qtd_reprovacao}")
print(f"Percentual de alunos aprovados: {percentual_aprovacao}")