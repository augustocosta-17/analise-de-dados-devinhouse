# 📂 Semana 06 - Pandas e Tratamento de Dados

## 📝 Resumo da Semana
Nesta semana aprofundei o conhecimento em Pandas, focando em leitura de dados, identificação e tratamento de valores ausentes (NaN), e técnicas de limpeza de dados para análise.

## 🎯 Objetivos de Aprendizado
- Ler e carregar dados de arquivos CSV com Pandas
- Identificar valores nulos em DataFrames
- Aplicar técnicas de tratamento de dados ausentes
- Usar `fillna()` para preencher valores nulos
- Converter tipos de dados com `pd.to_numeric()`
- Trabalhar com estratégias de imputação (média, valores fixos)

## 💻 Tecnologias Utilizadas
- **Python 3.14.0**
- **Pandas 2.3.3** - Manipulação e análise de dados
- **NumPy 2.3.4** - Computação numérica
- **CSV** - Arquivos de dados estruturados

## 📁 Estrutura da Semana
```
semana_06/
├── aula_um/
│   ├── main.py          # Tratamento de dados CSV
│   ├── clientes.csv     # Dataset de clientes
│   └── vendas.csv       # Dataset de vendas
├── aula_dois/
│   ├── main.py          # Análise de dados Excel
│   └── dataset_clamed.xlsx  # Dataset de produtos
├── venv/                # Ambiente virtual Python
└── README.md
```

## 🚀 Conceitos Aplicados

### Aula 01 - Tratamento Completo de Dados CSV
**Arquivos:** `aula_um/main.py`, `clientes.csv`, `vendas.csv`

#### Técnicas Implementadas:

**1. Leitura e Configuração**
```python
df_clientes = pd.read_csv('clientes.csv')
df_vendas = pd.read_csv('vendas.csv')
```

**2. Tratamento de Valores Nulos**
- Nome: `fillna('Não informado')`
- Email: `fillna('nao_informado@email.com')`
- Idade: Conversão numérica + preenchimento com média arredondada

**3. Conversão de Tipos**
```python
pd.to_numeric(df['idade'], errors='coerce')  # Idade
pd.to_datetime(df['data'], format='mixed')   # Datas com múltiplos formatos
```

**4. Limpeza de Dados**
- Remoção de duplicatas: `drop_duplicates(subset=['nome', 'email'])`
- Correção de emails: Regex para adicionar `.com` em emails incompletos

**5. Identificação de Outliers**
- Método IQR (Intervalo Interquartil)
- Cálculo de limites: Q1 - 1.5×IQR e Q3 + 1.5×IQR

**6. Normalização de Dados**
- Min-Max Scaling: `(valor - min) / (max - min)`
- Valores normalizados entre 0 e 1

**7. Ordenação**
```python
df.sort_values('preco_unitario')  # Ordenação crescente
```

---

### Aula 02 - Análise de Dados Excel
**Arquivos:** `aula_dois/main.py`, `dataset_clamed.xlsx`

#### Técnicas Implementadas:

**1. Leitura de Excel**
```python
df = pd.read_excel('dataset_clamed.xlsx')  # Requer openpyxl
```

**2. Análise Exploratória**
```python
df.describe()           # Estatísticas descritivas
df.info()              # Tipos e contagem de dados
df.isnull().sum()      # Contagem de nulos por coluna
df.duplicated().sum()  # Total de duplicatas
```

**3. Identificação de Problemas**
- 9 valores nulos em 3 colunas diferentes
- 20 linhas duplicadas
- Outliers em coluna de preços

**4. Tratamento de Duplicatas**
```python
# Visualizar duplicatas
df[df.duplicated(['id_produto', 'nome_produto'], keep=False)]

# Remover duplicatas
df = df.drop_duplicates(subset=['id_produto', 'nome_produto'])
```

**5. Tratamento de Valores Nulos**
```python
df['preco'].fillna(df['preco'].mean(), inplace=True)           # Média
df['quantidade_estoque'].fillna(0, inplace=True)               # Valor fixo
df['fornecedor'].fillna('Não informado', inplace=True)         # Texto padrão
```

**6. Detecção de Outliers - Método IQR**
```python
q1 = df['preco'].quantile(0.25)
q3 = df['preco'].quantile(0.75)
iqr = q3 - q1
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

# Filtrar outliers
outliers = df[(df['preco'] < limite_inferior) | (df['preco'] > limite_superior)]
```

---

## 📊 Datasets Utilizados

### Aula 01:
- **clientes.csv**: Dados de clientes (id, nome, idade, email, cidade, estado)
- **vendas.csv**: Dados de vendas (id_venda, id_cliente, produto, quantidade, preco_unitario, data_venda)

### Aula 02:
- **dataset_clamed.xlsx**: 150 produtos (id_produto, nome_produto, preco, quantidade_estoque, fornecedor)

## 🔧 Configuração do Ambiente
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install pandas numpy openpyxl
```

## ✅ Habilidades Desenvolvidas

### Manipulação de Dados:
✅ Leitura de arquivos CSV e Excel (xlsx)  
✅ Conversão de tipos de dados (numéricos, datas)  
✅ Tratamento de datas em múltiplos formatos  
✅ Remoção de duplicatas  
✅ Ordenação de dados  

### Limpeza de Dados:
✅ Identificação de valores nulos  
✅ Estratégias de imputação (média, mediana, valores fixos)  
✅ Correção de dados inconsistentes (regex)  
✅ Tratamento de outliers (método IQR)  

### Análise Exploratória:
✅ Estatísticas descritivas (describe, info)  
✅ Identificação de duplicatas  
✅ Detecção de outliers  
✅ Normalização de dados (Min-Max Scaling)  

### Bibliotecas:
✅ Pandas para manipulação de DataFrames  
✅ NumPy para operações numéricas  
✅ OpenPyXL para leitura de Excel  
✅ Regex para limpeza de strings  

---

[⬅️ Voltar ao Módulo 01](../README.md)
