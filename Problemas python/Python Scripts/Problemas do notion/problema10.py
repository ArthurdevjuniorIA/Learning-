valor_imposto = float(input())
if 0<valor_imposto<2000:
    print("Isento")
elif valor_imposto<=3000:
    print((3000-valor_imposto) * 0.08)
elif valor_imposto<=4500:
    novo_valor = ((valor_imposto-3000)*0.18) +1000 *0.08
    print(novo_valor)
else:
    imposto_maximo = (valor_imposto-4500) *0.28+ 1500*0.18+ 1000*0.08
    print(imposto_maximo)