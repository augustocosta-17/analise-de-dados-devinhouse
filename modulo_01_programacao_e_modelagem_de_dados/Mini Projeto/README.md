# 🏥 Mini Projeto - Análise Healthcare Dataset

## 📋 Sobre o Projeto
Primeiro projeto avaliativo do **Módulo 01**, desenvolvido para a empresa fictícia **Clamed Data Insights**, especializada em soluções de análise de dados voltadas para o setor de saúde.

### 🎯 Objetivo
Identificar padrões, anomalias e tendências em dados hospitalares que possam apoiar decisões estratégicas sobre:
- Qualidade de atendimento
- Custos operacionais
- Eficiência hospitalar

---

## 📊 Dataset
**Arquivo:** `healthcare_dataset.csv`

### Características:
- **Registros:** 55.500 linhas (55.000 após limpeza)
- **Colunas:** 15 variáveis
- **Período:** 2019-2024
- **Origem:** Dados de clínicas e hospitais

### Variáveis:
| Coluna | Tipo | Descrição |
|--------|------|-----------|
| Name | object | Nome do paciente |
| Age | int64 | Idade do paciente |
| Gender | object | Gênero (Male/Female) |
| Blood Type | object | Tipo sanguíneo |
| Medical Condition | object | Condição médica diagnosticada |
| Date of Admission | datetime | Data de admissão |
| Doctor | object | Nome do médico responsável |
| Hospital | object | Nome do hospital |
| Insurance Provider | object | Seguradora |
| Billing Amount | float64 | Valor cobrado (USD) |
| Room Number | int64 | Número do quarto |
| Admission Type | object | Tipo de admissão (Elective/Urgent/Emergency) |
| Discharge Date | datetime | Data de alta |
| Medication | object | Medicamento prescrito |
| Test Results | object | Resultado dos testes (Normal/Abnormal/Inconclusive) |

---

## 🛠️ Tecnologias Utilizadas

```python
Python 3.14.0          # Linguagem principal
Pandas 2.3.3          # Manipulação de dados
NumPy 2.3.4           # Computação numérica
Matplotlib 3.10.7     # Visualização
Seaborn 0.13.2        # Gráficos estatísticos
Jupyter 1.1.1         # Ambiente interativo
```

---

## 📁 Estrutura do Projeto

```
Mini Projeto/
├── mini_projeto_clamed.ipynb    # Notebook principal da análise
├── healthcare_dataset.csv       # Dataset original
├── ROTEIRO_MINI_PROJETO.txt     # Guia de procedimentos
├── requirements.txt             # Dependências Python
├── venv/                        # Ambiente virtual isolado
└── README.md                    # Este arquivo
```

---

## 🧹 Processo de Limpeza de Dados

### ✅ Etapa 1: Carregamento e Exploração
- Leitura do CSV com Pandas
- Análise inicial: `shape`, `info()`, `describe()`
- Identificação de problemas

### ✅ Etapa 2: Tratamento de Duplicatas
**Problema:** 534 registros duplicados

**Estratégia:** Remoção inteligente baseada em 3 colunas-chave:
```python
df.drop_duplicates(subset=['Name', 'Date of Admission', 'Test Results'], keep='first')
```

**Justificativa:** 
- Paciente pode ter múltiplas admissões no mesmo dia
- Mas se Nome + Data + Resultado do Teste forem iguais = duplicata verdadeira
- Preserva admissões legítimas, remove apenas duplicatas reais

**Resultado:** 49.995 registros (99,1% preservados)

### ✅ Etapa 3: Conversão de Tipos
```python
# Datas convertidas de object para datetime
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], errors='coerce')
df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], errors='coerce')
```

### ✅ Etapa 4: Padronização
```python
# Nomes padronizados para Title Case
df['Name'] = df['Name'].str.title().str.strip()
```

**Exemplos:**
- `Bobby JacksOn` → `Bobby Jackson`
- `  LesLie TErRy  ` → `Leslie Terry`

### ✅ Etapa 5: Identificação de Outliers
**Método:** IQR (Intervalo Interquartil)

**Colunas analisadas:**
- `Age` - Idades fora do padrão
- `Billing Amount` - Valores de cobrança extremos
- `Room Number` - Quartos inválidos

**Critério:** Valores fora do intervalo `[Q1 - 1.5×IQR, Q3 + 1.5×IQR]`

---

## � Status do Projeto

**Em Desenvolvimento** 🔄

O projeto encontra-se em fase de construção, com a etapa de **Limpeza e Preparação de Dados** concluída. As próximas fases incluirão:
- Feature Engineering
- Análise Exploratória de Dados (EDA)
- Visualizações
- Insights e Conclusões

---

## 🚀 Como Executar

### 1. Configurar Ambiente Virtual
```powershell
# Navegar até a pasta do projeto
cd "D:\analise-de-dados-devinhouse\modulo_01_programacao_e_modelagem_de_dados\Mini Projeto"

# Ativar ambiente virtual
.\venv\Scripts\Activate.ps1

# Se houver erro de execução de scripts, usar:
powershell -ExecutionPolicy Bypass -Command ".\venv\Scripts\Activate.ps1"
```

### 2. Instalar Dependências
```powershell
pip install -r requirements.txt
```

### 3. Abrir Jupyter Notebook
```powershell
jupyter notebook mini_projeto_clamed.ipynb
```

### 4. Executar Análise
- Execute as células sequencialmente (Shift + Enter)
- Acompanhe os outputs de cada etapa
- Ajuste parâmetros conforme necessário

---

## 📚 Recursos de Apoio

### ROTEIRO_MINI_PROJETO.txt
Guia completo e genérico com:
- ✅ 7 fases de análise de dados
- ✅ Comandos Pandas essenciais
- ✅ Estratégias de limpeza de dados
- ✅ Técnicas de visualização
- ✅ Boas práticas de código
- ✅ Cheat sheet de comandos

**Uso:** Consultar durante qualquer análise de dados futura

---

## 🎓 Aprendizados Principais

### Técnicas Aplicadas:
✅ Estratégia inteligente de remoção de duplicatas  
✅ Conversão de tipos de dados (datetime)  
✅ Padronização de strings (title case, strip)  
✅ Método IQR para detecção de outliers  
✅ Análise exploratória de dados  
✅ Documentação de decisões técnicas  

### Habilidades Desenvolvidas:
✅ Pensamento crítico na análise de dados  
✅ Tomada de decisões baseadas em contexto  
✅ Documentação clara de processos  
✅ Uso de ambientes virtuais isolados  
✅ Trabalho com Jupyter Notebooks  
✅ Manipulação avançada de DataFrames  

---

## 👨‍💻 Autor

**Augusto Costa**  
Estudante de Análise de Dados - DevInHouse V4

📧 Email: augustoccostamg@gmail.com  
💼 LinkedIn: [Augusto César da Costa](https://www.linkedin.com/in/augusto-c%C3%A9sar-da-costa-768516218)  
🐙 GitHub: [@augustocosta-17](https://github.com/augustocosta-17)

---

## 📅 Histórico

- **31/10/2025** - Conclusão da Fase 3 (Limpeza e Preparação)
- **31/10/2025** - Início do projeto
- **31/10/2025** - Criação do ambiente virtual e estrutura

---

[⬅️ Voltar ao Módulo 01](../README.md)
