
# import package
from typing import Optional
from fastapi import FastAPI
# create an instance of fastapi
app = FastAPI()

# @app - decorator with function

# '/' is the path, there are multiple "methods" we can specifiy with the decorator. "GET" is the operation.
# function that is defined after the decorator is the "path operation function"


@app.get('/blog')
# we can set default values for the function parameters
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    # we can use a f string - same as a string interpolation
    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return {'data': f'{limit} blogs from the db'}


# you can specify the type of the return, kinda like typescript
@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/unpublished')
def unpublished_blog():
    return {'data': 'all unpublished blogs'}


@app.get('/blog/{id}/comments')
def comments(id: int):
    # fetch comments of blog with id = id
    return {'data': {'1', '2'}}


@app.post('/blog')
def create_blog():
    return {'data': "blog is created"}
