from pydantic import BaseModel


class ExerciseCreate(BaseModel):
    name: str
    description: str
    muscle_group: str
    difficulty: str