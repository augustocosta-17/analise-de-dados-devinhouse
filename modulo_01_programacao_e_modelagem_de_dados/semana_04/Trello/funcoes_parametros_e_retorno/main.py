def calcular_media(numeros):
    return sum(numeros) / len(numeros)


def encontrar_maior_menor(numeros):
    return max(numeros), min(numeros)


def main():
    numeros = [10, 5, 8, 20, 3, 15, 12]
    
    media = calcular_media(numeros)
    
    maior, menor = encontrar_maior_menor(numeros)
    
    print(f"Lista de números: {numeros}")
    print(f"Média dos números: {media:.2f}")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")


if __name__ == "__main__":
    main()
