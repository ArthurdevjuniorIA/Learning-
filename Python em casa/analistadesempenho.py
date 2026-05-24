while True:
    nome_atleta = input("Qual é o seu nome? ")
    if nome_atleta == "Sair" or nome_atleta == "sair":
        break
    nota_atleta = float(input("Qual foi sua nota na competição? "))
    if nota_atleta<5.0:
        print("Eliminado")
    elif nota_atleta<7.4:
        print("Classificado para a respecagem")
    elif nota_atleta>7.5:
        print("Finalista garantido!")
    