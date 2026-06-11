import random

opcoes = ["Maçã", "Banana", "Laranja", "Uva", "Morango"]

# Se k=1, ele retorna uma lista com 1 fruta
# Se k=3, ele retorna uma lista com 3 frutas
selecao = random.sample(opcoes, k=2)

print(selecao)