copos_derrubados = 0
numero_bandeja = int(input())
for i in range(numero_bandeja):
    latas_copos = list(map(int,input().split()))
    if latas_copos[0]>latas_copos[1]:
       copos_derrubados = copos_derrubados+ latas_copos[1]
print(copos_derrubados)