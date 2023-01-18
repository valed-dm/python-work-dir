from app.crud.base import CRUDBase
from app.models.menus import Menus
from app.schemas.menus import MenusCreate, MenusUpdate


class CRUDMenus(CRUDBase[Menus, MenusCreate, MenusUpdate]):
    ...


menus = CRUDMenus(Menus)
