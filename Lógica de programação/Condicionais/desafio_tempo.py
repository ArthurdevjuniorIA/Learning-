ano = int(input())
mes = int(input())
dia = int(input())
hora = int(input())
minuto = int(input())
segundo = int(input())
eh_bissexto = ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0
if minuto>59 or minuto<0 or hora>23 or segundo>59 or segundo<0 or mes>12 or mes<1 or 0>ano:
    print("ERRO: Data ou hora inválida!")
else:
    if eh_bissexto:
        if mes ==2:
            if dia>29 or dia<0:
                print("ERRO: Data ou hora inválida!")
    else:
        if mes == 2:
            if dia>28 or dia<0:
                print("ERRO: Data ou hora inválida!")
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia>31 or dia<0:
                print("ERRO: Data ou hora inválida!")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia>30 or dia<0:
                print("ERRO: Data ou hora inválida!")
        else: 
            segundo+1
            if segundo == 60:
                segundo = 60 -segundo
                minuto = minuto+1
            if minuto >= 60:
                minuto = 60 - minuto
                hora = hora+1
            if hora>= 24:
                hora = 24 - hora
                dia = dia+1
            if dia>= 31:
                dia = 31 - dia
                mes = mes+1
            if mes>= 12:
                mes = 12- mes
                ano = ano+1
            print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
                
                    



