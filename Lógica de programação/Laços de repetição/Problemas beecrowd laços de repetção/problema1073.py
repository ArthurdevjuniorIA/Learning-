n = int(input())
valor_par = 0
if 5<n<2000:
    for i in range(n+1):
        if i % 2 == 0:
            valor_par+=i
            if i>1:
                print(f"{i}^2 = {i**2}")