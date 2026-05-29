from sqlalchemy.orm import Session

from models.workout import WorkoutProgram


def create_workout(db: Session, workout):
    db_workout = WorkoutProgram(**workout.dict())

    db.add(db_workout)

    db.commit()

    db.refresh(db_workout)

    return db_workout


def get_workouts(db: Session):
    return db.query(WorkoutProgram).all()