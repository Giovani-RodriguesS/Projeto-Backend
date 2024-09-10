from sqlalchemy import create_engine, MetaData, text
from models import meta


def db_connection(url, name):
    engine = create_engine(url)

    with engine.connect() as creating_db:
        creating_db.execute(text(f"CREATE DATABASE IF NOT EXISTS {name}"))       

    engine = create_engine(f"{url}{name}")
    meta.create_all(bind=engine)
    return engine.connect()

db_name = 'mysql'
db_url = 'mysql+mysqldb://root:admin@localhost:3306/'

connect = db_connection(db_url, db_name)
