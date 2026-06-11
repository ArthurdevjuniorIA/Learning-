volume_minimo_A = int(input())
volume_maximo_B = int(input())
capacidade_xicara = int(input())
volume_cafe = int(input())
if volume_minimo_A+volume_cafe>capacidade_xicara:
    print("N")
elif capacidade_xicara-volume_cafe>volume_maximo_B:
    print("N")
else:
    print("S")