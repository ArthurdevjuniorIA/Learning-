nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
atendimento_prioritario = [ ]
atendimento_normal = [ ]
if idade>=60:
    atendimento_prioritario.append(idade)
else:
    atendimento_normal.append(idade)
for i in range(len(atendimento_normal)):
    for idoso in atendimento_prioritario:
        if atendimento_prioritario == [ ]:
            print(atendimento_normal[1-i])