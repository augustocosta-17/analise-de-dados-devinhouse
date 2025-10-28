import random

numero_secreto = random.randint(1, 100)
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Digite um número entre 1 e 100: "))
    
    if tentativa > numero_secreto:
        print("Menor!")
    elif tentativa < numero_secreto:
        print("Maior!")
    else:
        print("Parabéns, você acertou!")
