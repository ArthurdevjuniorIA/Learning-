sigla_padrao_programacao= input()
linguas_disponiveis = ["pt", "en", "es", "fr", "it"]
if sigla_padrao_programacao == linguas_disponiveis[0]:
    print("Olá mundo!")
elif sigla_padrao_programacao == linguas_disponiveis[1]:
    print("Hello World!")
elif sigla_padrao_programacao == linguas_disponiveis[2]:
    print("¡Hola, mundo!")
elif sigla_padrao_programacao == linguas_disponiveis[3]:
    print("Bonjour, monde!")
elif sigla_padrao_programacao == linguas_disponiveis[4]:
    print("Ciao, mondo!")
else:
    print("Idioma não suportado")