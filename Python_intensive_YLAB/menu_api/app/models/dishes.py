from sqlalchemy import Column, Integer, Numeric, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base


class Dishes(Base):
    __tablename__ = 'dishes'
    __table_args__ = (UniqueConstraint(
        'title', name='_dish_title_uc'),)

    id = Column(Integer, primary_key=True)
    submenus_id = Column(Integer, ForeignKey(
        "submenus.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=True)
    price = Column(Numeric(8, 2), nullable=False)

    submenus = relationship('Submenus', back_populates="dishes")
