"""
Módulo de Transformação de Dados
Responsável por limpar, transformar e enriquecer os dados
"""

import pandas as pd
import numpy as np
import re

def limpar_alunos_csv(df: pd.DataFrame) -> pd.DataFrame:
   df_clean = df.copy()

   # Tratamento da coluna 'id_aluno'
   df_clean['id_aluno'] = pd.to_numeric(df_clean['id_aluno'], errors='coerce')

   # Tratamento da coluna 'nome'
   def limpar_nome(nome):
      if pd.isnull(nome) or nome.strip() == '' :
         return np.nan
      
      nome = nome.strip()
      nome = re.sub(r'\s+', ' ', nome)
      nome = nome.title()
      return nome
   
   df_clean['nome'] = df_clean['nome'].apply(limpar_nome)