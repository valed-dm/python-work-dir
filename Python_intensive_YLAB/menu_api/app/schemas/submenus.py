from pydantic import BaseModel


class SubmenusBase(BaseModel):
    title: str
    description: str


class SubmenusBaseCreate(SubmenusBase):
    title: str
    description: str
    menus_id: int

class SubmenusBaseUpdate(SubmenusBase):
    title: str


# Properties shared by models stored in DB
class SubmenusBaseInDBBase(SubmenusBase):
    id: int
    menus_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Submenus(SubmenusBaseInDBBase):
    pass


# Properties properties stored in DB
class SubmenusInDB(SubmenusBaseInDBBase):
    pass
