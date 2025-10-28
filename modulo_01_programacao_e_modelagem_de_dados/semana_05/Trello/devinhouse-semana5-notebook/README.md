# 📓 Projeto: Análise de Dados com Pandas e NumPy

## 📝 Descrição do Projeto
Este é o projeto principal da Semana 5, onde aplicamos **Pandas** e **NumPy** para realizar análise de dados profissional. O projeto trabalha com três datasets relacionados (clientes, pedidos e produtos) para extrair insights de negócio.

## 📂 Arquivos do Projeto
- `devinhouse-semana5.ipynb` - Jupyter Notebook com análise completa
- `clientes.csv` - Base de dados de clientes
- `pedidos.csv` - Base de dados de pedidos
- `produtos.csv` - Base de dados de produtos

## 🎯 Objetivos do Projeto
1. Aprender a usar **Pandas** para manipulação de dados
2. Aplicar **NumPy** para análise numérica
3. Realizar análise exploratória de dados (EDA)
4. Integrar múltiplos datasets
5. Extrair insights de negócio

## 📊 Estrutura do Notebook

### 1️⃣ **Leitura e Estruturação dos Dados (Pandas)**
- Importação dos dados CSV
- Exploração inicial com `head()`, `info()`, `describe()`
- Verificação de valores nulos
- Entendimento da estrutura dos dados

**Conceitos Aplicados:**
- `pd.read_csv()` - Leitura de arquivos
- `.head()` - Primeiras linhas
- `.info()` - Informações sobre o DataFrame
- `.describe()` - Estatísticas descritivas
- `.isnull().sum()` - Contagem de valores nulos

### 2️⃣ **Filtros e Seleções**
- Filtrar clientes com idade > 30
- Filtrar pedidos com valor > R$ 500
- Filtrar produtos da categoria "Eletrônicos"
- Acessar linhas específicas com `iloc[]`

**Conceitos Aplicados:**
- Filtragem booleana: `df[df['coluna'] > valor]`
- Comparações e condições
- Indexação posicional com `.iloc[]`

### 3️⃣ **Operações com DataFrames**
- Agrupamento de pedidos por cliente
- Merge (junção) de clientes e pedidos
- Pivot table para médias por categoria
- Detecção de duplicatas

**Conceitos Aplicados:**
- `.groupby()` - Agrupamento de dados
- `pd.merge()` - Junção de DataFrames
- `pd.pivot_table()` - Tabelas dinâmicas
- `.duplicated()` - Detecção de duplicatas

### 4️⃣ **Análise Numérica com NumPy**
- Conversão de colunas Pandas para arrays NumPy
- Cálculo de média, soma e desvio padrão
- Aplicação de desconto (operação vetorizada)
- Análise de propriedades dos arrays

**Conceitos Aplicados:**
- `np.array()` - Criação de arrays
- `np.mean()`, `np.sum()`, `np.std()` - Estatísticas
- Broadcasting - Operações vetorizadas
- `.dtype`, `.shape` - Propriedades

### 5️⃣ **Relatório Final**
- 🏆 Cliente que mais gastou
- 💰 Ticket médio por categoria de produto
- 🏙️ Cidade com maior número de clientes

**Conceitos Aplicados:**
- Integração de múltiplas análises
- `.idxmax()` - Identificar máximo
- Formatação de strings (f-strings)
- Apresentação de insights

## 💡 Insights Extraídos

### 📈 Análises Realizadas
1. **Análise de Clientes**
   - Perfil demográfico (idade)
   - Distribuição geográfica (cidades)
   - Comportamento de compra

2. **Análise de Pedidos**
   - Valores totais e estatísticas
   - Distribuição de gastos
   - Simulação de descontos

3. **Análise de Produtos**
   - Categorias disponíveis
   - Preços médios por categoria
   - Produtos eletrônicos em destaque

4. **Análise Integrada**
   - Relacionamento cliente-pedido
   - Cliente com maior gasto total
   - Padrões de consumo

## 🛠️ Tecnologias e Bibliotecas

### Pandas
```python
import pandas as pd
```
- Manipulação de DataFrames
- Leitura de CSV
- Operações de merge e groupby
- Pivot tables

### NumPy
```python
import numpy as np
```
- Arrays multidimensionais
- Operações matemáticas vetorizadas
- Cálculos estatísticos eficientes

### Google Colab (Opcional)
```python
from google.colab import drive
drive.mount('/content/drive')
```
- Ambiente de desenvolvimento na nuvem
- Integração com Google Drive

## 🚀 Como Executar

### Opção 1: Jupyter Notebook Local
```bash
# Instalar dependências
pip install pandas numpy jupyter

# Iniciar Jupyter
jupyter notebook

# Abrir o arquivo devinhouse-semana5.ipynb
```

### Opção 2: Google Colab
1. Fazer upload do notebook e dos arquivos CSV para o Google Drive
2. Abrir o notebook no Google Colab
3. Ajustar o caminho dos arquivos na célula de leitura

### Opção 3: VS Code
1. Abrir o arquivo `.ipynb` no VS Code
2. Selecionar o kernel Python
3. Executar as células sequencialmente

## 📚 O Que Aprendemos

### Habilidades Técnicas
✅ Usar Pandas para análise de dados  
✅ Manipular DataFrames eficientemente  
✅ Aplicar NumPy para cálculos numéricos  
✅ Realizar merge de datasets  
✅ Criar pivot tables e agrupamentos  
✅ Trabalhar com Jupyter Notebooks  

### Habilidades Analíticas
✅ Realizar análise exploratória de dados (EDA)  
✅ Identificar padrões e insights  
✅ Integrar múltiplas fontes de dados  
✅ Responder perguntas de negócio com dados  
✅ Apresentar resultados de forma clara  

## 🎓 Próximos Passos
Este projeto é a **ponte** entre programação Python básica e análise de dados profissional. Nas próximas semanas do módulo, continuaremos aprofundando:
- Mais práticas com Pandas e NumPy
- Análise de dados mais complexas
- Outros conceitos importantes de programação e análise
- Preparação para os próximos módulos (SQL, Power BI, etc.)

## 📌 Observações
- O notebook foi originalmente desenvolvido para Google Colab
- Os caminhos dos arquivos devem ser ajustados conforme seu ambiente
- Todas as células devem ser executadas em sequência
- Os dados são fictícios para fins educacionais

---

[⬅️ Voltar à Semana 05](../../README.md)
