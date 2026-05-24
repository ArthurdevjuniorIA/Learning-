import random
numeros = random.sample(range(10), k=3)
print(f"Isso é só uma fase de teste por isso printarei {numeros}")

while True:
    palpite_usuario = input("Digite a sequência de 3 números (ou 'sair'): ")
    
    if palpite_usuario == "sair":
        print("Saindo do jogo...")
        break
   
    if len(palpite_usuario) != 3:
        print("Erro! Digite exatamente 3 números.")
        break
    else:
        if palpite_usuario[0] != numeros[0]:
            print("Errouuuuuu")
        elif palpite_usuario[0] == numeros[0]:
            print("Está quente, você acertou um número na posição correta")


