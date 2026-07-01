for i in range(10,-1,-1):
    if i ==0:
        print("Aproveite a promoção agora!")
        break
    if i % 2 == 0:
        print(f"Falta apenas {i} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {i} segundos restantes.")