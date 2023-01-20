from app.crud.base import CRUDBase
from app.models.submenus import Submenus
from app.schemas.submenus import SubmenusCreate, SubmenusUpdate


class CRUDMenus(CRUDBase[Submenus, SubmenusCreate, SubmenusUpdate]):
    ...


submenus = CRUDMenus(Submenus)
