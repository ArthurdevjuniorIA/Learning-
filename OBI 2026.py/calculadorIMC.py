peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))
IMC = peso/(altura**2)
print(f"Seu IMC é: {IMC:.2f}")
if IMC<18.5:
    print("Você está abaixo do peso")
elif IMC<25:
    print("Você está no peso normal")
else:
     print("Você está acima do peso")
     altura_ideal = peso/altura ==25
     print(altura_ideal)