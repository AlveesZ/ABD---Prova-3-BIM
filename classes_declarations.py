from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, DateTime, create_engine, ForeignKey

# <dbms>[+<driver>]://<user>:<pass>@<host>[:<port>][/<database>]
URL="mysql+mysqlconnector://rober:roberto@localhost:3306/intro_orm"
engine = create_engine(url=URL)

Base = declarative_base()


class numero_casa(Base):
    __tablename__ = "numero_casa"
    id_numero = Column(Integer, primary_key=True)
    numero = Column(Integer, nullable = False )
    id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"), nullable = True)

class Endereço(Base):
    __tablename__ = "Endereco"
    id_endereco = Column(Integer, primary_key=True)
    rua = Column(String(255), nullable=False  )
    bairro = Column(String(255), nullable=False)
    cidade = Column(String(255), nullable=False)
    endereco = relationship("numero_casa")
    endereco_dois = relationship('Pais')
    endereco_tres = relationship('Vendedor')
    id_vendedor = Column(Integer, ForeignKey("Vendedor.id_vendedor"), nullable = False)
    id_cliente = Column(Integer, ForeignKey("Cliente.id_cliente"), nullable = False)

class Cliente(Base):
    __tablename__ = "Cliente"
    id_cliente = Column(Integer, primary_key=True, nullable = False)
    nome = Column(String(255), nullable=False)
    cpf = Column(Integer, nullable=False)
    cliente = relationship("Endereco")
    cliente_dois = relationship("Telefone")
    e_mail = Column(String(255), nullable=False)
    id_venda = Column(Integer, ForeignKey("Venda.id_venda"), nullable=False)

class País(Base):
    __tablename__ = "Pais"
    id_pais = Column(Integer, primary_key=True, nullable = False)
    nome = Column(String(255), nullable=False)
    sigla = Column(String(4), nullable=False)
    id_endereço = Column(Integer, ForeignKey("Endereco.id_endereco"), nullable=False)

class Produto(Base):
    __tablename__ = "Produto"
    id_produto = Column(Integer, primary_key=True, nullable = False)
    descricao = Column(String(255), nullable=False)
    data_cadastro = Column(DateTime, nullable=False)
    valor = Column(Integer, nullable=False)
    qtd_estoque = Column(Integer, nullable=False)
    id_venda = Column(Integer, ForeignKey("Venda.id_venda"), nullable=False)

class Telefone(Base):
    __tablename__="Telefone"
    id_telefone = Column(Integer, primary_key=True, nullable = False)
    numero = Column(Integer, nullable=False)
    ddd = Column(Integer, nullable=False)
    ddi = Column(Integer, nullable=False)
    id_vendedor = Column(Integer, ForeignKey("Vendedor.id_vendedor"), nullable=False)
    id_cliente = Column(Integer, ForeignKey("Cliente.id_cliente"), nullable = False)

class Venda(Base):
    __tablename__ = "Venda"
    id_venda = Column(Integer, primary_key=True, nullable = False)
    data_venda = Column(DateTime, nullable=False)
    venda = relationship('Cliente')
    venda_dois = relationship('Produto')
    venda_tres = relationship('Vendedor')
    valor_total = Column(Integer, nullable=False)

class Vendedor(Base):
    __tablename__ = "Vendedor"
    id_vendedor = Column(Integer, primary_key=True, nullable = False)
    nome = Column(String(255), nullable=False)
    cpf = Column(Integer, nullable=False)
    vendedor = relationship('Endereco')
    vendedor_dois = relationship("Telefone")
    data_admissao = Column(DateTime, nullable=False)
    id_endereco = Column(Integer, ForeignKey("Endereco.id_endereco"), nullable=False)
    id_venda = Column(Integer, ForeignKey("Venda.id_venda"), nullable=False)

Base.metadata.create_all(engine)