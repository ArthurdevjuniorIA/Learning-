quanto_vitorias = 0
for i in range(6):
    pontuacao = (input())
    if pontuacao == "V":
     quanto_vitorias+=1
if quanto_vitorias>=5:
    print(1)
elif quanto_vitorias>=3:
    print(2)
elif quanto_vitorias>=1:
    print(3)
else:
    print(-1)
        
