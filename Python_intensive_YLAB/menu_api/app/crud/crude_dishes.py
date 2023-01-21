from app.crud.base import CRUDBase
from app.models.dishes import Dishes
from app.schemas.dishes import DishesCreate, DishesUpdate


class CRUDMenus(CRUDBase[Dishes, DishesCreate, DishesUpdate]):
    ...


dishes = CRUDMenus(Dishes)
