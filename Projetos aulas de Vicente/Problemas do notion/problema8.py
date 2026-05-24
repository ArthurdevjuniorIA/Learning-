hora = int(input())
minuto = int(input())
segundo = int(input())

if hora>23 or hora<0:
    print("[ERRO] horas devem está no intervalo 0 - 23")
if minuto>59 or minuto<0:
    print("[ERRO] minutos devem está no intervalo 0 - 59")
  
if segundo>59 or segundo<0:
      print("[ERRO] segundos devem está no intervalo 0 - 59")
else:
    print("Alarme registrado")