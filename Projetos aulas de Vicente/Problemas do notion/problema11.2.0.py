sigla_padrao = input()
saudacoes= {"pt":"Olá Mundo!","en": "Hello Wolrd!", "es": "¡Hola, mundo!","fr": "Bonjour, monde!", "it": "Ciao,mondo!"}
resultado = saudacoes.get(sigla_padrao, "Idioma não suportado")
print(resultado)