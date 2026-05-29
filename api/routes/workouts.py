from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db

from models.workout import WorkoutProgram

from schemas.workout import WorkoutCreate

router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)


@router.get("/")
def get_workouts(
    db: Session = Depends(get_db)
):
    return db.query(WorkoutProgram).all()


@router.get("/user/{user_id}")
def get_user_workouts(
    user_id: int,
    db: Session = Depends(get_db)
):
    return db.query(WorkoutProgram)\
        .filter(WorkoutProgram.created_by == user_id)\
        .all()


@router.post("/")
def create_workout(
    workout: WorkoutCreate,
    db: Session = Depends(get_db)
):
    db_workout = WorkoutProgram(**workout.dict())

    db.add(db_workout)

    db.commit()

    db.refresh(db_workout)

    return db_workout


@router.delete("/{workout_id}")
def delete_workout(
    workout_id: int,
    db: Session = Depends(get_db)
):
    workout = db.query(WorkoutProgram)\
        .filter(WorkoutProgram.id == workout_id)\
        .first()

    if not workout:
        raise HTTPException(
            status_code=404,
            detail="Workout not found"
        )

    db.delete(workout)

    db.commit()

    return {"message": "Workout deleted"}