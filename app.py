from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

DB_URI = 'sqlite:///data/mini.db'

Base = declarative_base()
engine = create_engine(DB_URI)