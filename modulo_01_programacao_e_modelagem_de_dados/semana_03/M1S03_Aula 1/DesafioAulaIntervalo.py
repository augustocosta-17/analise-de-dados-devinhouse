import random

resultados = []

for _ in range(100):
    lancamento = random.randint(1, 6)
    resultados.append(lancamento)

contador = [0] * 6

for numero in resultados:
    contador[numero - 1] += 1

for i in range(6):
    print(f"O número {i + 1} apareceu {contador[i]} vezes")
