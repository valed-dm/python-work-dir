from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base
from app.models.dishes import Dishes


class Submenus(Base):
    id = Column(Integer(), primary_key=True)
    __table_args__ = (UniqueConstraint(
        'submenu_item', name='_submenu_item_uc'),)

    submenu_item = Column(String(64), nullable=False)
    submenu_description = Column(String(256), nullable=True)
    menus_id = Column(Integer(), ForeignKey("menus.id"))
    menus = relationship('Menus', back_populates="submenus")
    dishes = relationship(Dishes, cascade="all,delete-orphan",
                          back_populates="submenus")
