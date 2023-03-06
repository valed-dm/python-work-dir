from pydantic import BaseModel
from typing import Optional


class DishesBase(BaseModel):
    title: str
    description: str
    price: str


class DishesCreate(DishesBase):
    pass


class DishesUpdate(DishesBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None


# Properties shared by models stored in DB
class DishesInDBBase(DishesBase):
    id: int
    submenus_id: int

    class Config:
        orm_mode = True


# Properties stored in DB
class DishesInDB(DishesInDBBase):
    pass


# Properties to return to client
class Dishes(DishesInDBBase):
    pass
