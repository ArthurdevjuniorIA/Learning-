''''clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
nome = clientes
nome = " ".join(nome)
print(nome)'''
'''valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma = soma+valor
print(soma)'''
projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
'''for none in projetos:
    if none is None:
        print("Projeto ausente!")
    else:
        print(none)'''
'''livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
for hobbit in livros:
    if hobbit == "O Hobbit":
        print("Livro encontrado: O hobbit")
        break'''
for i in range(4,-1,-1):
    print(f"Venda realizada! Estoque restante: {i}")
    if i == 0:
        print("Estoque acabou")