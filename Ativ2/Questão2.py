tentativas_utilizadas = 0
tentativas_restantes_lv1 = 10
tentativas_restantes_lv2 = 7
tentativas_restantes_lv3 = 5
numero_secreto = 1234

print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!\n")
print("1- Nível fácil (10 tentativas)")
print("2- Nível médio (7 tentativas)")
print("3- Nível difícil (5 tentativas)")
nivel = int(input("Informe o nível do jogo que deseja:\n"))
    
while True:
    if nivel == 1:
        print(f"Possui apenas {tentativas_restantes_lv1} tentativas!")
        numero_usuario = int(input("Informe o número que vc acredita ser o secreto:\n"))
        
        if numero_usuario != 1234 and tentativas_restantes_lv1 == 1:
            print("Você perdeu! :(")
            break
        elif numero_usuario == numero_secreto:
            pontuação_lv1 = tentativas_restantes_lv1 * 100
            print("Você venceu. Vítória! :)")
            print(f"Sua pontuação foi: {pontuação_lv1}")
            print(f"Tentativas utilizadas: {tentativas_utilizadas}")
            break
        elif numero_usuario != numero_secreto:
            if numero_usuario >= 1 and numero_usuario <= 100:
                print("Inválido! Apenas números de 4 dígitos são aceitos!\n")
                continue
            elif numero_usuario > numero_secreto:
                print("Número maior que o número secreto!\n")
                tentativas_restantes_lv1 = tentativas_restantes_lv1 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
            else:
                print("Número menor que o número secreto!\n") 
                tentativas_restantes_lv1 = tentativas_restantes_lv1 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
        else:
            print("Inválido!\n")
            continue 

    elif nivel == 2:
        print(f"Possui apenas {tentativas_restantes_lv2} tentativas!")
        numero_usuario = int(input("Informe o número que vc acredita ser o secreto:\n"))
        
        if numero_usuario != 1234 and tentativas_restantes_lv2 == 1:
            print("Você perdeu! :(")
            break
        elif numero_usuario == numero_secreto:
            pontuação_lv2 = tentativas_restantes_lv2 * 100
            print("Você venceu. Vítória! :)")
            print(f"Sua pontuação foi: {pontuação_lv2}")
            print(f"Tentativas utilizadas: {tentativas_utilizadas}")
            break
        elif numero_usuario != numero_secreto:
            if numero_usuario >= 1 and numero_usuario <= 100:
                print("Inválido! Apenas números de 4 dígitos são aceitos!\n")
                continue
            elif numero_usuario > numero_secreto:
                print("Número maior que o número secreto!\n")
                tentativas_restantes_lv2 = tentativas_restantes_lv2 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
            else:
                print("Número menor que o número secreto!\n") 
                tentativas_restantes_lv2 = tentativas_restantes_lv2 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
        else:
            print("Inválido!\n")
            continue 

    elif nivel == 3:
        print(f"Possui apenas {tentativas_restantes_lv3} tentativas!")
        numero_usuario = int(input("Informe o número que vc acredita ser o secreto:\n"))
        
        if numero_usuario != 1234 and tentativas_restantes_lv3 == 1:
            print("Você perdeu! :(")
            break
        elif numero_usuario == numero_secreto:
            pontuação_lv3 = tentativas_restantes_lv3 * 100
            print("Você venceu. Vítória! :)")
            print(f"Sua pontuação foi: {pontuação_lv3}")
            print(f"Tentativas utilizadas: {tentativas_utilizadas}")
            break
        elif numero_usuario != numero_secreto:
            if numero_usuario >= 1 and numero_usuario <= 100:
                print("Inválido! Apenas números de 4 dígitos são aceitos!\n")
                continue
            elif numero_usuario > numero_secreto:
                print("Número maior que o número secreto!\n")
                tentativas_restantes_lv3 = tentativas_restantes_lv3 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
            else:
                print("Número menor que o número secreto!\n") 
                tentativas_restantes_lv3 = tentativas_restantes_lv3 - 1
                tentativas_utilizadas = tentativas_utilizadas + 1
                continue
        else:
            print("Inválido!\n")
            continue    
    else:
        print("Inválido!")
        break