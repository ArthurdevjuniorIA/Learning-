numero_dias = int(input())
total_acessos = 0
for i in range(1,numero_dias+1):
    acessos_dia = int(input())
    total_acessos =acessos_dia+total_acessos
    if total_acessos>=1000000:
        print(i)
        break
