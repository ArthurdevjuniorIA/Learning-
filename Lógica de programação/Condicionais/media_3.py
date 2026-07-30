N1, N2, N3, N4 = float(input())
media = ((N1*2)+(N2*3)+(N3*4)+(N4))/10
if media>=7:
    print(f"Media: {media:.1f}")
    print("Aluno provado")
elif media>4.9:
    print(f"Media: {media:.1f}")
    print("Aluno em exame")
    exame = float(input())