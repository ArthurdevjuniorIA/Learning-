Salario= float(input())
if 0<Salario<=400.00:
    print(f"Novo salario: {Salario*0.15+ Salario:.2f}")
    print(f"Reajuste ganho: {Salario*0.15:.2f}")
    print("Em percentual: 15 %")
elif 400<Salario<= 800.00:
    print(f"Novo salario: {Salario*0.12+ Salario:.2f}")
    print(f"Reajuste ganho: {Salario*0.12:.2f}")
    print("Em percentual: 12 %")
elif 800<Salario<= 1200.00:
    print(f"Novo salario: {Salario*0.10+ Salario:.2f}")
    print(f"Reajuste ganho: {Salario*0.10:.2f}")
    print("Em percentual: 10 %")
elif 1200<Salario<= 2000.00:
    print(f"Novo salario: {Salario*0.07+ Salario:.2f}")
    print(f"Reajuste ganho: {Salario*0.07:.2f}")
    print("Em percentual: 7 %")
elif 2000.00<Salario:
    print(f"Novo salario: {Salario*0.04+ Salario:.2f}")
    print(f"Reajuste ganho: {Salario*0.04:.2f}")
    print("Em percentual: 4 %")

