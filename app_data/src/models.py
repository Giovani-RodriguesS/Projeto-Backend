from sqlalchemy.sql.sqltypes import Integer, String, DateTime, Float
from sqlalchemy import Column, Table, MetaData

meta = MetaData()

people = Table(
    'people', meta, 
    Column('person_id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('gender', String(1)),
    Column('birth_date', DateTime),
    Column('address', String(255)),
    Column('salary', Float),
    Column('cpf', String(11))
)

accounts = Table(
    'accounts', meta, 
    Column('account_id', Integer, primary_key=True),
    Column('status_id', Integer, unique=True),
    Column('due_day', Integer),
    Column('person_id', Integer, unique=True),
    Column('balance', Float),
    Column('avaliable_balance', Float)
)

cards = Table(
    'cards', meta, 
    Column('card_id', Integer, primary_key=True),
    Column('card_number', String(255)),
    Column('account_id', Integer, unique=True),
    Column('status_id', Integer, unique=True),
    Column('limit', Float),
    Column('expiration_date', String(255))
)

 	
 	
 	
 	

 	