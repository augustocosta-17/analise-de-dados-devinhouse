import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df_clientes = pd.read_csv('clientes.csv')
df_vendas = pd.read_csv('vendas.csv')

# Definindo 'Não informado para valores ausentes na coluna 'nome'
df_clientes['nome'].fillna('Não informado', inplace=True)

# Definindo a coluna 'idade' como numérica e preenchendo valores ausentes com a média arredondada
df_clientes['idade'] = pd.to_numeric(df_clientes['idade'], errors='coerce')
df_clientes['idade'].fillna(df_clientes['idade'].mean().round(), inplace=True)

# Definindo 'não informado' para valores ausentes na coluna 'email'
df_clientes['email'].fillna('nao_informado@email.com', inplace=True)
print(df_clientes)