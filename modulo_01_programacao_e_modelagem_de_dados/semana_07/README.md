# 📂 Semana 07 - Modelagem de Dados e SQL

## 📝 Resumo da Semana
Nesta semana aprendemos sobre modelagem de banco de dados, focando em estruturas relacionais, normalização e relacionamentos entre tabelas. Introdução aos conceitos de banco de dados SQL e design de esquemas relacionais.

## 🎯 Objetivos de Aprendizado
- Compreender conceitos de modelagem de dados
- Identificar entidades e relacionamentos
- Aplicar normalização de banco de dados
- Projetar esquemas de banco de dados relacionais
- Criar diagramas entidade-relacionamento (ER)

## 💻 Tecnologias Utilizadas
- **Python 3.14.0**
- **Pandas 2.3.3** - Manipulação de dados
- **NumPy 2.3.4** - Computação numérica
- **Matplotlib 3.10.7** - Visualização
- **Seaborn 0.13.2** - Visualização estatística
- **SQL** - Linguagem de consulta estruturada
- **Modelagem ER** - Diagramas entidade-relacionamento

## 📁 Estrutura da Semana
```
semana_07/
├── aula_um/
│   └── Modelo_E-commerce.png   # Exemplo de diagrama ER (demonstração em aula)
├── aula_dois/
│   ├── Conceitual_2.brM3       # Modelo conceitual no BrModelo
│   ├── image.png               # Exportação do diagrama ER
│   └── Captura de tela...png   # Screenshot do modelo
├── Trello/
│   └── image.png               # Exercício de modelagem Trello
├── venv/                       # Ambiente virtual Python
├── requirements.txt            # Dependências do projeto
└── README.md
```

## 🚀 Conceitos Aplicados

### Aula 01 - Modelagem de Banco de Dados
**Arquivos:** `aula_um/Modelo_E-commerce.png`

#### Fundamentos de Modelagem de Dados:

**Conceitos Abordados:**

**1. Entidades**
- Identificação de objetos do mundo real
- Definição de atributos
- Escolha de chaves primárias
- Exemplo demonstrado: modelo de e-commerce

**2. Relacionamentos**
- Tipos de relacionamento entre entidades
- Um para Um (1:1)
- Um para Muitos (1:N)
- Muitos para Muitos (N:N)
- Uso de tabelas intermediárias (junction tables)

**3. Atributos e Chaves**
- **Chaves Primárias (PK):** Identificadores únicos de registros
- **Chaves Estrangeiras (FK):** Relacionamentos entre tabelas
- **Atributos descritivos:** Dados específicos de cada entidade
- **Atributos compostos:** Múltiplos valores em um atributo

**4. Normalização**
- **1ª Forma Normal (1FN):** Valores atômicos (indivisíveis)
- **2ª Forma Normal (2FN):** Dependência funcional completa
- **3ª Forma Normal (3FN):** Sem dependências transitivas
- Benefícios: Redução de redundância e consistência dos dados

**5. Cardinalidade**
- Definição de quantos registros podem se relacionar
- Cardinalidade mínima e máxima
- Notações: 1:1, 1:N, N:N

**6. Diagramas ER**
- Representação visual do modelo de dados
- Notações padrão (Chen, Crow's Foot, UML)
- Identificação de entidades, atributos e relacionamentos

---

### Aula 02 - Prática de Modelagem com BrModelo
**Arquivos:** `aula_dois/Conceitual_2.brM3`, `aula_dois/image.png`

#### Ferramenta de Modelagem:

**BrModelo - Ferramenta CASE**
- Software nacional para modelagem de dados
- Criação de diagramas conceituais, lógicos e físicos
- Exportação de modelos para SQL
- Interface intuitiva para design de banco de dados

**Atividade Prática:**
- Criação de modelo conceitual personalizado
- Definição de entidades e relacionamentos específicos
- Aplicação de cardinalidade e normalização
- Exportação e documentação do modelo

**Entregáveis:**
- Arquivo `.brM3` com modelo conceitual
- Diagramas exportados em formato de imagem
- Screenshots do processo de modelagem

---

### Trello - Exercício Prático de Modelagem
**Arquivos:** `Trello/image.png`

#### Exercício Complementar:

**Objetivo:**
- Aplicar os conceitos de modelagem aprendidos
- Criar diagrama ER para cenário proposto
- Praticar identificação de entidades e relacionamentos

**Conteúdo:**
- Modelo de dados elaborado conforme exercício Trello
- Aplicação prática dos conceitos de normalização
- Definição de cardinalidade e chaves

---

## 📊 Exemplo Prático

### Estrutura Genérica de Modelagem:

```sql
-- Exemplo de estrutura conceitual demonstrada em aula

ENTIDADES:
- Identificação de objetos do negócio
- Definição de atributos relevantes
- Estabelecimento de chaves primárias

RELACIONAMENTOS:
- Mapeamento de conexões entre entidades
- Definição de cardinalidade
- Criação de tabelas associativas quando necessário

NORMALIZAÇÃO:
- Aplicação das formas normais
- Eliminação de redundâncias
- Garantia de integridade dos dados
```

---

## 🔧 Configuração do Ambiente
```powershell
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
.\venv\Scripts\Activate.ps1

# Instalar dependências
pip install -r requirements.txt
# ou
pip install pandas numpy matplotlib seaborn notebook ipykernel

# Registrar kernel Jupyter
python -m ipykernel install --user --name=semana_07 --display-name="Python (semana_07)"
```

## ✅ Habilidades Desenvolvidas

### Modelagem de Dados:
✅ Identificação de entidades e atributos  
✅ Definição de relacionamentos entre tabelas  
✅ Aplicação de normalização (1FN, 2FN, 3FN)  
✅ Criação de diagramas ER  
✅ Definição de chaves primárias e estrangeiras  

### Conceitos de Banco de Dados:
✅ Compreensão de cardinalidade (1:1, 1:N, N:N)  
✅ Tabelas intermediárias (junction tables)  
✅ Integridade referencial  
✅ Design de esquemas relacionais  

### Aplicação Prática:
✅ Análise de requisitos de negócio  
✅ Identificação de entidades do domínio  
✅ Definição de relacionamentos complexos  
✅ Aplicação de técnicas de normalização  
✅ Criação de modelos escaláveis e consistentes  

### Ferramentas:
✅ BrModelo para criação de diagramas ER  
✅ Exportação de modelos para SQL  
✅ Documentação visual de estruturas de dados  
✅ Versionamento de modelos conceituais  

---

[⬅️ Voltar ao Módulo 01](../README.md)
