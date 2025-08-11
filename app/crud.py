from sqlalchemy.orm import Session
from . import models, schemas

def get_items(db: Session):
    return db.query(models.Item).all()

def get_item(db: Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemCreate):
    obj = get_item(db, item_id)
    if obj:
        obj.name = item.name
        obj.description = item.description
        obj.price = item.price
        db.commit()

def delete_item(db: Session, item_id: int):
    obj = get_item(db, item_id)
    if obj:
        db.delete(obj)
        db.commit()