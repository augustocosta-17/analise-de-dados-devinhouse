"""
Módulo de Extração de Dados
Responsável por extrair dados de diferentes fontes (CSV, Excel, APIs, etc.)
"""

import pandas as pd
import os
from typing import Optional


def extract_csv(file_path: str = 'data/raw/alunos.csv', encoding: str = 'utf-8') -> Optional[pd.DataFrame]:
    """
    Extrai dados de um arquivo CSV
    
    Args:
        file_path (str): Caminho do arquivo CSV (padrão: 'data/raw/alunos.csv')
        encoding (str): Codificação do arquivo (padrão 'utf-8')
        
    Returns:
        pd.DataFrame: Dados extraídos ou None em caso de erro
    """
    try:
        if not os.path.exists(file_path):
            print(f"❌ Arquivo não encontrado: {file_path}")
            return None
        
        df = pd.read_csv(file_path, encoding=encoding)
        print(f"✅ Arquivo carregado: {file_path}")
        print(f"📊 Shape: {df.shape[0]} linhas x {df.shape[1]} colunas")
        return df
        
    except Exception as e:
        print(f"❌ Erro ao carregar CSV: {e}")
        return None

