from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

conn_string = 'sqlite:///./blog.db'

engine = create_engine(conn_string, connect_args={"check_same_thread": False})


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
