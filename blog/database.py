from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
conn_string = 'sqlite:///./blog.db'

engine = create_engine(conn_string, connect_args={"check_same_thread": False})

Base = declarative_base()
