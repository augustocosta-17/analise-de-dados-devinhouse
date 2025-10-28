import pandas as pd
import numpy as np

produtos = pd.read_csv('produtos.csv')
vendas = pd.read_csv('vendas.csv')
categorias = pd.read_csv('categorias.csv')

df_prod_cat = pd.merge(produtos, categorias, on='id_categoria', how='left')
df_prod_cat_media = df_prod_cat.groupby('nome_categoria').agg({'preco': 'mean'}).reset_index()

produtos_filtrados = produtos[(produtos['preco'] > 20) & (produtos['estoque'] < 200)]

produtos_filtrados.to_csv('relatorio_estoque_critico.csv', index=False)

print(f"\nProdutos com preço > 20 e estoque < 200: {len(produtos_filtrados)} produtos")
print("Arquivo 'relatorio_estoque_critico.csv' criado com sucesso!")