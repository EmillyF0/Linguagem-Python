
idade = int(input("Digite sua idade:\n"))
salario_mensal = float(input("Informe seu salário mensal:\n"))
valor_da_divida_atual = float(input("Informe a dívida atual:\n"))
tempo_de_emprego_em_meses = int(input("Qual o tempo de emprego:\n"))
valor_solicitado = float(input("Informe o valor a ser solicitado:\n"))
numero_de_parcelas = int(input("Informe o número de parcelas:\n"))
comprometimento = valor_da_divida_atual / salario_mensal
valor_da_parcela = valor_solicitado / numero_de_parcelas
soma_comprometimento_parcela = comprometimento + valor_da_parcela

if idade >= 21 and  idade <= 65 and salario_mensal >= 2500 and tempo_de_emprego_em_meses >= 12 and comprometimento <= ((30 / 100) * comprometimento) and valor_da_parcela <= ((25 / 100) * salario_mensal):
    print("Aprovado")
elif idade >= 21 and idade <= 65 and salario_mensal >= 2500 and tempo_de_emprego_em_meses >= 6 and soma_comprometimento_parcela < ((50 / 100) * salario_mensal):
    print("Aprovado com restrições")
else:
    print("Reprovado")