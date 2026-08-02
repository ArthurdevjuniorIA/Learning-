numero = int(input())
binario = list(map(int,input().split()))
quantos_100 = 0
if [binario::3] == 100:
    quantos_100+=1
print(quantos_100)