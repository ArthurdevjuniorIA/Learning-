nome_funcionario = [ ]
producao_de_todos = [ ]
soma_producao = 0
while True:
    nome_do_funcionario = input("Nome do funcionário: ")
    if nome_do_funcionario == "fim":
        print("==============================\nRELATÓRIO GERAL DA SEMANA\n==============================")
        for some in producao_de_todos:
            soma_producao = some+soma_producao
        media_producao = producao_de_todos/len(producao_de_todos)
        print(f"Total de peças montadas: {soma_producao}")
        print(f"Média de produção por funcionário: {media_producao:.0f}")
        break
        
    producao = list(map(int,input("Produção (Seg Ter Qua Qui Sex): ").split()))
    for produto in producao:
        producao_de_todos.append(produto)
    if nome_do_funcionario not in nome_funcionario:
        nome_funcionario.append(nome_do_funcionario)
        maior_producao = sum(producao)
        if sum(producao)>maior_producao:
            maior_producao = nome_do_funcionario

    else:
        nome_funcionario.remove(nome_funcionario)