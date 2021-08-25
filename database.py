from sqlalchemy import create_engine
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

conn_string = 'postgresql://postgres:1126@localhost'

engine = create_engine(conn_string)
