# 📂 Semana 08 - Modelagem NoSQL e SQL Essencial

## 📝 Resumo da Semana
Nesta semana aprendemos sobre modelagem de dados NoSQL (não relacional) e SQL essencial, cobrindo desde conceitos de bancos não relacionais até comandos fundamentais DDL e DML para manipulação de bancos de dados relacionais.

## 🎯 Objetivos de Aprendizado
- Compreender conceitos de modelagem NoSQL
- Diferenciar tipos de bancos NoSQL (Documentos, Grafos, Colunas, Chave-Valor)
- Aplicar normalização em modelagem lógica relacional
- Dominar comandos SQL essenciais (DDL + DML)
- Criar, alterar e deletar estruturas de banco de dados
- Realizar consultas com filtros e ordenação

## 💻 Tecnologias Utilizadas
- **Python 3.14.0**
- **Pandas** - Manipulação de dados
- **NumPy** - Computação numérica
- **SQL** - Linguagem de consulta estruturada
- **NoSQL** - Conceitos de bancos não relacionais
- **SQLite** - Banco de dados relacional leve

## 📁 Estrutura da Semana
```
semana_08/
├── aula_um/          # Arquivos e exercícios da primeira aula
├── Trello/           # Exercícios práticos Trello
├── venv/             # Ambiente virtual Python
├── requirements.txt  # Dependências do projeto
└── README.md
```

## 🚀 Conceitos Aplicados

### Parte 1 - Modelagem NoSQL

#### 1. Conceitos de Modelagem Não Relacional

**Características dos Bancos NoSQL:**
- Flexibilidade de esquema (schema-less ou schema-flexible)
- Escalabilidade horizontal (distribuição de dados)
- Alta performance para grandes volumes de dados
- Otimização para casos de uso específicos
- Diferentes modelos de dados para diferentes necessidades

**Diferenças NoSQL vs SQL:**
- **SQL:** Estrutura rígida, tabelas relacionadas, ACID, escalabilidade vertical
- **NoSQL:** Estrutura flexível, diversos modelos, BASE, escalabilidade horizontal

---

#### 2. Tipos de Bancos NoSQL

**A. Bancos de Documentos**
- **Conceito:** Armazenam dados em documentos (JSON, BSON, XML)
- **Exemplos:** MongoDB, CouchDB, Firebase
- **Caso de uso:** Aplicações web, catálogos de produtos, perfis de usuário
- **Estrutura:**
```json
{
  "_id": "12345",
  "nome": "João Silva",
  "email": "joao@email.com",
  "enderecos": [
    {
      "tipo": "residencial",
      "cidade": "São Paulo",
      "estado": "SP"
    }
  ]
}
```

**B. Bancos de Grafos**
- **Conceito:** Armazenam dados como nós (entidades) e arestas (relacionamentos)
- **Exemplos:** Neo4j, Amazon Neptune, ArangoDB
- **Caso de uso:** Redes sociais, sistemas de recomendação, detecção de fraudes
- **Estrutura:** Nós conectados por relacionamentos com propriedades

**C. Bancos de Colunas (Column-Family)**
- **Conceito:** Organizam dados em colunas ao invés de linhas
- **Exemplos:** Apache Cassandra, HBase, Google Bigtable
- **Caso de uso:** Analytics, séries temporais, grandes volumes de escrita
- **Estrutura:** Famílias de colunas com chaves de linha

**D. Bancos Chave-Valor**
- **Conceito:** Estrutura simples de pares chave-valor (como dicionários)
- **Exemplos:** Redis, Amazon DynamoDB, Memcached
- **Caso de uso:** Cache, sessões de usuário, carrinho de compras
- **Estrutura:**
```
chave: "usuario:12345"
valor: {"nome": "João", "status": "ativo"}
```

---

### Parte 2 - Modelagem Lógica Relacional

#### 1. Normalização de Banco de Dados

**Objetivos da Normalização:**
- Eliminar redundância de dados
- Garantir integridade dos dados
- Facilitar manutenção e atualizações
- Otimizar espaço de armazenamento

**1ª Forma Normal (1FN):**
- Valores atômicos (indivisíveis) em cada coluna
- Cada coluna deve conter apenas um tipo de dado
- Eliminar grupos repetidos

**Exemplo - ANTES (não normalizado):**
```
Cliente | Telefones
João    | 1111-1111, 2222-2222
```

**Exemplo - DEPOIS (1FN):**
```
Cliente | Telefone
João    | 1111-1111
João    | 2222-2222
```

**2ª Forma Normal (2FN):**
- Estar em 1FN
- Todos os atributos não-chave devem depender da chave primária completa
- Eliminar dependências parciais

**3ª Forma Normal (3FN):**
- Estar em 2FN
- Eliminar dependências transitivas
- Atributos não-chave não devem depender de outros atributos não-chave

---

#### 2. Chaves Primárias e Estrangeiras

**Chave Primária (Primary Key - PK):**
- Identificador único de cada registro
- Não pode ser NULL
- Não pode ter valores duplicados
- Pode ser simples (uma coluna) ou composta (múltiplas colunas)

**Exemplo:**
```sql
CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);
```

**Chave Estrangeira (Foreign Key - FK):**
- Referencia a chave primária de outra tabela
- Garante integridade referencial
- Estabelece relacionamentos entre tabelas

**Exemplo:**
```sql
CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY,
    cliente_id INT,
    data_pedido DATE,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);
```

---

### Parte 3 - SQL Essencial (DDL + DML)

#### 1. DDL - Data Definition Language (Definição de Estrutura)

**CREATE TABLE - Criar Tabelas**
```sql
-- Sintaxe básica
CREATE TABLE nome_tabela (
    coluna1 TIPO CONSTRAINT,
    coluna2 TIPO CONSTRAINT,
    ...
);

-- Exemplo prático
CREATE TABLE produtos (
    produto_id INT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2),
    estoque INT DEFAULT 0,
    categoria VARCHAR(50)
);
```

**ALTER TABLE - Modificar Estrutura**
```sql
-- Adicionar coluna
ALTER TABLE produtos ADD descricao TEXT;

-- Modificar coluna
ALTER TABLE produtos MODIFY preco DECIMAL(12,2);

-- Renomear coluna
ALTER TABLE produtos RENAME COLUMN nome TO nome_produto;

-- Deletar coluna
ALTER TABLE produtos DROP COLUMN descricao;
```

**DROP TABLE - Deletar Tabela**
```sql
-- Deletar tabela (cuidado: operação irreversível!)
DROP TABLE nome_tabela;

-- Deletar se existir
DROP TABLE IF EXISTS nome_tabela;
```

---

#### 2. DML - Data Manipulation Language (Manipulação de Dados)

**INSERT - Inserir Dados**
```sql
-- Inserir registro completo
INSERT INTO produtos (produto_id, nome, preco, estoque, categoria)
VALUES (1, 'Notebook', 2500.00, 10, 'Eletrônicos');

-- Inserir múltiplos registros
INSERT INTO produtos VALUES
    (2, 'Mouse', 50.00, 100, 'Periféricos'),
    (3, 'Teclado', 150.00, 50, 'Periféricos');

-- Inserir apenas algumas colunas
INSERT INTO produtos (produto_id, nome, preco)
VALUES (4, 'Monitor', 800.00);
```

**UPDATE - Atualizar Dados**
```sql
-- Atualizar registro específico
UPDATE produtos
SET preco = 2300.00, estoque = 15
WHERE produto_id = 1;

-- Atualizar múltiplos registros
UPDATE produtos
SET categoria = 'Acessórios'
WHERE categoria = 'Periféricos';

-- Atualizar com cálculo
UPDATE produtos
SET preco = preco * 1.1
WHERE categoria = 'Eletrônicos';
```

**DELETE - Deletar Dados**
```sql
-- Deletar registro específico
DELETE FROM produtos
WHERE produto_id = 4;

-- Deletar com condição
DELETE FROM produtos
WHERE estoque = 0;

-- ATENÇÃO: Deletar todos os registros (use com cuidado!)
DELETE FROM produtos;
```

---

#### 3. SELECT - Consultas e Filtros

**SELECT Básico**
```sql
-- Selecionar todas as colunas
SELECT * FROM produtos;

-- Selecionar colunas específicas
SELECT nome, preco FROM produtos;

-- SELECT com alias (apelido)
SELECT nome AS produto, preco AS valor FROM produtos;

-- SELECT com cálculos
SELECT nome, preco, preco * 0.9 AS preco_desconto FROM produtos;
```

**WHERE - Filtros**
```sql
-- Filtro simples
SELECT * FROM produtos WHERE categoria = 'Eletrônicos';

-- Comparadores: =, !=, <, >, <=, >=
SELECT * FROM produtos WHERE preco > 100.00;

-- BETWEEN (intervalo)
SELECT * FROM produtos WHERE preco BETWEEN 50 AND 500;

-- IN (lista de valores)
SELECT * FROM produtos WHERE categoria IN ('Eletrônicos', 'Periféricos');

-- LIKE (padrão de texto)
SELECT * FROM produtos WHERE nome LIKE '%book%';
-- % = qualquer sequência de caracteres
-- _ = um único caractere

-- IS NULL / IS NOT NULL
SELECT * FROM produtos WHERE descricao IS NULL;
```

**Operadores Lógicos**
```sql
-- AND (todas as condições devem ser verdadeiras)
SELECT * FROM produtos
WHERE categoria = 'Eletrônicos' AND preco < 3000;

-- OR (pelo menos uma condição deve ser verdadeira)
SELECT * FROM produtos
WHERE categoria = 'Eletrônicos' OR categoria = 'Periféricos';

-- NOT (negação)
SELECT * FROM produtos
WHERE NOT categoria = 'Acessórios';

-- Combinando operadores
SELECT * FROM produtos
WHERE (categoria = 'Eletrônicos' OR categoria = 'Periféricos')
  AND preco > 100
  AND estoque > 0;
```

**ORDER BY - Ordenação**
```sql
-- Ordenação crescente (padrão)
SELECT * FROM produtos ORDER BY preco;
SELECT * FROM produtos ORDER BY preco ASC;

-- Ordenação decrescente
SELECT * FROM produtos ORDER BY preco DESC;

-- Ordenar por múltiplas colunas
SELECT * FROM produtos
ORDER BY categoria ASC, preco DESC;

-- Ordenar com limite
SELECT * FROM produtos
ORDER BY preco DESC
LIMIT 5;  -- Top 5 produtos mais caros
```

**Consultas Combinadas**
```sql
-- Exemplo completo
SELECT nome, preco, estoque, categoria
FROM produtos
WHERE categoria IN ('Eletrônicos', 'Periféricos')
  AND preco BETWEEN 100 AND 2000
  AND estoque > 0
ORDER BY preco DESC;
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

# Registrar kernel Jupyter
python -m ipykernel install --user --name=semana_08 --display-name="Python (semana_08)"
```

## ✅ Habilidades Desenvolvidas

### Modelagem NoSQL:
✅ Compreensão de bancos não relacionais  
✅ Identificação de casos de uso para NoSQL  
✅ Bancos de Documentos (MongoDB)  
✅ Bancos de Grafos (Neo4j)  
✅ Bancos de Colunas (Cassandra)  
✅ Bancos Chave-Valor (Redis)  

### Modelagem Lógica Relacional:
✅ Aplicação de 1ª Forma Normal (1FN)  
✅ Aplicação de 2ª Forma Normal (2FN)  
✅ Aplicação de 3ª Forma Normal (3FN)  
✅ Definição de chaves primárias  
✅ Definição de chaves estrangeiras  
✅ Garantia de integridade referencial  

### SQL - DDL (Data Definition Language):
✅ CREATE TABLE (criação de tabelas)  
✅ ALTER TABLE (modificação de estrutura)  
✅ DROP TABLE (remoção de tabelas)  
✅ Definição de constraints (PK, FK, NOT NULL, DEFAULT)  

### SQL - DML (Data Manipulation Language):
✅ INSERT (inserção de dados)  
✅ UPDATE (atualização de dados)  
✅ DELETE (remoção de dados)  
✅ SELECT (consultas básicas)  

### SQL - Consultas e Filtros:
✅ WHERE com operadores de comparação  
✅ Operadores lógicos (AND, OR, NOT)  
✅ BETWEEN, IN, LIKE  
✅ IS NULL / IS NOT NULL  
✅ ORDER BY (ordenação crescente e decrescente)  
✅ LIMIT (limitação de resultados)  

---

[⬅️ Voltar ao Módulo 01](../README.md)

