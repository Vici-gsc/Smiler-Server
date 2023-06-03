from google.cloud.sql.connector import Connector, IPTypes
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.secret import db_info


connector = Connector() 


def get_conn():
    conn = connector.connect(
            db_info['project_id'],
            "pymysql",
            user=db_info['user'],
            password=db_info['password'],
            db=db_info['database'],
            ip_type=IPTypes.PUBLIC
        )
    return conn


engine = sqlalchemy.create_engine(
    "mysql+pymysql://",
    creator=get_conn,
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
