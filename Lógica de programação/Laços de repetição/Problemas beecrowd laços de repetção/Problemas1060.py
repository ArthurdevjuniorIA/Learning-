positivos = 0
i =1
while i<=6:
    valor= float(input())
    if valor>0:
        positivos = positivos+1
    i = i+1
print(f"{positivos} valores positivos")
