i=1
SOMA=0
pos=0
while i<=6:
    A=float(input())
    SOMA=SOMA+A
    if A>0:
        pos=pos+1
    i=i+1
MEDIA=SOMA/6
print(f"{pos} valores positivos")
print(f"{MEDIA}")