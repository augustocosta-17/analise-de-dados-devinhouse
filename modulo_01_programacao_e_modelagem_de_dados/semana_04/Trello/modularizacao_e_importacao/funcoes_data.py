from datetime import datetime, timedelta

def data_atual():
    return datetime.now()

def formatar_data(data):
    return data.strftime("%d/%m/%Y")

def diferenca_dias(data1, data2):
    return (data2 - data1).days

def adicionar_dias(data, dias):
    return data + timedelta(days=dias)