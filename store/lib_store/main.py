from fastapi import FastAPI, HTTPException
from .database import Base, engine, SessionLocal
from .schemas import DataItemInSchema
from .models import DataItem

app = FastAPI()
Base.metadata.create_all(bind=engine)


@app.post('/data/')
async def create_data(item: DataItemInSchema):
    db = SessionLocal()
    db_item = DataItem(key=item.key, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return {'status': 'success'}


@app.get('/data/')
async def create_data():
    db = SessionLocal()
    all_items = db.query(DataItem).all()
    db.close()
    return {'items': all_items}

@app.get('/data/{key}')
async def read_data(key: str):
    db = SessionLocal()
    item = db.query(DataItem).filter(DataItem.key == key).first()
    db.close()
    if item:
        return {'key': item.key, 'value':item.value}
    raise HTTPException(status_code=404, detail='Item not found')
