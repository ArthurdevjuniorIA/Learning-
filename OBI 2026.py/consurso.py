participantes_candidatos = list(map(int, input().split()))
notas_participantes = list(map(int, input().split()))
notas_participantes.sort()
media = sum(notas_participantes)/participantes_candidatos[0]
aprovados = max(notas_participantes)>media
print(aprovados)
