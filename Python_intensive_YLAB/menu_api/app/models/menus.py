from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base
from app.models.submenus import Submenus


class Menus(Base):
    __tablename__ = 'menus'
    __table_args__ = (UniqueConstraint('menu_item', name='_menu_item_uc'),)

    id = Column(Integer(), primary_key=True)
    menu_item = Column(String(64), nullable=False)
    menu_description = Column(String(256), nullable=True)
    submenus = relationship(Submenus, cascade='all,delete-orphan',
                            back_populates='menus')
