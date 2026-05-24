# 1. Recebe o total de dias do usuário
total_dias = int(input())

# 2. Define as listas de divisores e as etiquetas correspondentes
divisores = [365, 30]
tempos = ["ano(s)", "mes(es)"]

# 3. O laço 'for' percorre as duas listas ao mesmo tempo usando o 'zip'
for d, t in zip(divisores, tempos):
    
    # O divmod divide o total pelo divisor atual (365 ou 30)
    # 'qtd' guarda o resultado (quantos cabem)
    # 'total_dias' é atualizado com o resto da divisão para a próxima volta
    qtd, total_dias = divmod(total_dias, d)
    
    # Imprime a quantidade e a etiqueta exata exigida pelo problema
    print(f"{qtd} {t}")

# 4. O que sobrou no total_dias após o laço são os dias finais
print(f"{total_dias} dia(s)")