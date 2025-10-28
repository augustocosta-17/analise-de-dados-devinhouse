qtd_alunos = int(input("Digite quantos alunos você deseja cadastrar: "))
alunos = []

for i in range(qtd_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f"Digite a nota {j+1} de {nome}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota deve ser entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
    alunos.append((nome, notas))

aprovados = []
reprovados = []

for nome, notas in alunos:
    média = sum(notas) / len(notas)
    if média >= 7:
        aprovados.append((nome, média))
    else:
        reprovados.append((nome, média))

print("\nAprovados:")
for nome, média in aprovados:
    print(f"{nome} média {média:.2f}")

print("\nReprovados:")
for nome, média in reprovados:
    print(f"{nome} média {média:.2f}")
