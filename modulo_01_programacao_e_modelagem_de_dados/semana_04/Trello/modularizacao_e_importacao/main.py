import funcoes_calculo
import funcoes_data
from datetime import datetime

print("Testando operações matemáticas:")
a = 10
b = 5
print(f"{a} + {b} = {funcoes_calculo.somar(a, b)}")
print(f"{a} - {b} = {funcoes_calculo.subtrair(a, b)}")
print(f"{a} * {b} = {funcoes_calculo.multiplicar(a, b)}")
print(f"{a} / {b} = {funcoes_calculo.dividir(a, b)}")
print(f"{a} ^ {b} = {funcoes_calculo.potencia(a, b)}")

print("\nTestando operações com datas:")
hoje = funcoes_data.data_atual()
print(f"Data atual: {funcoes_data.formatar_data(hoje)}")

data1 = datetime(2024, 1, 1)
data2 = datetime(2024, 12, 31)
print(f"Diferença entre 01/01/2024 e 31/12/2024: {funcoes_data.diferenca_dias(data1, data2)} dias")

nova_data = funcoes_data.adicionar_dias(hoje, 30)
print(f"Data daqui a 30 dias: {funcoes_data.formatar_data(nova_data)}")