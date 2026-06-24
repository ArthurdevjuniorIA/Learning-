lista =[]
while True:
    alunos = input("Digite o nome do participante (ou 'fim' para encerrar): ")
    if alunos != "fim":
        lista.append(alunos)
    if alunos == "fim":
        print("=== LISTA DE PRESENÇA ===")
        for n in lista:
            print(n)
