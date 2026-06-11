a,b = map(int, input().split())
sequencia_A = list(map(int,input().split()))
sequencia_B = list(map(int,input().split()))
posicao_b = 0
for numero_a in sequencia_A:
    if numero_a == sequencia_B[posicao_b]:
        posicao_b+=1
else:
    print("N")
    