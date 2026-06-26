limite = int(input())
for i in range(1,limite+1):
    i = i % 2
    if i == 0:
        print("even")
    else:
        print("odd")
