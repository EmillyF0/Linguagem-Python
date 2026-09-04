tentativas_senhas = 0
saldo = 2500
qtd_operacoes = 0
deposito = 0
saque = 0
senha = input("Informe a senha:\n")

while True:
    if senha != "5678" and tentativas_senhas == 3:
        print("Bloqueado! Tente novamente mais tarde.")
        break
    elif senha != "5678":
        input("Digite a senha novamente:\n")
        tentativas_senhas = 1 + tentativas_senhas
    else:
        if senha == "5678":
            print("1- Consultar saldo")
            print("2- Depositar")
            print("3- Sacar")
            print("4- Exibir quantidade de operações")
            print("1- Encerrar")
            resposta = int(input("Informe a opção desejada:\n"))

            if resposta == 1:
                print(f"Saldo atual: {saldo}\n")
                qtd_operacoes = qtd_operacoes + 1
                continue
            elif resposta == 2:
                deposito = float(input("Quanto deseja depositar?\n"))
                if deposito <= 0:
                    print("Inválido\n")
                    continue
                else:
                    saldo = saldo + deposito
                    print("Deposito realizado com sucesso!\n")
                    qtd_operacoes = qtd_operacoes + 1
                    continue
            elif resposta == 3:
                saque = float(input("Quanto deseja sacar?\n"))
                if saque > saldo:
                    print("Saque maior que o saldo! não é possível realizar esta ação!\n")
                else:
                    saldo = saldo - saque
                    print("Saque realizado com sucesso!\n")
                    qtd_operacoes = qtd_operacoes + 1
                    continue
            elif resposta == 4:
                print(f"Quantidade de operações realizadas: {qtd_operacoes}\n")
                qtd_operacoes = qtd_operacoes + 1
                continue
            elif resposta == 5:
                print(f"Total depositado: {deposito}\n")
                print(f"Total sacado: {saque}\n")
                print(f"Saldo atual: {saldo}\n")
                print(f"Operações realizadas: {qtd_operacoes}\n")
                break
            else:
                print("Inválido\n")
                continue
    