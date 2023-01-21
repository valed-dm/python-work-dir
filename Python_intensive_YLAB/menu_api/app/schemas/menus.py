from pydantic import BaseModel
from typing import Optional


class MenusBase(BaseModel):
    title: str
    description: str


class MenusCreate(MenusBase):
    pass


class MenusUpdate(MenusBase):
    pass


# Properties shared by models stored in DB
class MenusInDBBase(MenusBase):
    id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Menus(MenusInDBBase):
    pass
