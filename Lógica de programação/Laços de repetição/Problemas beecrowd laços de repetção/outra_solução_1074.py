n = int(input())
for _ in range(n):
    x = int(input())
    if x ==0:
        print("NULL")
    else:
        paridade = "EVEN" if x%2==0 else "ODD"
        sinal= "POSITIVE" if x>0 else "NEGATIVE"
        print(f"{paridade} {sinal}")