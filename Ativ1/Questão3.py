nota1 = float(input("Informe a 1° nota:\n"))
nota2 = float(input("Informe a 2° nota:\n"))
nota3 = float(input("Informe a 3° nota:\n"))
frequencia = float(input("Informe seu percentual de frequência:\n"))
ativ_entregues = int(input("Informe a quantidade de atividade entregues:\n"))
total_de_ativ = int(input("Informe quantidade total de atividades:\n"))
soma_notas = nota1 + nota2 + nota3 
media = soma_notas / 3

if media >= 9 and frequencia >= 90 and ativ_entregues == total_de_ativ:
    print("Aprovado com excelência!")
elif media >= 7 and frequencia >= 75 and ativ_entregues >= ((70 / 100) * total_de_ativ):
    print("Aprovado!")
    print("Requisito para aumentar classificação, elevar a: média, frequência e atividades entregues.")
elif media >= 5 and media <= 6.99 and frequencia >= 75:
    print("Recuperação!")
    print("Aumentar a: média e frequência.")
elif frequencia < 75:
    print("Reprovado por frequência!")
else:
    print("Reprovado por nota!")