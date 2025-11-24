# 📝 Exercícios SQL - Semana 09

## 🎯 Problemas e Soluções

### **Exercício 1: JOIN entre Clientes e Pedidos**

**Problema:** Dado duas tabelas [clientes e pedidos], combine clientes e pedidos para exibir nome e valor total dos pedidos.

**Solução:**
```sql
SELECT c.nome, p.valor_total
FROM clientes c
INNER JOIN pedidos p ON c.cliente_id = p.cliente_id;
```

---

### **Exercício 2: Agregações**

**Problema:** Faça as agregações:
- Total de vendas por mês
- Quantidade de pedidos por cliente

**Solução:**
```sql
-- Total de vendas por mês
SELECT 
    MONTH(data_pedido) AS mes,
    YEAR(data_pedido) AS ano,
    SUM(valor_total) AS total_vendas
FROM pedidos
GROUP BY YEAR(data_pedido), MONTH(data_pedido)
ORDER BY ano, mes;

-- Quantidade de pedidos por cliente
SELECT 
    cliente_id,
    COUNT(*) AS quantidade_pedidos
FROM pedidos
GROUP BY cliente_id;
```

---

### **Exercício 3: CTE (Common Table Expression)**

**Problema:** Crie uma CTE que calcule o total de vendas por cliente e selecione apenas os que gastaram mais de R$ 500,00.

**Solução:**
```sql
WITH TotalVendasCliente AS (
    SELECT 
        cliente_id,
        SUM(valor_total) AS total_gasto
    FROM pedidos
    GROUP BY cliente_id
)
SELECT 
    cliente_id,
    total_gasto
FROM TotalVendasCliente
WHERE total_gasto > 500.00;
```

---

### **Exercício 4: Funções de String e Data**

**Problema:**
- Extraia apenas o mês da coluna data
- Concatene nome e e-mail dos clientes

**Solução:**
```sql
-- Extrair apenas o mês da coluna data
SELECT 
    MONTH(data) AS mes
FROM pedidos;

-- Concatenar nome e e-mail dos clientes
SELECT 
    CONCAT(nome, ' - ', email) AS nome_email
FROM clientes;
```

---

### **Exercício 5: Consultas Analíticas**

**Problema:** Crie consultas que retornem:
- Top 5 clientes por valor de compra
- Média de pedidos por mês
- Receita total por trimestre

**Solução:**
```sql
-- Top 5 clientes por valor de compra
SELECT 
    cliente_id,
    SUM(valor_total) AS valor_total_compras
FROM pedidos
GROUP BY cliente_id
ORDER BY valor_total_compras DESC
LIMIT 5;

-- Média de pedidos por mês
SELECT 
    YEAR(data_pedido) AS ano,
    MONTH(data_pedido) AS mes,
    AVG(valor_total) AS media_pedidos
FROM pedidos
GROUP BY YEAR(data_pedido), MONTH(data_pedido)
ORDER BY ano, mes;

-- Receita total por trimestre
SELECT 
    YEAR(data_pedido) AS ano,
    QUARTER(data_pedido) AS trimestre,
    SUM(valor_total) AS receita_total
FROM pedidos
GROUP BY YEAR(data_pedido), QUARTER(data_pedido)
ORDER BY ano, trimestre;
```

---

## 📊 Conceitos Aplicados

- ✅ **JOIN** - Relacionamento entre tabelas
- ✅ **Funções de Agregação** - SUM, COUNT, AVG
- ✅ **GROUP BY** - Agrupamento de dados
- ✅ **CTE (Common Table Expression)** - Consultas temporárias
- ✅ **Funções de Data** - MONTH, YEAR, QUARTER
- ✅ **Funções de String** - CONCAT
- ✅ **ORDER BY** - Ordenação de resultados
- ✅ **LIMIT** - Limitação de registros
- ✅ **WHERE** - Filtros condicionais

---

## 🎓 Habilidades Desenvolvidas

- Relacionamento de múltiplas tabelas
- Análise temporal de dados
- Cálculos agregados e estatísticos
- Consultas analíticas complexas
- Uso de CTEs para consultas reutilizáveis
- Manipulação de strings e datas
