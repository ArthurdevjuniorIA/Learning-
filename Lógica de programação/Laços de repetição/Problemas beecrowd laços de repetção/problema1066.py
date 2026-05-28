numeros_pares = 0
numeros_impares = 0
numeros_positivos = 0
numeros_negativos = 0
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        numeros_pares+=1
    else:
        numeros_impares+=1
    if x>0:
        numeros_positivos+=1
    elif x<0:
        numeros_negativos+=1
print(f"{numeros_pares} valor(es) par(es)")
print(f"{numeros_impares} valor(es) impar(es)")
print(f"{numeros_positivos} valor(es) positivo(s)")
print(f"{numeros_negativos} valor(es) negativo(s)")