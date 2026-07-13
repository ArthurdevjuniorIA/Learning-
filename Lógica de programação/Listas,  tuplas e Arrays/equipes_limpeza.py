equipes_de_3 = [ ]
equipes = [ ]
while True:
    voluntario = input("Nome do voluntário (ou 'fim' para encerrar): ")
    if voluntario  == "fim":
        for i in range(len(equipes)):
                print(f"Equipe {i}")
                print(*equipes[i])
        break
        
    else:
        equipes_de_3.append(voluntario)
        if len(equipes_de_3) == 3:
                equipes.append(equipes_de_3)
                equipes_de_3.copy()

           

