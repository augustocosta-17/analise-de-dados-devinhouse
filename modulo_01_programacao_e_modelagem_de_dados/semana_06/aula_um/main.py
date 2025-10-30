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

# Removendo duplicatas
df_clientes.drop_duplicates(subset=['nome', 'email'], inplace=True)

# Corrigindo as inconsistências do email no padrão errado
df_clientes['email'] = df_clientes['email'].str.replace(r'@email$', '@email.com', regex=True)

# Deixando a coluna data como datetime (aceita múltiplos formatos 00-00-0000, 00/00/0000, 0000-00-00)
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'], format='mixed', errors='coerce')

# Transformando a coluna 'quantidade' e 'preco' em numéricas e preenchendo valores ausentes
df_vendas['quantidade'] = pd.to_numeric(df_vendas['quantidade'], errors='coerce')
df_vendas['preco_unitario'] = pd.to_numeric(df_vendas['preco_unitario'], errors='coerce')
df_vendas.fillna({'quantidade': 1, 'preco_unitario': df_vendas['preco_unitario'].mean().round()}, inplace=True)

# Calculando os quartis para a coluna 'preco_unitario' para definirmos outliers
q1 = df_vendas['preco_unitario'].quantile(0.25)
q3 = df_vendas['preco_unitario'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
df_vendas_sem_outliers = df_vendas[(df_vendas['preco_unitario'] >= limite_inferior) & (df_vendas['preco_unitario'] <= limite_superior)]

# Normalização dos dados de preço unitário entre 0 e 1
min_preco = df_vendas_sem_outliers['preco_unitario'].min()
max_preco = df_vendas_sem_outliers['preco_unitario'].max()
df_vendas_sem_outliers['preco_unitario'] = (df_vendas_sem_outliers['preco_unitario'] - min_preco) / (max_preco - min_preco)
df_vendas_sem_outliers = df_vendas_sem_outliers.sort_values('preco_unitario')

# Normalização das idades dos clientes entre 0 e 1
min_idade = df_clientes['idade'].min()
max_idade = df_clientes['idade'].max()
df_clientes['idade'] = (df_clientes['idade'] - min_idade) / (max_idade - min_idade)
df_clientes = df_clientes.sort_values('idade')

# Junção dos dataframes de clientes e vendas
df_final = pd.merge(df_vendas_sem_outliers, df_clientes, left_on='id_cliente', right_on='id', how='inner')
df_final = df_final.drop(columns=['id_cliente', 'id'])
print(df_final)
