somando = 0
i =1
while i <=10:
    valor= int(input())
    if valor<=0:
        break
    somando = somando+valor
    i= i+1
print(f"{somando} É A SOMA DOS 10 NÚMEROS")