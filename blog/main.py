from fastapi import FastAPI
from . import schemas
from .database import engine
from . import models
app = FastAPI()

models.Base.metadata.create_all(engine)


@app.post('/blog')
def create(request: schemas.Blog):
    return request
