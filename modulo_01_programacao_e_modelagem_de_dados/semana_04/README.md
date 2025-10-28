# 📂 Semana 04 - Funções e Manipulação de Arquivos

## 🎯 Tema da Semana
Modularização de código através de funções e módulos, manipulação de arquivos CSV e JSON, e organização de projetos Python.

## 📋 Lista de Exercícios

### Aulas Práticas

#### **M1S04_Aula1** - Calculadora Modular
- `calculadora.py` - Módulo com funções de cálculo
- `main.py` - Programa principal
- **Conceitos:** Funções, modularização, importação de módulos

#### **M1S04_Aula2** - Sistema de Relatórios
- `calculos.py` - Módulo de cálculos
- `relatorio.py` - Módulo de geração de relatórios
- `main.py` - Programa principal integrado

##### **Manipulação de Arquivos** - `Manip_Arquivos/`
- `vendas.csv` - Dados de entrada
- `relatorio.csv` - Relatório gerado
- `main.py` - Processamento de dados CSV
- **Conceitos:** Leitura/escrita de CSV, processamento de dados

#### **M1S04_Aula3** - Trabalhando com JSON
- `produtos.json` - Arquivo de dados JSON
- `main.py` - Manipulação de dados JSON
- **Conceitos:** JSON, serialização, deserialização

### Exercícios Trello

#### **1. Funções, Parâmetros e Retorno** - `Trello/funcoes_parametros_e_retorno/`
- `main.py`
- **Conceitos:** Definição de funções, parâmetros, valores de retorno, escopo

#### **2. Leitura e Escrita CSV** - `Trello/leitura_e_escrita_csv/`
- `vendas.csv` - Dados originais
- `vendas_com_total.csv` - Dados processados
- `main.py` - Processamento de vendas
- **Conceitos:** Biblioteca CSV, leitura, escrita, transformação de dados

#### **3. Limpeza de Dados** - `Trello/limpeza_de_dados/`
- `main.py` - Script de limpeza
- `validos.csv` - Dados validados
- `invalidos.csv` - Dados rejeitados
- **Conceitos:** Validação de dados, separação de dados válidos/inválidos

#### **4. Modularização e Importação** - `Trello/modularizacao_e_importacao/`
- `funcoes_calculo.py` - Módulo de cálculos
- `funcoes_data.py` - Módulo de datas
- `main.py` - Programa principal
- **Conceitos:** Organização de código, múltiplos módulos, imports

#### **5. Trabalhando com Datas** - `Trello/trabalhando_com_datas/`
- `datas.py` - Manipulação de datas
- **Conceitos:** Biblioteca datetime, formatação, cálculos com datas

## 💡 O Que Foi Aprendido

### Funções
- ✅ Definição de funções com `def`
- ✅ Parâmetros e argumentos (posicionais, nomeados, padrão)
- ✅ Valores de retorno (`return`)
- ✅ Escopo de variáveis (local vs global)
- ✅ Docstrings e documentação
- ✅ Funções como objetos de primeira classe

### Modularização
- ✅ Criação de módulos próprios
- ✅ Importação: `import`, `from...import`, `as`
- ✅ Estrutura de projetos Python
- ✅ `__pycache__` e compilação de módulos
- ✅ Separação de responsabilidades

### Manipulação de Arquivos CSV
- ✅ Biblioteca `csv` do Python
- ✅ Leitura com `csv.reader()` e `csv.DictReader()`
- ✅ Escrita com `csv.writer()` e `csv.DictWriter()`
- ✅ Processamento linha a linha
- ✅ Transformação e enriquecimento de dados

### Manipulação de JSON
- ✅ Biblioteca `json` do Python
- ✅ Serialização: `json.dump()` e `json.dumps()`
- ✅ Deserialização: `json.load()` e `json.loads()`
- ✅ Trabalhar com dados estruturados complexos

### Manipulação de Datas
- ✅ Biblioteca `datetime`
- ✅ Objetos: `date`, `time`, `datetime`
- ✅ Formatação com `strftime()`
- ✅ Parsing com `strptime()`
- ✅ Cálculos e diferenças entre datas

### Qualidade de Dados
- ✅ Validação de dados de entrada
- ✅ Tratamento de erros com try/except
- ✅ Limpeza e normalização
- ✅ Separação de dados válidos e inválidos

## 🛠️ Tecnologias Utilizadas
- Python 3.x
- Biblioteca `csv`
- Biblioteca `json`
- Biblioteca `datetime`
- Módulos personalizados

## 🎯 Habilidades Desenvolvidas
- Escrever código modular e reutilizável
- Organizar projetos Python de forma profissional
- Processar arquivos de dados em diferentes formatos
- Validar e limpar dados
- Trabalhar com datas e timestamps
- Gerar relatórios automatizados

## 🚀 Aplicações Práticas
- Sistemas de processamento de vendas
- Geração de relatórios automáticos
- ETL básico (Extract, Transform, Load)
- Validação e limpeza de datasets

---

[⬅️ Voltar ao Módulo 01](../README.md)
