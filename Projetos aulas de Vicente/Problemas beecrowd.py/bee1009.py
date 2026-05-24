nome_trabalhador= (input())
salario_vendedor= float(input())
produtos_vendidos = float(input())
salario_final = salario_vendedor+produtos_vendidos*0.15
print(f"TOTAL = R$ {salario_final:.2f}")