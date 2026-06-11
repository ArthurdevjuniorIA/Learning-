horario_original = int(input())
minutos = int(input())
segundos = int(input())
tempo_adiado = int(input())
if 0<=horario_original<=23 and 0<=minutos<=59 and 0<=segundos<=59:
    segundos = tempo_adiado+segundos
    while segundos>=60:
        if segundos>59:
            segundos = segundos-60
            minutos +=1
        if minutos>59:
            minutos = minutos-60
            horario_original +=1
        if horario_original>=24:
            horario_original= horario_original-24
print(horario_original)
print(minutos)
print(segundos)
         