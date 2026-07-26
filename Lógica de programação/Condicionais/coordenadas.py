x = float(input())
y = float(input())
if x<0:
    if y<0:
        print("Está no terceiro quadrante")
    else:
        print("Está no segundo quadrante")
elif x>0:
    if y<0:
        print("Está no quarto quadrante")
    else:
        print("Está no primeiro quadrante ")
else:
    print("ponto está localizado na origem")