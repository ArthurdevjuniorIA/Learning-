number1= float(input())
if 0<=number1<=25.0000:
    print ("Intervalo [0,25]")
elif 25.00001<number1<=50.0000000:
    print("Intervalo (25,50]")
elif 50.0000000<number1<=75.000000:
    print("Intervalo (50,75]")
elif 75.0000000<number1<=100.00000:
    print("Intervalo (75,100]")
else: 
    print("Fora de intervalo")  