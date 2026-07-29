A = int(input("Digite um número qualquer maior que 2 e menor que o próximo que você vai digitar: "))
B = int(input("Digite um número qualquermaior que o anterior que você digitou: "))
quantidade_total_comprimento_collatz = 0
eh_maior = 0
maior_comprimento_collatz = 0
for N in range(A,B+1):
    teste = N
    testando = N
    comprimento_collatz = 0
    while testando>1:
        if testando % 2 == 0:
            testando = testando/2
            comprimento_collatz+=1
        elif testando % 2 !=0:
            testando = 3*testando+1
            comprimento_collatz+=1
    if testando == 1:
        divisivel = 0
        for i in range(1,comprimento_collatz+1):
            if comprimento_collatz % i == 0:
                divisivel +=1
        if divisivel == 2:
            quantidade_total_comprimento_collatz +=1
            if comprimento_collatz>maior_comprimento_collatz:
                maior_comprimento_collatz = comprimento_collatz
                eh_maior = N
            elif comprimento_collatz == maior_comprimento_collatz:
                if eh_maior - N > 0:
                    eh_maior = N
                else:
                    eh_maior = eh_maior
print(f"Há {quantidade_total_comprimento_collatz} com comprimento collatz")
print(f"{eh_maior} venceu, com um comprimento Collatz primo de {maior_comprimento_collatz} passos!")