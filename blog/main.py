from fastapi import FastAPI
from . import schemas
app = FastAPI()

# here we are extending the mod


@app.post('/blog')
def create(request: schemas.Blog):
    return request
