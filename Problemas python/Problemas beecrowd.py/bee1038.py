pedido_usuario = map(input().split())
possiveis_pedidos = {"1": "R$4.00","2": "R$4.50", "3": "R$5.00", "4": "R$2.00", "5": "R$1.50"}
total = possiveis_pedidos.get(pedido_usuario)
print(f"TOTAL:R${total}")
