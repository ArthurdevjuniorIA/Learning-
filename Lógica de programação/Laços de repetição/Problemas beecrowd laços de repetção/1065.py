valores_pares = 0
for i in range(5):
    valor = int(input())
    if valor % 2 == 0:
        valores_pares = valores_pares+1
    i = i+1
print(f"{valores_pares} valores pares")
print(i)
