CREATE DATABASE intro_orm;
Use DATABASE intro_orm

CREATE TABLE  Numero_Casa (
    id_numero INTEGER  AUTO_INCREMENT  PRIMARY_KEY,
    numero VARCHAR(12) NOT NULL, 
    Foreign key (id_endereco) References Endereco(id_endereco)
 );

CREATE TABLE Endereco (
    id_endereco INTEGER AUTO_INCREMENT PRIMARY_KEY,
    rua VARCHAR(100) NOT NULL,
    bairro VARCHAR(50) NOT NULL,
    cidade VARCHAR(50) NOT NULL,
    Foreign key (id_vendedor) References Vendedor(id_vendedor),
    Foreign key (id_cliente)  References Cliente(id_cliente)
);

CREATE TABLE Cliente (
    id_cliente INTEGER AUTO_INCREMENT PRIMARY_KEY,
    nome VARCHAR(100) NOT NULL,
    cpf INTEGER NOT NULL,
    e_mail VARCHAR(150),
    Foreign key(id_venda) References Venda(id_venda)
);

CREATE TABLE Pais (
    id_pais INTEGER AUTO_INCREMENT PRIMARY_KEY,
    nome VARCHAR(50) NOT NULL,
    sigla VARCHAR(4) NOT NULL,
    Foreign Key(id_endereco) References Endereco(id_endereco)
);

CREATE TABLE Produto(
    id_produto INTEGER AUTO_INCREMENT PRIMARY_KEY,
    nome VARCHAR(100) NOT NULL,
    descricao VARCHAR(300) NOT NULL,
    data_cadastro DATETIME NOT NULL,
    valor INTEGER NOT NULL,
    qtd_estoque INTEGER NOT NULL,
    Foreign Key (id_venda ) References Venda(id_venda)
);

CREATE TABLE Telefone (
    id_telefone INTEGER AUTO_INCREMENT PRIMARY_KEY,
    numero INTEGER NOT NULL,
    DDD INTEGER NOT NULL,
    DDI INTEGER NOT NULL,
    Foreign Key(id_cliente) References Cliente(id_cliente),
    Foreign Key(id_vendedor) References Vendedor(id_vendedor)
);

CREATE TABLE Venda (
    id_venda INTEGER AUTO_INCREMENT PRIMARY_KEY,
    data_venda DATETIME NOT NULL,
    valor_total INTEGER NOT NULL
);

CREATE TABLE Vendedor(
    id_vendedor INTEGER AUTO_INCREMENT PRIMARY_KEY,
    nome VARCHAR(50) NOT NULL,
    cpf  INTEGER NOT NULL,
    data_admissao DATETIME NOT NULL,
    Foreign Key(id_endereco) References Endereco(id_endereco),
    Foreign Key(id_telefone ) References Telefone(id_telefone)
);

