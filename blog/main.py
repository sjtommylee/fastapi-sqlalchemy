from fastapi import FastAPI
from . import schemas
from . import database
from . import models
app = FastAPI()


@app.post('/blog')
def create(request: schemas.Blog):
    return request
