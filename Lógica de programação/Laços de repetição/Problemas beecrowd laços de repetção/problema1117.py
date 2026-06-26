soma_notas = 0
contador_notas = 0
while True:
       nota_aluno = float(input()) 
       if nota_aluno>=0 and nota_aluno<=10:
             soma_notas = soma_notas+nota_aluno
             contador_notas+=1
       else:
            print("nota invalida")
       if contador_notas>=2:
            break
media = (soma_notas)/2
print(f"media = {media}")

            

