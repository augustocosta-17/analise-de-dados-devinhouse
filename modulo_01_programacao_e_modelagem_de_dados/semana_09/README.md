# 📂 Semana 09 - SQL Avançado

## 📝 Resumo da Semana
Nesta semana aprofundamos em SQL avançado, explorando JOINs complexos, agregações, subconsultas, CTEs (Common Table Expressions), funções de manipulação de dados e criação de Views.

## 🎯 Objetivos de Aprendizado
- Dominar diferentes tipos de JOINs (INNER, LEFT, RIGHT, FULL OUTER)
- Realizar agregações complexas com GROUP BY e HAVING
- Utilizar DISTINCT para eliminar duplicatas
- Criar subconsultas e CTEs para consultas reutilizáveis
- Aplicar funções de data e texto
- Criar e gerenciar Views

## 💻 Tecnologias Utilizadas
- **SQL** - Linguagem de consulta estruturada
- **PostgreSQL / MySQL** - Sistemas de gerenciamento de banco de dados
- **CTEs (Common Table Expressions)** - Consultas temporárias
- **Views** - Tabelas virtuais

## 📁 Estrutura da Semana
```
semana_09/
├── Trello/
│   └── exercicios_sql.md    # Exercícios práticos resolvidos
└── README.md
```

## 🚀 Conceitos Aplicados

### 1. JOINs - Relacionamento entre Tabelas

**INNER JOIN**
```sql
-- Retorna apenas registros que têm correspondência em ambas as tabelas
SELECT c.nome, p.valor_total
FROM clientes c
INNER JOIN pedidos p ON c.cliente_id = p.cliente_id;
```

**LEFT JOIN (LEFT OUTER JOIN)**
```sql
-- Retorna todos os registros da tabela da esquerda e correspondências da direita
SELECT c.nome, p.valor_total
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id;
```

**RIGHT JOIN (RIGHT OUTER JOIN)**
```sql
-- Retorna todos os registros da tabela da direita e correspondências da esquerda
SELECT c.nome, p.valor_total
FROM clientes c
RIGHT JOIN pedidos p ON c.cliente_id = p.cliente_id;
```

**FULL OUTER JOIN**
```sql
-- Retorna todos os registros de ambas as tabelas (com ou sem correspondência)
SELECT c.nome, p.valor_total
FROM clientes c
FULL OUTER JOIN pedidos p ON c.cliente_id = p.cliente_id;
```

---

### 2. Agregações - GROUP BY e Funções

**Funções de Agregação**
```sql
-- SUM: Soma de valores
SELECT categoria, SUM(preco) AS total_categoria
FROM produtos
GROUP BY categoria;

-- COUNT: Contagem de registros
SELECT categoria, COUNT(*) AS quantidade_produtos
FROM produtos
GROUP BY categoria;

-- AVG: Média de valores
SELECT categoria, AVG(preco) AS preco_medio
FROM produtos
GROUP BY categoria;

-- MAX / MIN: Maior e menor valor
SELECT 
    categoria, 
    MAX(preco) AS preco_maximo,
    MIN(preco) AS preco_minimo
FROM produtos
GROUP BY categoria;
```

**GROUP BY com múltiplas colunas**
```sql
SELECT 
    YEAR(data_pedido) AS ano,
    MONTH(data_pedido) AS mes,
    SUM(valor_total) AS total_vendas
FROM pedidos
GROUP BY YEAR(data_pedido), MONTH(data_pedido);
```

---

### 3. DISTINCT e HAVING

**DISTINCT - Eliminar Duplicatas**
```sql
-- Retorna valores únicos
SELECT DISTINCT categoria FROM produtos;

-- Combinação única de múltiplas colunas
SELECT DISTINCT cliente_id, cidade FROM clientes;
```

**HAVING - Filtro após Agregação**
```sql
-- Diferença: WHERE filtra antes do GROUP BY, HAVING filtra depois
SELECT 
    categoria, 
    COUNT(*) AS quantidade
FROM produtos
GROUP BY categoria
HAVING COUNT(*) > 10;

-- HAVING com múltiplas condições
SELECT 
    cliente_id,
    SUM(valor_total) AS total_gasto
FROM pedidos
GROUP BY cliente_id
HAVING SUM(valor_total) > 1000 AND COUNT(*) >= 5;
```

---

### 4. Subconsultas

**Subconsulta no WHERE**
```sql
-- Filtrar com base em resultado de outra consulta
SELECT nome, preco
FROM produtos
WHERE preco > (SELECT AVG(preco) FROM produtos);
```

**Subconsulta no FROM**
```sql
-- Usar resultado de consulta como tabela temporária
SELECT 
    categoria,
    AVG(preco_medio) AS media_geral
FROM (
    SELECT categoria, AVG(preco) AS preco_medio
    FROM produtos
    GROUP BY categoria
) AS subconsulta;
```

**Subconsulta com IN**
```sql
-- Filtrar com lista de valores
SELECT nome
FROM clientes
WHERE cliente_id IN (
    SELECT cliente_id 
    FROM pedidos 
    WHERE valor_total > 500
);
```

---

### 5. CTEs (Common Table Expressions) - WITH

**CTE Simples**
```sql
WITH TotalVendasCliente AS (
    SELECT 
        cliente_id,
        SUM(valor_total) AS total_gasto
    FROM pedidos
    GROUP BY cliente_id
)
SELECT 
    c.nome,
    tv.total_gasto
FROM clientes c
INNER JOIN TotalVendasCliente tv ON c.cliente_id = tv.cliente_id
WHERE tv.total_gasto > 500;
```

**Múltiplas CTEs**
```sql
WITH 
VendasPorCliente AS (
    SELECT cliente_id, SUM(valor_total) AS total
    FROM pedidos
    GROUP BY cliente_id
),
MediaVendas AS (
    SELECT AVG(total) AS media
    FROM VendasPorCliente
)
SELECT v.cliente_id, v.total
FROM VendasPorCliente v, MediaVendas m
WHERE v.total > m.media;
```

---

### 6. Funções de Data e Texto

**Funções de Data**
```sql
-- YEAR, MONTH, DAY
SELECT 
    YEAR(data_pedido) AS ano,
    MONTH(data_pedido) AS mes,
    DAY(data_pedido) AS dia
FROM pedidos;

-- DATE_TRUNC (PostgreSQL) - Truncar data
SELECT DATE_TRUNC('month', data_pedido) AS mes_ano
FROM pedidos;

-- QUARTER - Trimestre
SELECT QUARTER(data_pedido) AS trimestre
FROM pedidos;

-- DATEDIFF - Diferença entre datas
SELECT DATEDIFF(data_entrega, data_pedido) AS dias_entrega
FROM pedidos;
```

**Funções de Texto**
```sql
-- CONCAT - Concatenar strings
SELECT CONCAT(nome, ' - ', email) AS contato
FROM clientes;

-- SUBSTRING - Extrair parte da string
SELECT SUBSTRING(nome, 1, 5) AS primeiros_caracteres
FROM clientes;

-- UPPER / LOWER - Maiúsculas / Minúsculas
SELECT UPPER(nome) AS nome_maiusculo FROM clientes;
SELECT LOWER(email) AS email_minusculo FROM clientes;

-- LENGTH - Tamanho da string
SELECT nome, LENGTH(nome) AS tamanho
FROM clientes;

-- TRIM - Remover espaços
SELECT TRIM(nome) AS nome_limpo FROM clientes;
```

---

### 7. Views - Tabelas Virtuais

**Criar View**
```sql
-- View salva uma consulta complexa
CREATE VIEW vw_resumo_clientes AS
SELECT 
    c.cliente_id,
    c.nome,
    c.email,
    COUNT(p.pedido_id) AS total_pedidos,
    SUM(p.valor_total) AS total_gasto
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nome, c.email;
```

**Consultar View**
```sql
-- Usar como uma tabela normal
SELECT * FROM vw_resumo_clientes
WHERE total_gasto > 1000;
```

**Atualizar View**
```sql
CREATE OR REPLACE VIEW vw_resumo_clientes AS
SELECT 
    c.cliente_id,
    c.nome,
    COUNT(p.pedido_id) AS total_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nome;
```

**Deletar View**
```sql
DROP VIEW vw_resumo_clientes;
```

---

## 📊 Exercícios Práticos

Todos os exercícios resolvidos estão disponíveis em:
📂 **[Trello/exercicios_sql.md](./Trello/exercicios_sql.md)**

**Exercícios incluídos:**
1. JOIN entre Clientes e Pedidos
2. Agregações (Total de vendas por mês, Quantidade de pedidos)
3. CTE para filtrar clientes com gasto > R$ 500
4. Funções de Data e String (MONTH, CONCAT)
5. Consultas Analíticas (Top 5 clientes, Média mensal, Receita trimestral)

---

## ✅ Habilidades Desenvolvidas

### SQL Avançado - JOINs:
✅ INNER JOIN (correspondência exata)  
✅ LEFT JOIN (todos da esquerda)  
✅ RIGHT JOIN (todos da direita)  
✅ FULL OUTER JOIN (todos de ambas)  
✅ Múltiplos JOINs encadeados  

### Agregações e Agrupamentos:
✅ GROUP BY (agrupamento de dados)  
✅ SUM, COUNT, AVG, MAX, MIN  
✅ DISTINCT (valores únicos)  
✅ HAVING (filtro pós-agregação)  

### Consultas Complexas:
✅ Subconsultas no WHERE  
✅ Subconsultas no FROM  
✅ CTEs (Common Table Expressions)  
✅ Múltiplas CTEs encadeadas  

### Funções de Manipulação:
✅ Funções de Data (YEAR, MONTH, QUARTER, DATE_TRUNC)  
✅ Funções de Texto (CONCAT, SUBSTRING, UPPER, LOWER, TRIM)  
✅ Cálculos temporais (DATEDIFF)  

### Views:
✅ CREATE VIEW (criação de views)  
✅ CREATE OR REPLACE VIEW (atualização)  
✅ DROP VIEW (remoção)  
✅ Consultas em views  

---

[⬅️ Voltar ao Módulo 01](../README.md)
