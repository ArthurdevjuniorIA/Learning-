maior=-1 
for i in range(1,101):
    x=int(input())
    if x>maior:
        maior=x
        posicao_maior = i
print(maior)
print(posicao_maior)