from fastapi import FastAPI, File, UploadFile
from model import Item
import pandas as pd
from db.query import si_gu_dong_ri, si_gu_dong
from db.database import SessionLocal

app = FastAPI()
db = SessionLocal()


@app.get('/')
def main() -> dict:
    return {'hello' : 'world'}

@app.get('/hello')
def hello(name: str) -> dict:
	return {'name' : name}


@app.post('/hello-body')
def hello(Item: Item):
	return Item

@app.post('/file')
def file_upload(file: UploadFile) -> dict:
    read_csv = pd.read_csv(file.file, encoding='utf-8')
    read_x = read_csv.iloc[:,4]
    read_y = read_csv.iloc[:,5]

    result = {}
    x_coordinates = []
    y_coordinates = []

    for x, y in zip(read_x, read_y):
        x_coordinates.append(x)
        y_coordinates.append(y)
        result['x'] = x_coordinates
        result['y'] = y_coordinates


    return result

@app.post('/file-convert')
def file_upload(file: UploadFile) -> list:
    read_csv = pd.read_csv(file.file, encoding='utf-8')
    read_x = read_csv.iloc[:,4]
    read_y = read_csv.iloc[:,5]

    result = []

    for x, y in zip(read_x, read_y):
        execute_query = db.execute(si_gu_dong_ri(x, y)).fetchone()
        result.append(execute_query)
        if not result:
            execute_query = db.execute(si_gu_dong(x, y)).fetchone()
            result.append(execute_query)

    return result



