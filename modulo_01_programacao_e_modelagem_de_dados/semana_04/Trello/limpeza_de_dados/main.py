import re
import csv
import os

emails = [
    "usuario@exemplo.com",
    "teste.email@dominio.org", 
    "invalido@",
    "email_sem_dominio",
    "usuario@dominio",
    "123@teste.com.br",
    "@dominio.com",
    "email.com"
]

padrao = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
validos = []
invalidos = []

for email in emails:
    if re.match(padrao, email.strip()):
        validos.append(email)
    else:
        invalidos.append(email)

pasta_script = os.path.dirname(os.path.abspath(__file__))
arquivo_validos = os.path.join(pasta_script, 'validos.csv')
arquivo_invalidos = os.path.join(pasta_script, 'invalidos.csv')

with open(arquivo_validos, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])
    for email in validos:
        writer.writerow([email])

with open(arquivo_invalidos, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Email'])
    for email in invalidos:
        writer.writerow([email])

print(f"Arquivos CSV criados na pasta: {pasta_script}")
print(f"- validos.csv ({len(validos)} emails)")
print(f"- invalidos.csv ({len(invalidos)} emails)")
