salario_bruto = float(input("Informe o salário bruto:\n"))
quantidade_de_dependentes = int(input("Informe a quantidade de dependentes:\n"))
valor_pago_em_previdência = float(input("Informe o valor pago em previdência:\n"))
valor_pago_em_pensão_alimentícia = float(input("Informe o valor pago em pensão alimentícia:\n"))
dedução_por_dependente = 250 * quantidade_de_dependentes
base_de_calculo = salario_bruto - valor_pago_em_previdência - valor_pago_em_pensão_alimentícia - dedução_por_dependente

if base_de_calculo <= 2500:
    print("Isento")
    aliquota = "Isento"
elif base_de_calculo >= 2500 and base_de_calculo <= 3500:
    print("Alíquota de 7,5%")
    aliquota = 7,5%
elif base_de_calculo >= 3500 and base_de_calculo <= 5000:
    print("Alíquota de 15%")
    aliquota = 15%
elif base_de_calculo >= 5000 and base_de_calculo <= 7500:
    print("Aliquota de 22,5%")
    aliquota = 22,5%
else:
    print("27,5%")
    aliquota = 27,5%

print(f"Salário bruto: {salario_bruto}")
print(f"Total de dedução por dependente: {dedução_por_depedente}")
print(f"Base de cálculo: {base_de_calculo}")
print(f"Alíquota: {aliquota}")
print(f"Imposto:")
print(f"Salário liquido:")