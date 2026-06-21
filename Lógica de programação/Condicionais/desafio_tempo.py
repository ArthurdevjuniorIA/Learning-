ano = int(input())
mes = int(input())
dia = int(input())
hora = int(input())
minuto = int(input())
segundo = int(input())
segundo = segundo+1
eh_bissexto = ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0
if minuto>59 or minuto<0 or hora>23 or segundo>59 or segundo<0 or mes>12 or mes<1 or 0>ano:
    print("ERRO: Data ou hora inválida!")
else:
    if eh_bissexto:
        if mes == 2 and dia>29 or dia<=0:
            print("ERRO: Data ou hora inválida!")
        elif mes == 2:
            if segundo == 60:
                segundo = segundo- 60
                minuto = minuto+1
            if minuto >= 60:
                minuto = minuto - 60
                hora = hora+1
            if hora>= 24:
                hora = hora - 24
                dia = dia+1
            if dia>= 30:
                dia = dia -29
                mes = mes+1
            print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
            if dia>31 or dia<=0:
                print("ERRO: Data ou hora inválida!")
            else: 
                if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                    if segundo == 60:
                        segundo = segundo- 60
                        minuto = minuto+1
                    if minuto >= 60:
                        minuto = minuto - 60
                        hora = hora+1
                    if hora>= 24:
                        hora = hora - 24
                        dia = dia+1
                    if dia>= 31:
                        dia = dia -31
                        mes = mes+1
                    if mes> 12:
                        mes = mes -12
                        ano = ano+1
                    print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
            if dia>30 or dia<=0:
                print("ERRO: Data ou hora inválida!")
            else:
                if segundo == 60:
                    segundo = segundo- 60
                    minuto = minuto+1
                if minuto >= 60:
                    minuto = minuto - 60
                    hora = hora+1
                if hora>= 24:
                    hora = hora - 24
                    dia = dia+1
                if dia>=31:
                    dia = dia -30
                    mes = mes+1
                if mes> 12:
                    mes = mes -12
                    ano = ano+1
                print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")

    elif  eh_bissexto == False:
        if mes == 2 and dia>28 or dia<=0:
            print("ERRO: Data ou hora inválida!")
        elif mes == 2:
            if segundo == 60:
                segundo = segundo- 60
                minuto = minuto+1
            if minuto >= 60:
                minuto = minuto - 60
                hora = hora+1
            if hora>= 24:
                hora = hora - 24
                dia = dia+1
            if dia> 29:
                dia = dia -28
                mes = mes+1
            print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
        else:
            if mes == 2 and dia>28 or dia<=0:
                print("ERRO: Data ou hora inválida!")
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12: 
                if dia>31 or dia<0:
                    print("ERRO: Data ou hora inválida!")
                else: 
                    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
                        if segundo == 60:
                            segundo = segundo- 60
                            minuto = minuto+1
                        if minuto >= 60:
                            minuto = minuto - 60
                            hora = hora+1
                        if hora>= 24:
                            hora = hora - 24
                            dia = dia+1
                        if dia> 31:
                            dia = dia -31
                            mes = mes+1
                        if mes> 12:
                            mes = mes -12
                            ano = ano+1
                        print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
            elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
                if dia>30 or dia<=0:
                    print("ERRO: Data ou hora inválida!")
                else:
                    if segundo == 60:
                        segundo = segundo- 60
                        minuto = minuto+1
                    if minuto >= 60:
                        minuto = minuto - 60
                        hora = hora+1
                    if hora>= 24:
                        hora = hora - 24
                        dia = dia+1
                    if dia> 30:
                        dia = dia -30
                        mes = mes+1
                    if mes> 12:
                        mes = mes -12
                        ano = ano+1
                    print(f"{ano}:{mes}:{dia}:{hora}:{minuto}:{segundo}")
                    



