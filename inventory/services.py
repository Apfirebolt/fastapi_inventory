from datetime import datetime, timezone
from sqlalchemy.orm import Session
from inventory.model import Item
from inventory.schema import ItemCreate, ItemUpdate

def get_all_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()

def get_item_by_id(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, data: ItemCreate):
    # Generate timestamp strings to satisfy the NOT NULL database constraint
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    new_item = Item(
        title=data.title,
        quantity=data.quantity,
        created_at=now,
        updated_at=now
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

def update_item(db: Session, item_id: int, data: ItemUpdate):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return None
        
    # Update only fields that were actually provided in the request
    for key, value in data.dict(exclude_unset=True).items():
        setattr(item, key, value)
        
    # Update the timestamp
    item.updated_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return None
    db.delete(item)
    db.commit()
    return item