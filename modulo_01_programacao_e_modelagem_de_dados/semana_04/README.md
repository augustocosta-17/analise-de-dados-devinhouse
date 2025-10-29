# 📂 Semana 04 - Funções e Manipulação de Arquivos

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CSV](https://img.shields.io/badge/CSV-File-green?style=flat-square)
![JSON](https://img.shields.io/badge/JSON-File-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completo-success?style=flat-square)

</div>

---

## 🎯 Tema da Semana
Modularização de código através de funções e módulos, manipulação de arquivos CSV e JSON, e organização de projetos Python.

---

## 📋 Projetos e Exercícios

### **Aulas Práticas**

#### 🧮 **M1S04_Aula1** - Calculadora Modular

<details>
<summary><b>Ver detalhes</b></summary>

**Arquivos:**
- [`calculadora.py`](./M1S04_Aula1/calculadora.py) - Módulo com funções de cálculo
- [`main.py`](./M1S04_Aula1/main.py) - Programa principal

**Conceitos:** Funções, modularização, importação de módulos

</details>

---

#### 📊 **M1S04_Aula2** - Sistema de Relatórios

<details>
<summary><b>Ver detalhes</b></summary>

**Arquivos:**
- [`calculos.py`](./M1S04_Aula2/calculos.py) - Módulo de cálculos
- [`relatorio.py`](./M1S04_Aula2/relatorio.py) - Módulo de geração de relatórios
- [`main.py`](./M1S04_Aula2/main.py) - Programa principal integrado

**Subprojeto: Manipulação de Arquivos**
- [`Manip_Arquivos/main.py`](./M1S04_Aula2/Manip_Arquivos/main.py)
- `vendas.csv` → `relatorio.csv`
- **Conceitos:** Leitura/escrita de CSV, processamento de dados

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd M1S04_Aula2
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots da execução!

</details>

---

#### 📄 **M1S04_Aula3** - Trabalhando com JSON

<details>
<summary><b>Ver detalhes</b></summary>

**Arquivos:**
- [`produtos.json`](./M1S04_Aula3/produtos.json) - Arquivo de dados JSON
- [`main.py`](./M1S04_Aula3/main.py) - Manipulação de dados JSON

**Conceitos:** JSON, serialização, deserialização

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd M1S04_Aula3
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots da execução!

</details>

---

### **Exercícios Trello**

#### 1. ⚙️ **Funções, Parâmetros e Retorno**

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`Trello/funcoes_parametros_e_retorno/`](./Trello/funcoes_parametros_e_retorno/)

**Conceitos:**
- ✅ Definição de funções com `def`
- ✅ Parâmetros posicionais e nomeados
- ✅ Valores de retorno
- ✅ Escopo de variáveis

</details>

---

#### 2. 📁 **Leitura e Escrita CSV**

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`Trello/leitura_e_escrita_csv/`](./Trello/leitura_e_escrita_csv/)

**Arquivos:**
- `vendas.csv` → `vendas_com_total.csv`
- `main.py` - Processamento de vendas

**Conceitos:**
- ✅ Biblioteca `csv`
- ✅ Leitura com `csv.reader()`
- ✅ Escrita com `csv.writer()`
- ✅ Transformação de dados

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd Trello/leitura_e_escrita_csv
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots da execução!

</details>

---

#### 3. 🧹 **Limpeza de Dados**

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`Trello/limpeza_de_dados/`](./Trello/limpeza_de_dados/)

**Arquivos:**
- `main.py` - Script de limpeza
- Saídas: `validos.csv`, `invalidos.csv`

**Conceitos:**
- ✅ Validação de dados
- ✅ Separação válidos/inválidos
- ✅ Tratamento de erros
- ✅ Pipeline de limpeza

**🏆 Destaque:** Projeto importante para qualidade de dados

</details>

<details>
<summary><b>📸 Screenshots & Execução</b></summary>

```bash
cd Trello/limpeza_de_dados
python main.py
```

> 💡 **Dica:** Adicione aqui screenshots dos arquivos gerados!

</details>

---

#### 4. 📦 **Modularização e Importação**

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`Trello/modularizacao_e_importacao/`](./Trello/modularizacao_e_importacao/)

**Arquivos:**
- `funcoes_calculo.py` - Módulo de cálculos
- `funcoes_data.py` - Módulo de datas
- `main.py` - Programa principal

**Conceitos:**
- ✅ Organização de código
- ✅ Múltiplos módulos
- ✅ `import` e `from...import`
- ✅ Separação de responsabilidades

</details>

---

#### 5. 📅 **Trabalhando com Datas**

<details>
<summary><b>Ver detalhes</b></summary>

**Pasta:** [`Trello/trabalhando_com_datas/`](./Trello/trabalhando_com_datas/)

**Arquivo:** `datas.py`

**Conceitos:**
- ✅ Biblioteca `datetime`
- ✅ Formatação com `strftime()`
- ✅ Parsing com `strptime()`
- ✅ Cálculos com datas

</details>

---

## 💡 Conhecimentos Adquiridos

### **Funções e Modularização**

<table>
<tr>
<td width="50%">

**🔧 Funções**
- ✅ Definição com `def`
- ✅ Parâmetros (posicionais, nomeados, padrão)
- ✅ Valores de retorno (`return`)
- ✅ Escopo de variáveis
- ✅ Docstrings

</td>
<td width="50%">

**📦 Módulos**
- ✅ Criação de módulos próprios
- ✅ `import`, `from...import`, `as`
- ✅ Estrutura de projetos
- ✅ `__pycache__`
- ✅ Separação de responsabilidades

</td>
</tr>
</table>

### **Manipulação de Arquivos**

```python
# CSV - Leitura
import csv
with open('dados.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# CSV - Escrita
with open('saida.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['nome', 'valor'])
    writer.writeheader()
    writer.writerow({'nome': 'Item', 'valor': 100})

# JSON
import json
with open('dados.json', 'r') as file:
    data = json.load(file)

# Datas
from datetime import datetime
hoje = datetime.now()
formatado = hoje.strftime('%d/%m/%Y')
```

### **Qualidade de Dados**
- ✅ Validação de entrada
- ✅ Tratamento de erros (`try/except`)
- ✅ Limpeza e normalização
- ✅ Separação válidos/inválidos

---

## 🛠️ Tecnologias e Bibliotecas

![Python](https://img.shields.io/badge/Python_3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)

**Bibliotecas utilizadas:**
- `csv` - Manipulação de arquivos CSV
- `json` - Serialização/deserialização JSON
- `datetime` - Manipulação de datas e horários
- Módulos personalizados

---

## 📊 Estatísticas da Semana

| Métrica | Valor |
|---------|-------|
| 📝 **Exercícios** | 8 |
| 📂 **Arquivos Criados** | 15+ |
| ⏱️ **Horas de Estudo** | ~12h |
| 💻 **Linhas de Código** | ~500 |
| 🎯 **Conceitos Aprendidos** | 25+ |

---

## 🎯 Desafios & Aprendizados

<details>
<summary><b>💪 Desafios Encontrados</b></summary>

- Organizar código em múltiplos módulos de forma eficiente
- Trabalhar com diferentes formatos de arquivo (CSV, JSON)
- Implementar validação robusta de dados
- Entender manipulação de datas e fusos horários
- Gerenciar abertura e fechamento de arquivos

</details>

<details>
<summary><b>🌟 Principais Aprendizados</b></summary>

- A importância da modularização para código limpo e reutilizável
- Context managers (`with`) garantem fechamento seguro de arquivos
- Validação de dados é essencial em qualquer pipeline de processamento
- CSV e JSON são formatos fundamentais em análise de dados
- Funções bem documentadas facilitam manutenção e colaboração

</details>

---

## 🚀 Aplicações Práticas

- ✅ Sistemas de processamento de vendas
- ✅ Geração de relatórios automatizados
- ✅ ETL básico (Extract, Transform, Load)
- ✅ Validação e limpeza de datasets
- ✅ Integração entre diferentes fontes de dados

---

## 🎓 Próximos Passos

Na **Semana 05**, avançaremos para:
- 🐼 Introdução ao **Pandas**
- 🔢 Introdução ao **NumPy**
- 📓 **Jupyter Notebooks**
- 📊 Análise integrada de dados
- 🔗 Relacionamento entre múltiplos datasets

---

## 📚 Recursos Adicionais

- 📖 [Python CSV - Documentação](https://docs.python.org/pt-br/3/library/csv.html)
- 📖 [Python JSON - Documentação](https://docs.python.org/pt-br/3/library/json.html)
- 📖 [Python datetime - Documentação](https://docs.python.org/pt-br/3/library/datetime.html)
- 🎥 [Working with Files in Python](https://www.youtube.com/results?search_query=python+working+with+files)

---

<div align="center">

[⬅️ Semana Anterior](../semana_03/README.md) | [Voltar ao Módulo 01](../README.md) | [Próxima Semana ➡️](../semana_05/README.md)

</div>
