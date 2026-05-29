from pydantic import BaseModel


class WorkoutCreate(BaseModel):
    title: str
    description: str
    goal_type: str
    created_by: int