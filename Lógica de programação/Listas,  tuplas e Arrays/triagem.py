while True:
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    atendimento_prioritario = [ ]
    atendimento_normal = [ ]
    if idade>=60:
        atendimento_prioritario.append(idade)
    else:
        atendimento_normal.append(idade)