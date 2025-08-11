from pydantic import BaseModel
from typing import Optional

# Entrada
class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# Saída
class ItemOut(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
