nome_funcionario = [ ]
soma_producao = 0
while True:
    nome_do_funcionario = input("Nome do funcionário: ")
    if nome_do_funcionario == "fim":
        print("==============================\nRELATÓRIO GERAL DA SEMANA\n==============================")
        for some in producao:
            soma_producao = some+soma_producao
        media_producao = soma_producao/len(producao)
        print(f"Total de peças montadas: {soma_producao}")
        print(f"Média de produção por funcionário: {media_producao:.0f}")
        break
    producao = list(map(int,input("Produção (Seg Ter Qua Qui Sex): ").split()))
    if nome_do_funcionario not in nome_funcionario:
        nome_funcionario.append(nome_do_funcionario)

    else:
        nome_funcionario.remove(nome_funcionario)