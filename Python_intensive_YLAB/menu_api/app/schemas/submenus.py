from pydantic import BaseModel


class SubmenusBase(BaseModel):
    submenus_item: str
    submenus_description: str


class SubmenusCreate(SubmenusBase):
    pass


class SubmenusUpdate(SubmenusBase):
    pass


# Properties shared by models stored in DB
class SubmenusInDBBase(SubmenusBase):
    id: int
    menus_id: int

    class Config:
        orm_mode = True


# Properties stored in DB
class SubmenusInDB(SubmenusInDBBase):
    pass


# Properties to return to client
class Submenus(SubmenusInDBBase):
    pass
