# Transcrito no mySql


CREATE DATABASE estoque;
USE estoque;

CREATE TABLE produtos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome NVARCHAR(50) NOT NULL,
    descricao NVARCHAR(250) NOT NULL,
    quantidade INT NOT NULL,
    CHECK (quantidade >= 0),
    preco FLOAT NOT NULL,
    CHECK (preco > 0)
);

CREATE TABLE vendas(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_produto INT,
    FOREIGN KEY (id_produto) REFERENCES produtos(id),
    quantidade_vendidas INT NOT NULL,
    CHECK (quantidade_vendidas > 0),
    data_venda DATE
);

