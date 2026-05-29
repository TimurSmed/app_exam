from sqlalchemy.orm import Session

from models.diet import DietPlan


def create_diet(db: Session, diet):
    db_diet = DietPlan(**diet.dict())

    db.add(db_diet)

    db.commit()

    db.refresh(db_diet)

    return db_diet


def get_diets(db: Session):
    return db.query(DietPlan).all()