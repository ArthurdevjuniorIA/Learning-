x = int(input())
y = int(input())
inicio = min(x,y)
fim = max(x,y)
valores_impares = 0
for i in range(inicio+1,fim):
    if i % 2 !=0:
        valores_impares +=i
print(valores_impares)