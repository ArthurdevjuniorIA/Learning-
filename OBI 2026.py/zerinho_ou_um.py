A,B,C = map(int, input().split())
if A != B and A!=C:
    print("A")
elif B !=A and B!=C:
    print("B")
elif C != A and C!=B:
    print("C")
else:
    print("*")
'''total_mes = float(input("Digite o total de despesas desse mês: "))
if total_mes>3000:
    print("Atenção! Você ultrapassou o limite do orçamento")
else:
    print("Você está dentro do orçamento")'''
'''horarios_permitidos = list(range(8,19))
hora = int(input("Digite a hora atual (formato 24 horas): "))
if hora not in horarios_permitidos:
    print("Acesso negado!")
else:
    print("Acesso permitido!")'''
'''nota_primeiro = float(input("Digite a primeira nota: "))
nota_segundo = float(input("Digite a segunda nota: "))
nota_terceiro = float(input("Digite a terceira nota: "))
media = (nota_primeiro+nota_segundo+nota_terceiro)/3
if media<5:
    print("Reprovado")
elif 5<=7:
    print("Recuperação")
else:
    print("Aprovado")'''
'''distancia_percorrida = float(input("Digite a distância percorrida(em km): "))
if distancia_percorrida<100:
    print("Valor pedágio: R$ 10,00")
elif 100<=distancia_percorrida<=200:
    print("Valor pedágio: R$ 20,00")
else:
    print("Valor pedágio: R$ 30,00")'''
'''inteiro = int(input("Digite um número inteiro: "))
if inteiro % 2 ==0:
    print("o número é par.")
else:
    print("O número é ímpar.")'''
'''renda_mensal = float(input("Digite o valor da sua renda mensal: "))
parcela_desejada = float(input("Digite o valor da parcela desejada: "))
if renda_mensal>2000 and parcela_desejada<(renda_mensal*0.3):
    print("Empréstimo concedido")
else:
    if renda_mensal<2000:
        print("Empréstimo negado: Renda abiaxo da mínima")
    elif parcela_desejada>(renda_mensal*0.3):
        print("Empréstimo negado: parcela acima de 30% da renda")'''