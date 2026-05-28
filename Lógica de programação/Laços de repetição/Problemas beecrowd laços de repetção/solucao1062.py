quantidade_positivos = 0
soma_positivo = 0
for i in range(6):
    valor = float(input())
    if valor>0:
        quantidade_positivos+=1
        soma_positivo+=valor
media = soma_positivo/quantidade_positivos
print(F"{quantidade_positivos} valores positivos")
print(f"{media:.2f}")