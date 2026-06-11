x = int(input())
divisores = []
for i in range(1,int(x**0.5)+1):
    if x % i == 0:
        #adiciona o valor que o I percorre no intervalo a lista de divisores
        divisores.append(i)
        #isso evita repetir o 2 duas vezes (se x for 4, por exemplo)
        if i != x // i:
            divisores.append(x // i)
divisores.sort()
print(*divisores, end=" ")