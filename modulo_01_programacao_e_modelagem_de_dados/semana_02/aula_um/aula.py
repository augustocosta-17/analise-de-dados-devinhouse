media_final = float(input("Digite sua média final: "))
aulas_assistidas = int(input("Digite o número de aulas assistidas: "))

if media_final >= 7 and aulas_assistidas >= 40:
    print("Aprovado!")
else:
    print("Reprovado!")