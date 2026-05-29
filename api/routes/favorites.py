from fastapi import APIRouter, Depends
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