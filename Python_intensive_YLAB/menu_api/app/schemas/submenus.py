from pydantic import BaseModel
from typing import Optional


class SubmenusBase(BaseModel):
    title: str
    description: str


class SubmenusCreate(SubmenusBase):
    pass


class SubmenusUpdate(SubmenusBase):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class SubmenusInDBBase(SubmenusBase):
    id: int
    menus_id: int
    dishes_counter: int

    class Config:
        orm_mode = True


# Properties stored in DB
class SubmenusInDB(SubmenusInDBBase):
    pass


# Properties to return to client
class Submenus(SubmenusInDBBase):
    pass
