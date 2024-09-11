from sqlalchemy import create_engine, MetaData, text
from src.models import meta


def db_connection(url, name):
    engine = create_engine(url)

    with engine.connect() as creating_db:
        creating_db.execute(text(f"CREATE DATABASE IF NOT EXISTS {name}"))       

    engine = create_engine(f"{url}{name}")
    meta.create_all(bind=engine)
    return engine.connect()

db_name = 'storage'
db_url = 'mysql+pymysql://root:1234@localhost:3306/'

connect = db_connection(db_url, db_name)
