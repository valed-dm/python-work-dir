from pydantic import BaseModel
from typing import Optional


class MenusBase(BaseModel):
    title: str
    description: str


class MenusCreate(MenusBase):
    pass


class MenusUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties shared by models stored in DB
class MenusInDBBase(MenusBase):
    id: int
    submenus_counter: int
    dishes_counter: int

    class Config:
        orm_mode = True


# Properties stored in DB
class MenusInDB(MenusInDBBase):
    pass


# Additional properties to return via API
class Menus(MenusInDBBase):
    pass
