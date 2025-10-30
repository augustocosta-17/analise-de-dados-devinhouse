import pandas as pd
import numpy as np
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

df_dataset = pd.read_excel('dataset_clamed.xlsx')

#print(df_dataset.describe().round(2))
#print(df_dataset.info())
#print(df_dataset.isnull().sum())
#print('\n', df_dataset.duplicated().sum())
#print('\n', df_dataset.head(10))

df_dataset = df_dataset.drop_duplicates(subset=['id_produto', 'nome_produto'])
df_dataset['preco'].fillna(df_dataset['preco'].mean(), inplace=True)
df_dataset['quantidade_estoque'].fillna(0, inplace=True)
df_dataset['fornecedor'].fillna('Não informado', inplace=True)

q1 = df_dataset['preco'].quantile(0.25)
q3 = df_dataset['preco'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr
df_dataset_sem_outliers = df_dataset[(df_dataset['preco'] >= limite_inferior) & (df_dataset['preco'] <= limite_superior)]
outliers = df_dataset[(df_dataset['preco'] < limite_inferior) | (df_dataset['preco'] > limite_superior)]
print(outliers)