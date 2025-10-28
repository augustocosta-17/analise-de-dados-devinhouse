import pandas as pd

df_produtos = pd.read_csv("produtos.csv")

estoque_baixo = df_produtos[df_produtos['estoque'] < 20]

print("\n=== PRODUTOS COM ESTOQUE ABAIXO DE 20 ===")
print(estoque_baixo)

estoque_baixo.to_csv("estoque_baixo.csv", index=False)
print("\n✅ Arquivo 'estoque_baixo.csv' criado com sucesso!")
