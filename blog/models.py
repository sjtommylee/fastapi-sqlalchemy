from sqlalchemy import Column, Integer, String
from blog.database import Base

# defining our model.


class Blog (Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
