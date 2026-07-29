from random import randint

# O computador escolhe um número de 1 a 1000
computador = randint(1, 1000)
acertou = False
tentativas = 0

print("Sou seu computador e pensei em um número entre 1 e 10. Tente adivinhar!")

while not acertou:
    palpite = int(input("Qual é o seu palpite? "))
    tentativas += 1
    
    if palpite == computador:
        acertou = True
    else:
        if palpite < computador:
            print("Mais... Tente novamente!")
        else:
            print("Menos... Tente novamente!")

print(f"Parabéns! Você acertou em {tentativas} tentativas.")
