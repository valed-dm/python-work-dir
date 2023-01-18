from pydantic import BaseModel


class DishesBase(BaseModel):
    title: str
    description: str


class DishesBaseCreate(DishesBase):
    title: str
    description: str
    submenus_id: int

class DishesBaseUpdate(DishesBase):
    title: str


# Properties shared by models stored in DB
class DishesBaseInDBBase(DishesBase):
    id: int
    submenus_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class Dishes(DishesBaseInDBBase):
    pass


# Properties properties stored in DB
class DishesInDB(DishesBaseInDBBase):
    pass
