quantidade_produtos = int(input())
frete_padrao = 20
soma_produto = 0
for i in range(quantidade_produtos):
    valor_produto = float(input())
    if valor_produto<0:
        continue
    soma_produto = valor_produto + soma_produto
    if valor_produto == 0:
        frete_padrao = 20
        soma_produto = soma_produto + frete_padrao
if soma_produto>=150 and valor_produto != 0:
    frete_padrao = 0
    soma_produto = soma_produto + frete_padrao
elif soma_produto<150:
    soma_produto = soma_produto + frete_padrao
print(f"Total = {soma_produto} R$")