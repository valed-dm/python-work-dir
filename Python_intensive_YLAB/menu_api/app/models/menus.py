from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base
from app.models.submenus import Submenus


class Menus(Base):
    __tablename__ = 'menus'
    __table_args__ = (UniqueConstraint('menus_item', name='_menus_item_uc'),)

    id = Column(Integer, primary_key=True)
    menus_item = Column(String(64), nullable=False)
    menus_description = Column(String(256), nullable=True)

    submenus = relationship(
        "Submenus", back_populates='menus', passive_deletes="True")
