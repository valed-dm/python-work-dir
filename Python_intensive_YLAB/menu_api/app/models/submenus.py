from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base
from app.models.dishes import Dishes


class Submenus(Base):
    __tablename__ = 'submenus'
    # __table_args__ = (UniqueConstraint(
    #     'submenus_item', name='_submenus_item_uc'),)

    id = Column(Integer, primary_key=True)
    menus_id = Column(Integer, ForeignKey(
        "menus.id", ondelete="CASCADE"), nullable=False)
    submenus_item = Column(String(64), nullable=False)
    submenus_description = Column(String(256), nullable=True)

    menus = relationship('Menus', back_populates="submenus")
    dishes = relationship(
        "Dishes", back_populates="submenus", passive_deletes="True")
