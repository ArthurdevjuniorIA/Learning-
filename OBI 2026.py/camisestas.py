numero_premiados = int(input())
tamanho_solicitados= list(map(int,input().split()))
quantas_P = int(input())
quantas_M = int(input())
if tamanho_solicitados.count(1)>quantas_P or tamanho_solicitados.count(2)>quantas_M:
    print("N")
else:
    print("S")
