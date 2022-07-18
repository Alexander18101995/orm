import sqlalchemy as sq
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

DSN = 'postgres://postgres:postgres@localhost:5432/test_db'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(lenght=40))

    pub = relationship('book', back_population='b')

class book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(lenght=40))
    id_publisher = sq.Column(sq.Integer, unique=True)

    b = relationship('publisher',back_population='pub')
    bs = relationship('stock',back_population='sb')
class shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(lenght=40))

    shop = relationship('stock', back_population='stock')

class stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer,unique=True)
    id_shop = sq.Column(sq.Integer, unique=True)
    count = sq.Column(sq.Integer)

    stock = relationship('shop', back_population='shop')
    sb = relationship('book', back_population='bs')
    s = relationship('sale', back_population='sale')
class sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer)
    count = sq.Column(sq.Integer)

    sale = relationship('stock', back_population='s')

session.close()