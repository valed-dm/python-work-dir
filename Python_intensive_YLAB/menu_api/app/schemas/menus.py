from pydantic import BaseModel
from typing import Optional


class MenusBase(BaseModel):
    menu_item: str
    menu_description: str


class MenusCreate(MenusBase):
    pass


class MenusUpdate(MenusBase):
    pass
   

# Properties shared by models stored in DB
class MenusInDBBase(MenusBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Menus(MenusInDBBase):
    pass
