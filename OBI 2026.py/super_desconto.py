quantidade_produtos = int(input())
frete_padrao = 20
soma_produto = 0
apenas_um = 0
for i in range(quantidade_produtos):
    valor_produto = float(input())
    tem_brinde = valor_produto == 0
    if valor_produto<0:
        continue
    soma_produto = valor_produto + soma_produto
    if tem_brinde == True:
        apenas_um +=1
        if apenas_um>=2:
            continue
if soma_produto>=150 and apenas_um == 0:
    frete_padrao = 0
    soma_produto = soma_produto + frete_padrao
else:
    soma_produto = soma_produto + frete_padrao
print(f"Total: R$ {soma_produto:.2f}")