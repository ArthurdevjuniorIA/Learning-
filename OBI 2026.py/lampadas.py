quantas_vezes = int(input())
acesa_ou_apagada = list(map(int,input().split()))
acesa = 1
apagada = 0
if quantas_vezes % 2 != 0:
    print(acesa)
else:
    print(apagada)
if acesa_ou_apagada.count(2) % 2 != 0:
    print(acesa)
elif acesa_ou_apagada.count(2) % 2 == 0:
    print(apagada)
