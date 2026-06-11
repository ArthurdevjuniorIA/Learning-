quota_mensal = int(input())
numero_meses = int(input())
mes_seguinte = quota_mensal
for i in range(numero_meses):
    Usou_mes = int(input())
    mes_seguinte= mes_seguinte+ quota_mensal -Usou_mes
print(mes_seguinte)

