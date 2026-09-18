from sqlalchemy import Column, Integer, String
from config.db import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(String(100), nullable=False)
    updated_at = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<Item(id={self.id}, title='{self.title}', quantity={self.quantity}, created_at='{self.created_at}', updated_at='{self.updated_at}')>"