tudo_junto = list(map(int, input().split()))
primeira_parte= tudo_junto[0]*tudo_junto[1]
segunda_parte = tudo_junto[2]*tudo_junto[3]
if primeira_parte == segunda_parte:
    print(0)
elif primeira_parte<segunda_parte:
    print(1)
else:
    print(-1)    
   