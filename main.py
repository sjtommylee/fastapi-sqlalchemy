
# import package
from fastapi import FastAPI

# create an instance of fastapi
app = FastAPI()

# @app - decorator with function


@app.get('/')
def index():
    return {'data': {'name': 'Tommy'}}


@app.get('/about')
def about():
    return {'data': {'aboutpage'}}
