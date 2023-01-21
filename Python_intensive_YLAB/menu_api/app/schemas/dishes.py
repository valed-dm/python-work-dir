from pydantic import BaseModel


class DishesBase(BaseModel):
    title: str
    description: str
    price: str


class DishesCreate(DishesBase):
    pass


class DishesUpdate(DishesBase):
    pass


# Properties shared by models stored in DB
class DishesInDBBase(DishesBase):
    id: int
    submenus_id: int

    class Config:
        orm_mode = True


# Properties properties stored in DB
class DishesInDB(DishesInDBBase):
    pass


# Properties to return to client
class Dishes(DishesInDBBase):
    pass
