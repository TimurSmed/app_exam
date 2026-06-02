from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from db.session import get_db
from models.diet import DietPlan
from schemas.diet import DietCreate

router = APIRouter(
    prefix="/diets",
    tags=["Diets"]
)


@router.get("/")
def get_diets(
    db: Session = Depends(get_db)
):
    return db.query(DietPlan).all()


@router.get("/search")
def search_diets(
    q: str = Query(...),
    db: Session = Depends(get_db)
):
    return db.query(DietPlan)\
        .filter(DietPlan.title.contains(q))\
        .all()


@router.get("/user/{user_id}")
def get_user_diets(
    user_id: int,
    db: Session = Depends(get_db)
):
    return db.query(DietPlan)\
        .filter(DietPlan.created_by == user_id)\
        .all()



@router.get("/{diet_id}")
def get_diet(
    diet_id: int,
    db: Session = Depends(get_db)
):
    diet = db.query(DietPlan)\
        .filter(DietPlan.id == diet_id)\
        .first()

    if not diet:
        raise HTTPException(
            status_code=404,
            detail="Diet not found"
        )

    return diet



@router.post("/")
def create_diet(
    diet: DietCreate,
    db: Session = Depends(get_db)
):
    db_diet = DietPlan(**diet.dict())

    db.add(db_diet)
    db.commit()
    db.refresh(db_diet)

    return db_diet


@router.put("/{diet_id}")
def update_diet(
    diet_id: int,
    diet: DietCreate,
    db: Session = Depends(get_db)
):
    db_diet = db.query(DietPlan)\
        .filter(DietPlan.id == diet_id)\
        .first()

    if not db_diet:
        raise HTTPException(
            status_code=404,
            detail="Diet not found"
        )

    db_diet.title = diet.title
    db_diet.description = diet.description
    db_diet.goal_type = diet.goal_type
    db_diet.created_by = diet.created_by

    db.commit()
    db.refresh(db_diet)

    return db_diet



@router.delete("/{diet_id}")
def delete_diet(
    diet_id: int,
    db: Session = Depends(get_db)
):
    diet = db.query(DietPlan)\
        .filter(DietPlan.id == diet_id)\
        .first()

    if not diet:
        raise HTTPException(
            status_code=404,
            detail="Diet not found"
        )

    db.delete(diet)
    db.commit()

    return {"message": "Diet deleted"}