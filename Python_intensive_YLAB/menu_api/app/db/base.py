# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.menus import Menus  # noqa
from app.models.submenus import Submenus  # noqa
from app.models.dishes import Dishes  # noqa
