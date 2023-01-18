from app.crud.base import CRUDBase
from app.models.submenus import Submenus
from app.schemas.submenus import SubmenusBaseCreate, SubmenusBaseUpdate


class CRUDMenus(CRUDBase[Submenus, SubmenusBaseCreate, SubmenusBaseUpdate]):
    ...


submenus = CRUDMenus(Submenus)
