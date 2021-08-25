# fastapi-sqlalchemy

for educational purposes

## commands / set up

1. python3 -m venv [foldername]: creates a "node_modules" essentially.
2. source [foldername]/bin/activate: source - reads and executes commands from the file specified.
3. pip3 install fastapi uvicorn
4. uvicorn main:app --reload : main - refers to the file name, :app refers to the instance, --reload flag will "watch" changes to the files
5. you can specify the folder where you want to run uvicorn on: uivcorn [directory_name].main:app --reload

## packages

1. fastapi
2. uvicorn
3. sqlalchemy
4. psycopg2 - postgresql database adapater

## general notes

1. create_engine - pass in a conn string,
