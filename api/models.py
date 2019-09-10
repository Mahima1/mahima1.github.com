'''
DB Schema
'''
from .extensions import db
# import sqlite3
# from sqlalchemy import func

session = db.session

Column = db.Column
Integer = db.Integer
String = db.String
Text = db.Text
Boolean = db.Boolean
DateTime = db.DateTime
Decimal = db.DECIMAL


# Blob = db.BLOB

# class BinanceData(db.Model):
#
#     id=Column(Integer, primary_key= True)
#
#     username=Column(String(50), unique=True, nullable=False)
#
#     email=Column(String(100), unique=True, nullable=False)
#
#     created=Column(DateTime, nullable=True)
#
#     bio=Column(Text, nullable=True)
#
#     admin=Column(Boolean, nullable=True)

# def add_user(kwargs):
#     user = User(**kwargs)
#     session.add(user)
#     session.commit()
#     return user

# session.add_all([])
#
# def find_email(name):
#     return session.query(User).filter_by(username = name).first().email

class BinanceData(db.Model):
    # __tablename__ = "binance_table"

    Id = Column(Integer, primary_key=True)
    Open_time = Column(DateTime)
    Open = Column(Decimal)
    High = Column(Decimal)
    Low = Column(Decimal)
    Close = Column(Decimal)
    Volume = Column(Integer)
    Close_time = Column(DateTime)
    Quote_asset_volume = Column(Decimal)
    Number_of_trades = Column(Integer)
    Buy_base_asset = Column(Decimal)
    Buy_quote_asset = Column(Decimal)
    Ignore = Column(Decimal)


def add_database(kwargs):
    data = BinanceData(**kwargs)
    session.add(data)
    session.commit()


def get_database():
    b = session.query(BinanceData).all()
    return b


def empty_database():
    try:
        num_rows_deleted = session.query(BinanceData).delete()
        session.commit()
        return num_rows_deleted
    except:
        session.rollback()
