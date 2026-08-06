nome_funcionario = [ ]
producao_de_todos = [ ]
com_maiores_producao = [ ]
produzido_por_todos = [ ]
menor_que_media =[ ]
soma_producao = 0
maior_producao = 0
soma_da_producao_cada = 0
while True:
    nome_do_funcionario = input("Nome do funcionário: ")
    if nome_do_funcionario == "fim":
        print("==============================\nRELATÓRIO GERAL DA SEMANA\n==============================")
        for some in producao_de_todos:
            soma_producao = some+soma_producao
        media_producao = soma_producao/len(nome_do_funcionario)
        print(f"Total de peças montadas: {soma_producao}")
        print(f"Média de produção por funcionário: {media_producao:.0f}")
        print(f"Funcionário(s) com maior produção semanal: ")
        for mais in com_maiores_producao:
            print(f"-{mais}")
        for i in range(len(produzido_por_todos)):
            for somando in produzido_por_todos[i]:
                soma_da_producao_cada = somando+soma_da_producao_cada
                if soma_da_producao_cada<media_producao:
                    menor_que_media.append(nome_do_funcionario[i])
        print("Funcionário(s) abaixo da média semanal: ")
        for menor in menor_que_media:
            print(f"-{menor}")
        break
        
    producao = list(map(int,input("Produção (Seg Ter Qua Qui Sex): ").split()))
    produzido_por_todos.append(producao)
    for produto in producao:
        producao_de_todos.append(produto)
    if nome_do_funcionario not in nome_funcionario:
        nome_funcionario.append(nome_do_funcionario)
        if sum(producao)>=maior_producao:
           maior_producao = sum(producao)
           com_maiores_producao.append(nome_do_funcionario)
        

    else:
        nome_funcionario.remove(nome_funcionario)