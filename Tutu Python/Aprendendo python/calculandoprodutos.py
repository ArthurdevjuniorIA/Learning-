while True:
    produto_x = int(input("Quantos chocolates você comprou? "))
    Valor_chocolate = produto_x * 7,90

    if produto_x <= 3:
        print("O que você acha de entrar na promoção leve 4 pague 5?\n caso queira, digite Eu quero caso contrário Eu não quero")
        resposta_oferta_abusiva = input()
        if resposta_oferta_abusiva == "Eu quero":
            print(f"Ótima escolha, pegue mais {4-produto_x} chocolate(s) da sua preferência e pague por 5")
            break
        else:
            print("Não tem essa escolha, digite tudo novamente")

    else:
        print("você está apto a promoção, leve 4 pague 5, o que você acha de participar\n caso queira, digite Eu quero caso contrário Eu não quero")
        resposta_oferta_abusivaa = input()
        if resposta_oferta_abusivaa == "Eu quero":
            print("Ainda bem que você escolheu esta opção, ótima escolha!")
            break
        else:
            print("Você não pode escolher essa opção, volte tudo do início")
    


    