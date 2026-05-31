from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.session import get_db
from models.exercise import Exercise
from schemas.exercise import ExerciseCreate

router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)


@router.get("/")
def get_exercises(
    db: Session = Depends(get_db)
):
    return db.query(Exercise).all()


@router.get("/{exercise_id}")
def get_exercise(
    exercise_id: int,
    db: Session = Depends(get_db)
):
    exercise = db.query(Exercise)\
        .filter(Exercise.id == exercise_id)\
        .first()

    if not exercise:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found"
        )

    return exercise


@router.post("/")
def create_exercise(
    exercise: ExerciseCreate,
    db: Session = Depends(get_db)
):
    db_exercise = Exercise(**exercise.dict())

    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)

    return db_exercise


@router.put("/{exercise_id}")
def update_exercise(
    exercise_id: int,
    exercise: ExerciseCreate,
    db: Session = Depends(get_db)
):
    db_exercise = db.query(Exercise)\
        .filter(Exercise.id == exercise_id)\
        .first()

    if not db_exercise:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found"
        )

    db_exercise.name = exercise.name
    db_exercise.description = exercise.description
    db_exercise.muscle_group = exercise.muscle_group
    db_exercise.difficulty = exercise.difficulty

    db.commit()
    db.refresh(db_exercise)

    return db_exercise


@router.get("/search")
def search_exercises(
    q: str = Query(...),
    db: Session = Depends(get_db)
):
    return db.query(Exercise)\
        .filter(Exercise.name.contains(q))\
        .all()


@router.delete("/{exercise_id}")
def delete_exercise(
    exercise_id: int,
    db: Session = Depends(get_db)
):
    exercise = db.query(Exercise)\
        .filter(Exercise.id == exercise_id)\
        .first()

    if not exercise:
        raise HTTPException(
            status_code=404,
            detail="Exercise not found"
        )

    db.delete(exercise)
    db.commit()

    return {"message": "Exercise deleted"}