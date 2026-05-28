n = int(input())
for _ in range(n):
    x = int(input())
    if x ==0:
        print("Null")
    else:
        paridade = "even" if x%2==0 else "ODD"
        sinal= "positive" if x>0 else "Negative"
        print(f"{paridade} {sinal}")