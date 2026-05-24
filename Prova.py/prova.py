## Questão 1
nome_usuario= input() ##  Pede o nome do usuário
print(f"OI {nome_usuario}!") ## Depois de uma string formatado ele printa mensagem
## Qustão 2
gruas_celsius = float(input())
converter_fahreheint = (gruas_celsius * 1.8) +32
print(f"Temperatura em Farenheit {converter_fahreheint:.2f}")
## Questão 3
gruas_celsius = float(input())
converter_fahreheint = (gruas_celsius * 1.8) +32
if -273.15>gruas_celsius:
    print("Temperatura inválida")
else:
    print(f"Temperatura em Farenheit {converter_fahreheint:.2f}")
## Questão 4
valor_original = float(input())
if valor_original>=100:
    print(f"Valor original:{valor_original}")
    print("Desconto: 10%")
    print(f"Valor final:{valor_original*0.9}")
elif valor_original>=50:
    print(f"Valor original:{valor_original}")
    print("Desconto: 5%")
    print(f"Valor final:{valor_original*0.95}")
else:
     print(f"Valor original:{valor_original}")
     print("Sem desconto")
## Questão 5
jogada1 = (input())
jogada2 = (input())
if jogada1 == "pedra" and jogada2 == "tesoura":
    print("Jogador 1 venceu")
elif jogada1 == "tesoura" and jogada2 == "pedra":
    print("Jogador 2 venceu")
elif jogada1 == "papel" and jogada2 == "tesoura":
    print("Jogador 2 venceu")
elif jogada1 == "tesoura" and jogada2 == "papel":
    print("Jogador 1 venceu")
elif jogada1 == "papel" and jogada2 == "pedra":
    print("Jogador 1 venceu")
elif jogada1 == "pedra" and jogada2 == "papel":
    print("Jogador 2 venceu")
else:
    print("Empate")