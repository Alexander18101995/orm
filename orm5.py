import sqlalchemy as sq
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

DSN = 'postgres://postgres:postgres@localhost:5432/test_db'
engine = sq.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()



Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(lenght=40))

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    publisher_id = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'))

    publisher = relationship(Publisher, backref='book')

class Stock(Base):
    __tablename__ = 'stock'
    id = sq.Column(sq.Integer, primary_key=True)
    book_id = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    shop_id = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref='stock')
    shop = relationship(Shop, backref='stock')

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer)
    date_sale = sq.Column(sq.Date)
    stock_id = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='sale')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create.all(engine)
create_tables(engine)

res = input('id...')
query_1 = session.query(Publisher).filter(Publisher.id == res)
for i in query_1.all():
    print(f'{res}-{i.name}')

session.close()