from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
db_name = 'gis'

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@{host}:{port}/{db_name}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={"check_same_thread": False},
    pool_size=10, 
    max_overflow=20
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()