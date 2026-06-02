from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_db

from models.favorite import Favorite

from schemas.favorite import FavoriteCreate

router = APIRouter(
    prefix="/favorites",
    tags=["Favorites"]
)


@router.get("/")
def get_favorites(
    db: Session = Depends(get_db)
):
    return db.query(Favorite).all()


@router.post("/")
def create_favorite(
    favorite: FavoriteCreate,
    db: Session = Depends(get_db)
):
    db_favorite = Favorite(**favorite.dict())

    db.add(db_favorite)

    db.commit()

    db.refresh(db_favorite)

    return db_favorite


@router.delete("/{favorite_id}")
def delete_favorite(
    favorite_id: int,
    db: Session = Depends(get_db)
):
    favorite = db.query(Favorite)\
        .filter(Favorite.id == favorite_id)\
        .first()

    if not favorite:
        raise HTTPException(
            status_code=404,
            detail="Favorite not found"
        )

    db.delete(favorite)
    db.commit()

    return {"message": "Favorite deleted"}