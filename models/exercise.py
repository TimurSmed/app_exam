from sqlalchemy import Column, Integer, String, Text

from db.base import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    description = Column(Text)

    muscle_group = Column(String)

    difficulty = Column(String)