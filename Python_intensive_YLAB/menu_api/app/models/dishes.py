from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base


class Dishes(Base):
    id = Column(Integer(), primary_key=True)
    __table_args__ = (UniqueConstraint(
        'dish_name', name='_dish_name_uc'),)

    dish_name = Column(String(64), nullable=False)
    dish_description = Column(String(256), nullable=True)
    dish_price = Column(Numeric(8, 2), nullable=False)
    submenus_id = Column(Integer(), ForeignKey("submenus.id"))
    submenus = relationship('Submenus', back_populates="dishes")
