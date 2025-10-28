import pandas as pd
import numpy as np

dados = {
    'Produto': ['Cadeira', 'Mesa', 'Sofá', 'Cama', 'Estante'],
    'Preço': [150.0, 300.0, 500.0, 400.0, 250.0],
    'Estoque': [20, 15, 10, 5, 8]
}

df = pd.DataFrame(dados)
print(df)