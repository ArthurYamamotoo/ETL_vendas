-- Cria a tabela de clientes primeiro
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INT PRIMARY KEY,
    nome TEXT,
    email TEXT,
    documento TEXT,
    tipo_pessoa TEXT,
    tipo_contato TEXT
);

-- Depois cria a tabela de vendas com referência ao cliente
CREATE TABLE IF NOT EXISTS vendas (
    id_venda INT PRIMARY KEY,
    id_cliente INT REFERENCES clientes(id_cliente),
    data_venda DATE,
    valor NUMERIC(10, 2)
);