from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy import select, func
from sqlalchemy.orm import relationship, column_property


from app.db.base_class import Base
from app.models.submenus import Submenus


class Menus(Base):
    __tablename__ = 'menus'
    __table_args__ = (UniqueConstraint('title', name='_menus_title_uc'),)

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=True)
    submenus_counter = Column(Integer)
    dishes_counter = Column(Integer)

    submenus = relationship(
        "Submenus", back_populates='menus', passive_deletes="True")
