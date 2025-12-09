# 📂 Semana 11 - Pipeline ETL e Análise de Dados

## 📋 Descrição do Projeto

Estrutura completa de projeto de análise de dados com pipeline ETL (Extract, Transform, Load) modularizado e organizado seguindo as melhores práticas da indústria.

---

## 🏗️ Estrutura do Projeto

```
semana_11/
├── data/
│   ├── raw/                    # Dados brutos (não processados)
│   └── processed/              # Dados processados e limpos
│
├── notebooks/
│   └── analise_dados.ipynb     # Notebook Jupyter principal
│
├── src/
│   ├── __init__.py            # Inicialização do pacote src
│   ├── analysis.py            # Funções de análise exploratória
│   ├── database.py            # Conexão e operações com banco de dados
│   └── etl/
│       ├── __init__.py        # Inicialização do pacote ETL
│       ├── extract.py         # Extração de dados
│       ├── transform.py       # Transformação e limpeza
│       └── load.py            # Carregamento e salvamento
│
├── venv/                       # Ambiente virtual Python
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

---

## 🛠️ Tecnologias Utilizadas

```python
pandas       # Manipulação de dados
numpy        # Computação numérica
matplotlib   # Visualizações
seaborn      # Gráficos estatísticos
openpyxl     # Leitura/escrita Excel
jupyter      # Ambiente interativo
ipykernel    # Kernel Jupyter
pyarrow      # Formato Parquet
```

---

## 📦 Módulos Desenvolvidos

### 🔹 ETL Package (`src/etl/`)

#### **extract.py** - Extração de Dados
Funções para extrair dados de diferentes fontes:
- `extract_csv()` - Extrai dados de arquivos CSV
- `extract_excel()` - Extrai dados de arquivos Excel
- `extract_multiple_csv()` - Extrai múltiplos CSVs de um diretório

#### **transform.py** - Transformação de Dados
Funções para limpar e transformar dados:
- `remove_duplicates()` - Remove duplicatas
- `handle_missing_values()` - Trata valores ausentes
- `remove_outliers_iqr()` - Remove outliers usando método IQR
- `normalize_column()` - Normaliza colunas numéricas
- `convert_data_types()` - Converte tipos de dados

#### **load.py** - Carregamento de Dados
Funções para salvar dados processados:
- `save_to_csv()` - Salva em formato CSV
- `save_to_excel()` - Salva em formato Excel
- `save_to_parquet()` - Salva em formato Parquet (otimizado)
- `append_to_csv()` - Adiciona dados a CSV existente
- `load_processed_data()` - Carrega dados processados

### 🔹 Analysis Module (`src/analysis.py`)

Funções para análise exploratória:
- `get_summary_statistics()` - Estatísticas descritivas
- `check_data_quality()` - Relatório de qualidade dos dados
- `analyze_correlations()` - Análise de correlações
- `group_analysis()` - Análise agrupada
- `detect_outliers_summary()` - Detecção de outliers
- `value_counts_analysis()` - Análise de distribuição de valores

### 🔹 Database Module (`src/database.py`)

Classe e funções para banco de dados SQLite:
- `DatabaseConnection` - Classe para gerenciar conexões
  - `connect()` - Estabelece conexão
  - `disconnect()` - Fecha conexão
  - `execute_query()` - Executa queries SELECT
  - `insert_dataframe()` - Insere DataFrame em tabela
  - `create_table_from_dataframe()` - Cria tabela a partir de DataFrame
  - `list_tables()` - Lista tabelas do banco
  - `get_table_info()` - Informações da estrutura da tabela
- `quick_query()` - Função auxiliar para queries rápidas

---

## 🚀 Como Usar

### 1. Configurar Ambiente Virtual

```powershell
# Navegar até a pasta do projeto
cd "e:\analise-de-dados-devinhouse\modulo_01_programacao_e_modelagem_de_dados\semana_11"

# Ativar ambiente virtual (no Windows)
.\venv\Scripts\python.exe

# Ou ativar o ambiente (se configurado)
.\venv\Scripts\Activate.ps1
```

### 2. Instalar Dependências

```powershell
# Usando o python do venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 3. Usar o Notebook Jupyter

```powershell
# Iniciar Jupyter
.\venv\Scripts\jupyter notebook

# Ou abrir diretamente no VS Code
code notebooks/analise_dados.ipynb
```

---

## 💡 Exemplos de Uso

### Extração de Dados

```python
from etl.extract import extract_csv, extract_excel

# Extrair CSV
df = extract_csv('../data/raw/dados.csv')

# Extrair Excel
df = extract_excel('../data/raw/dados.xlsx', sheet_name='Planilha1')
```

### Transformação de Dados

```python
from etl.transform import remove_duplicates, handle_missing_values, remove_outliers_iqr

# Remover duplicatas
df_clean = remove_duplicates(df, subset=['nome', 'data'])

# Tratar valores ausentes
df_clean = handle_missing_values(df_clean, strategy='drop')

# Remover outliers
df_clean = remove_outliers_iqr(df_clean, columns=['idade', 'valor'])
```

### Carregamento de Dados

```python
from etl.load import save_to_csv, save_to_parquet

# Salvar em CSV
save_to_csv(df_clean, '../data/processed/dados_limpos.csv')

# Salvar em Parquet (formato otimizado)
save_to_parquet(df_clean, '../data/processed/dados_limpos.parquet')
```

### Análise de Dados

```python
from analysis import check_data_quality, analyze_correlations

# Verificar qualidade dos dados
quality_report = check_data_quality(df_clean)

# Analisar correlações
correlation_matrix = analyze_correlations(df_clean, threshold=0.5)
```

### Trabalhar com Banco de Dados

```python
from database import DatabaseConnection

# Criar conexão
db = DatabaseConnection('../data/processed/database.db')
db.connect()

# Inserir dados
db.insert_dataframe(df_clean, 'tabela_principal', if_exists='replace')

# Executar query
resultado = db.execute_query('SELECT * FROM tabela_principal WHERE idade > 30')

# Fechar conexão
db.disconnect()
```

---

## 📊 Workflow Recomendado

1. **Extract** - Coloque dados brutos em `data/raw/`
2. **Transform** - Use funções de `transform.py` para limpar
3. **Load** - Salve dados processados em `data/processed/`
4. **Analyze** - Use `analysis.py` para exploração
5. **Visualize** - Crie gráficos no Jupyter Notebook
6. **Database** (opcional) - Persista dados em SQLite

---

## 🎯 Boas Práticas Implementadas

✅ **Modularização** - Código organizado em módulos reutilizáveis  
✅ **Separação de Dados** - raw/ e processed/ claramente separados  
✅ **Documentação** - Docstrings em todas as funções  
✅ **Type Hints** - Tipos especificados para melhor legibilidade  
✅ **Tratamento de Erros** - Try/except com mensagens claras  
✅ **Ambiente Virtual** - Isolamento de dependências  
✅ **Requirements.txt** - Dependências versionadas  
✅ **Feedback Visual** - Emojis e prints informativos  

---

## 📚 Recursos Adicionais

### Formatos de Dados Suportados:
- **CSV** - Arquivos de texto separados por vírgula
- **Excel** - Planilhas .xlsx e .xls
- **Parquet** - Formato colunar otimizado
- **SQLite** - Banco de dados relacional

### Métodos de Limpeza:
- **Duplicatas** - Remoção inteligente
- **Valores Ausentes** - Drop, fill, mean, median
- **Outliers** - Método IQR (Interquartile Range)
- **Normalização** - Min-Max Scaling e Z-Score

---

## 👨‍💻 Autor

**Augusto Costa**  
Estudante de Análise de Dados - DevInHouse V4

📧 Email: augustoccostamg@gmail.com  
💼 LinkedIn: [Augusto César da Costa](https://www.linkedin.com/in/augusto-c%C3%A9sar-da-costa-768516218)  
🐙 GitHub: [@augustocosta-17](https://github.com/augustocosta-17)

---

## 📝 Notas

- Este projeto foi desenvolvido como parte do curso DevInHouse V4
- A estrutura segue padrões da indústria para projetos de Data Science
- Todos os módulos são independentes e podem ser usados separadamente
- O código é totalmente documentado e pronto para produção

---

[⬅️ Voltar ao Módulo 01](../README.md)
