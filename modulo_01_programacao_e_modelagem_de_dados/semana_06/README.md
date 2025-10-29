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
│   ├── main.py          # Script principal com tratamento de dados
│   ├── clientes.csv     # Dataset de clientes
│   └── vendas.csv       # Dataset de vendas
├── venv/                # Ambiente virtual Python
└── README.md
```

## 🚀 Conceitos Aplicados

### Aula 01 - Leitura e Tratamento de Dados
**Arquivos:** `aula_um/main.py`

#### Técnicas Implementadas:
1. **Leitura de Dados CSV**
   ```python
   df_clientes = pd.read_csv('clientes.csv')
   df_vendas = pd.read_csv('vendas.csv')
   ```

2. **Identificação de Valores Nulos**
   ```python
   df.isnull().sum()  # Conta nulos por coluna
   ```

3. **Preenchimento de Valores Ausentes**
   - Texto fixo: `fillna('Não informado')`
   - Email padrão: `fillna('nao_informado@email.com')`
   - Média arredondada: `fillna(df['idade'].mean().round())`

4. **Conversão de Tipos**
   ```python
   pd.to_numeric(df['idade'], errors='coerce')
   ```

## 📊 Datasets Utilizados
- **clientes.csv**: Dados de clientes (id, nome, idade, email, cidade, estado)
- **vendas.csv**: Dados de vendas

## 🔧 Configuração do Ambiente
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install pandas numpy
```

## ✅ Habilidades Desenvolvidas
✅ Leitura de arquivos CSV com Pandas  
✅ Análise exploratória de dados  
✅ Identificação de valores nulos  
✅ Tratamento de dados ausentes  
✅ Conversão de tipos de dados  
✅ Estratégias de imputação  
✅ Limpeza e preparação de dados  

---

[⬅️ Voltar ao Módulo 01](../README.md)
