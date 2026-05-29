from pydantic import BaseModel


class DietCreate(BaseModel):
    title: str
    description: str
    goal_type: str
    created_by: int