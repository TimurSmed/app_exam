from sqlalchemy import Column, Integer, String

from db.base import Base


class Favorite(Base):
    __tablename__ = "favorites"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    item_type = Column(String)

    item_id = Column(Integer)