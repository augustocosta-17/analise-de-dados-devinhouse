entrada = input("Digite algo: ")

try:
    valor = int(entrada)
    print(f"Tipo: {type(valor)}")
except ValueError:
    try:
        valor = float(entrada)
        print(f"Tipo: {type(valor)}")
    except ValueError:
        print(f"Tipo: {type(entrada)}")
