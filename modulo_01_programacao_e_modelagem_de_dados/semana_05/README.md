# 📂 Semana 05 - Integração e Análise de Dados

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completo-success?style=flat-square)

</div>

---

## 🎯 Tema da Semana
Integração de múltiplos arquivos de dados, análise avançada com cruzamento de informações, introdução ao **Pandas** e **NumPy**, e aplicação prática de todos os conceitos aprendidos.

---

## 📋 Projetos e Exercícios

### **Aulas Práticas**

#### 📝 **Aula 1** - Introdução

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`aula_um/`](./aula_um/)

Conceitos iniciais de integração de dados e preparação para análises complexas.

</details>

---

#### 📦 **Aula 2** - Análise de Estoque

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`aula_dois/`](./aula_dois/)

**Arquivos:**
- `produtos.csv` - Base de dados de produtos
- `estoque_baixo.csv` - Relatório gerado
- `main.py` - Sistema de análise de estoque

**Conceitos:**
- ✅ Leitura de CSV com Python puro
- ✅ Filtragem de dados
- ✅ Geração de alertas de estoque
- ✅ Criação de relatórios automatizados

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd aula_dois
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots do relatório gerado!

</details>

---

#### 🔗 **Aula 3** - Análise Integrada Completa

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`aula_tres/`](./aula_tres/)

**Arquivos:**
- `produtos.csv` - Cadastro de produtos
- `categorias.csv` - Categorias de produtos
- `vendas.csv` - Histórico de vendas
- `relatorio_estoque_critico.csv` - Relatório final
- `main.py` - Sistema integrado de análise

**Conceitos:**
- ✅ Junção de múltiplos arquivos CSV
- ✅ Análise cruzada de dados
- ✅ Relacionamento entre tabelas
- ✅ Geração de relatórios complexos

**🏆 Destaque:** Análise completa integrando 3 fontes de dados!

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd aula_tres
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots dos insights gerados!

</details>

---

### **🎯 Projeto Trello - Análise Completa com Pandas**

#### 📓 **DevInHouse Semana 5 Notebook** - **Introdução ao Pandas e NumPy**

<details>
<summary><b>📖 Descrição Completa</b></summary>

**Pasta:** [`Trello/devinhouse-semana5-notebook/`](./Trello/devinhouse-semana5-notebook/)

**Arquivos:**
- `devinhouse-semana5.ipynb` - **Jupyter Notebook** com análise completa
- `clientes.csv` - Base de clientes
- `pedidos.csv` - Base de pedidos  
- `produtos.csv` - Base de produtos

**🌟 Marcos Importantes:**
- **Primeira vez usando Pandas** - A biblioteca profissional para análise de dados
- **Primeira vez usando NumPy** - Computação numérica eficiente
- **Primeiro Jupyter Notebook** - Ambiente interativo de análise

**Análises Realizadas:**
- 👥 Análise de clientes e distribuição geográfica
- 🛍️ Análise de pedidos e padrões de compra
- 📦 Análise de produtos e estoque
- 🔗 Relacionamento cliente-pedido-produto
- 📊 Insights de negócio acionáveis

**Conceitos Aplicados:**
- ✅ `pd.read_csv()` - Leitura de dados
- ✅ `df.head()`, `df.info()`, `df.describe()` - Exploração inicial
- ✅ `df.isnull()` - Verificação de dados nulos
- ✅ `df.groupby()` - Agrupamento de dados
- ✅ `pd.merge()` - Junção de DataFrames
- ✅ Filtros e seleções com Pandas
- ✅ Operações com NumPy arrays

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd Trello/devinhouse-semana5-notebook
jupyter notebook devinhouse-semana5.ipynb
```

Ou abra diretamente no VS Code com a extensão Jupyter instalada.

> 💡 **Dica:** Adicione aqui screenshots das análises e gráficos gerados!

</details>

---

## 💡 Conhecimentos Adquiridos

### **🐼 Introdução ao Pandas**

<table>
<tr>
<td width="50%">

**📊 Fundamentos**
- ✅ `pd.read_csv()` - Leitura de arquivos
- ✅ `df.head()` - Primeiras linhas
- ✅ `df.info()` - Informações do DataFrame
- ✅ `df.describe()` - Estatísticas descritivas
- ✅ `df.isnull()` - Verificação de nulos
- ✅ `df.shape` - Dimensões dos dados

</td>
<td width="50%">

**🔍 Operações Avançadas**
- ✅ `df.groupby()` - Agrupamento
- ✅ `pd.merge()` - Junção de DataFrames
- ✅ `df.pivot_table()` - Tabelas dinâmicas
- ✅ Filtros e seleções
- ✅ `df.iloc[]` - Indexação por posição
- ✅ Agregações (sum, mean, count)

</td>
</tr>
</table>

### **🔢 Introdução ao NumPy**

```python
import numpy as np

# Criação de arrays
arr = np.array([1, 2, 3, 4, 5])

# Operações matemáticas
media = arr.mean()
soma = arr.sum()
desvio = arr.std()

# Broadcasting - operações vetorizadas
resultado = arr * 2  # Multiplica todos os elementos
```

**Conceitos:**
- ✅ Arrays NumPy e suas operações
- ✅ Operações matemáticas eficientes
- ✅ Broadcasting (operações vetorizadas)
- ✅ Propriedades: `dtype`, `shape`
- ✅ Funções: `mean()`, `sum()`, `std()`, `max()`, `min()`

### **📓 Jupyter Notebooks**
- ✅ Ambiente interativo para análise
- ✅ Execução célula por célula
- ✅ Markdown para documentação
- ✅ Visualização inline de resultados

### **🔗 Integração de Dados (Python Puro)**
- ✅ Leitura de múltiplos arquivos CSV
- ✅ Relacionamento entre datasets
- ✅ Junção de dados usando dicionários
- ✅ Cruzamento de informações

### **📊 Análise de Negócio**
- ✅ Gestão de estoque e alertas críticos
- ✅ Análise de categorias de produtos
- ✅ Relacionamento cliente-pedido-produto
- ✅ Métricas de negócio (vendas, estoque)
- ✅ Geração de insights acionáveis

---

## 🛠️ Tecnologias e Bibliotecas

![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**Stack completa:**
- Python 3.x (base)
- Pandas (manipulação de dados)
- NumPy (computação numérica)
- Jupyter Notebook (ambiente interativo)
- CSV (manipulação com Python puro)

---

## 📊 Estatísticas da Semana

| Métrica | Valor |
|---------|-------|
| 📝 **Exercícios** | 4 |
| 📓 **Notebooks** | 1 (Jupyter) |
| 📂 **Arquivos CSV** | 7 |
| ⏱️ **Horas de Estudo** | ~15h |
| 💻 **Linhas de Código** | ~400 |
| 🎯 **Conceitos Aprendidos** | 30+ |
| 🆕 **Novas Bibliotecas** | 2 (Pandas, NumPy) |

---

## 🎯 Desafios & Aprendizados

<details>
<summary><b>� Desafios Encontrados</b></summary>

- Primeira experiência com Pandas - nova sintaxe e paradigma
- Entender DataFrames vs estruturas Python nativas
- Realizar junções (merge) entre múltiplos datasets
- Navegar pela documentação extensa do Pandas
- Integrar dados de múltiplas fontes CSV

</details>

<details>
<summary><b>🌟 Principais Aprendizados</b></summary>

- **Pandas é extremamente poderoso** - O que levaria muitas linhas em Python puro, Pandas resolve em uma
- **NumPy é a base** - Pandas usa NumPy internamente para performance
- **Jupyter Notebooks são ideais para análise** - Permite experimentação e documentação juntas
- **Análise de dados é iterativa** - Explorar, limpar, analisar, repetir
- **Pensar em termos de DataFrames** - Mudança de paradigma para análise eficiente

</details>

---

## 🚀 Aplicações Práticas

- ✅ Sistema de gestão de estoque com alertas
- ✅ Análise de vendas e comportamento de clientes
- ✅ Relatórios gerenciais automatizados
- ✅ Dashboard de dados (versão texto)
- ✅ Integração de múltiplas fontes de dados

---

## 🎓 Marco Importante

<div align="center">

### **🎉 Transição para Ferramentas Profissionais**

Esta semana marca um **momento fundamental** no aprendizado:

**Antes (Semanas 1-4):**
```
Python Puro → Estruturas básicas → Funções → Arquivos
```

**Agora (Semana 5+):**
```
Pandas + NumPy + Jupyter → Análise de Dados Profissional
```

</div>

**Por que isso importa:**
- 🐼 **Pandas** é a ferramenta #1 em análise de dados Python
- 🔢 **NumPy** é usado em ML, IA, Ciência de Dados
- 📓 **Jupyter** é padrão da indústria para análise exploratória
- 📊 Base sólida para **Power BI, SQL, Machine Learning**

---

## 🎓 Próximos Passos

Nas **próximas semanas**, continuaremos aprofundando:
- 📊 **Pandas avançado** - Operações complexas, pivot tables, merge
- 📈 **Visualização de dados** - Matplotlib, Seaborn
- 🧮 **Análises estatísticas** - Correlações, distribuições
- 🗄️ **SQL** - Consultas em bancos de dados
- 📊 **Power BI** - Dashboards interativos

---

## 📚 Recursos Adicionais

- 📖 [Pandas Documentation](https://pandas.pydata.org/docs/)
- 📖 [NumPy Documentation](https://numpy.org/doc/)
- 📖 [Jupyter Notebook Guide](https://jupyter.org/documentation)
- 🎥 [Pandas Tutorial - YouTube](https://www.youtube.com/results?search_query=pandas+tutorial)
- 📝 [Kaggle Learn - Pandas](https://www.kaggle.com/learn/pandas)

---

<div align="center">

[⬅️ Semana Anterior](../semana_04/README.md) | [Voltar ao Módulo 01](../README.md)

**🎉 Parabéns por completar a introdução ao Pandas e NumPy! 🎉**

</div>
