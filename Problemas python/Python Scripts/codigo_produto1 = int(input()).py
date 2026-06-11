cod1, qte1, valor1 = map(float, input().split())
cod2, qte2, valor2 = map(float, input().split())
valor_total= qte1*valor1+ qte2*valor2
print(f"VALOR A PAGAR: R$ {valor_total:.2f}")