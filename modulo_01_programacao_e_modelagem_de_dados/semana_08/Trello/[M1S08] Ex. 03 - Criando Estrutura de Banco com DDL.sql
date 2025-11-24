CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOTNULL,
    endereco VARCHAR(150) NOT NULL
);
CREATE TABLE produto (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2)
);
CREATE TABLE pedido (
    id INTEGER PRIMARY KEY,
    id_cliente INTEGER,
    data TIMESTAMP NOT NULL,

    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
);
CREATE TABLE itens_pedido (
    id_pedido INTEGER,
    id_produto INTEGER,
    quantidade INTEGER NOT NULL,
    preco_unitario DECIMAL(10,2),

    PRIMARY KEY (id_pedido, id_produto),

    FOREIGN KEY (id_pedido) REFERENCES pedido(id),
    FOREIGN KEY (id_produto) REFERENCES produto(id)
);
