renda_mensal = float(input("Informe a renda mensal:\n"))
gastos_moradia = float(input("Informe o gasto de moradia:\n"))
gasto_alimentação = float(input("Informe o gasto de alimentação:\n"))
gasto_transporte = float(input("Informe o gasto do transporte:\n"))
gasto_saude = float(input("Informe o gasto da saúde:\n"))
gasto_educaçao = float(input("Informe o gasto de educação:\n"))
gasto_lazer = float(input("Informe gasto para fins próprios:\n"))
valor_dividas = float(input("Informe o valor das dívidas:\n"))
renda_com_gasto_dividas = renda_mensal - valor_dividas
total_despesas = gastos_moradia + gastos_transpote + gastos_saude + gastos_educaçao + gastos_lazer + valor_dividas
saldo_mensal = renda_mensal - total_despesas
percentual_renda_comprometida = (saldo_mensal / (renda_mensal/100))
Percentual_gasto_dividas = (renda_com_gasto_dividas / (renda_mensal/100))

