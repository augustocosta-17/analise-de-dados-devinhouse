from datetime import datetime

data_input = input("Digite uma data (dd/mm/aaaa): ")

try:
    data_usuario = datetime.strptime(data_input, "%d/%m/%Y")
    ultimo_dia_ano = datetime(data_usuario.year, 12, 31)
    dias_restantes = (ultimo_dia_ano - data_usuario).days
    dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", 
                   "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    dia_semana = dias_semana[data_usuario.weekday()]
    
    print(f"\nData informada: {data_usuario.strftime('%d/%m/%Y')}")
    print(f"Dia da semana: {dia_semana}")
    print(f"Dias restantes até o final do ano: {dias_restantes}")
    
except ValueError:
    print("Erro: Data inválida. Use o formato dd/mm/aaaa")
