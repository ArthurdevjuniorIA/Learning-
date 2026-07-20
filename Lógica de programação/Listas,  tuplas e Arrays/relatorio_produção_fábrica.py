nome_funcionario = [ ]
producao_lista = [ ]
while True:
    nome_do_funcionario = input("Nome do funcionário: ")
    if nome_do_funcionario == "fim":
        print("==============================\nRELATÓRIO GERAL DA SEMANA\n==============================")
        soma_producao = sum(producao_lista)
        print(soma_producao)
        break
    producao = map(int,input("Produção (Seg Ter Qua Qui Sex): ").split())
    if nome_do_funcionario not in nome_funcionario:
        nome_funcionario.append(nome_do_funcionario)
        producao_lista.append(producao)

    else:
        nome_funcionario.remove(nome_funcionario)