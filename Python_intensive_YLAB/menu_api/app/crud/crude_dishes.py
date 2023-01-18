from app.crud.base import CRUDBase
from app.models.dishes import Dishes
from app.schemas.dishes import DishesBaseCreate, DishesBaseUpdate


class CRUDMenus(CRUDBase[Dishes, DishesBaseCreate, DishesBaseUpdate]):
    ...


dishes = CRUDMenus(Dishes)
