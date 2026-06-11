idade_em_dias = int(input())
ano = idade_em_dias//365
RESTO1 = idade_em_dias % 365
meses = RESTO1//30
dias = RESTO1 -meses*30
print(f"{ano} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")