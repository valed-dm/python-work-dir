from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship


from app.db.base_class import Base


class Submenus(Base):
    __tablename__ = 'submenus'
    __table_args__ = (UniqueConstraint(
        'title', name='_submenus_title_uc'),)

    id = Column(Integer, primary_key=True)
    menus_id = Column(Integer, ForeignKey(
        "menus.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(64), nullable=False)
    description = Column(String(256), nullable=True)
    dishes_counter = Column(Integer)

    menus = relationship('Menus', back_populates="submenus")
    dishes = relationship(
        "Dishes", back_populates="submenus", passive_deletes="True")
