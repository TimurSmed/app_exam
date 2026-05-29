from sqlalchemy import Column, Integer, String, Text

from db.base import Base


class WorkoutProgram(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text)

    goal_type = Column(String)

    created_by = Column(Integer)