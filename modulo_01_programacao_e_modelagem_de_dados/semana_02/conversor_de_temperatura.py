print("Conversor de Temperatura")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")
print("3 - Celsius para Kelvin")

opcao = int(input("Escolha uma opção (1-3): "))
if opcao not in [1, 2, 3]:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
    exit()
temp = float(input("Digite a temperatura: "))

if opcao == 1:
    resultado = (temp * 9/5) + 32
    print(f"{temp}°C = {resultado:}°F")
elif opcao == 2:
    resultado = (temp - 32) * 5/9
    print(f"{temp}°F = {resultado:}°C")
elif opcao == 3:
    resultado = temp + 273.15
    print(f"{temp}°C = {resultado:}K")