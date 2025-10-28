notas_alunos = {
    "Ana": [8.5, 9.0, 10.0],
    "Bruno": [7.0, 2.5, 8.0],
    "Carla": [9.5, 10.0, 6.0],
    "Diego": [6.0, 5.5, 7.0],
    "Daniel": [6.0, 3.4, 9.8]
}

def calcular_media(notas):
    return sum(notas) / len(notas)

for aluno, notas in notas_alunos.items():
    media = calcular_media(notas)
    if media >= 7.0:
        print(f'{aluno}: Aprovado com média {media:.2f}')

