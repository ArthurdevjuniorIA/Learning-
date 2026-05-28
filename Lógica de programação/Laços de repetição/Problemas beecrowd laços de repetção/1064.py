i=1
SOMA=0
positivos=0
while i<=6:
    A=float(input())
    if A>0:
        positivos=positivos+1
        SOMA=SOMA+A
    i=i+1
MEDIA=SOMA/positivos
print(f"{positivos} valores positivos")
print(f"{MEDIA:.1f}")