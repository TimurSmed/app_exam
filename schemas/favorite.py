from pydantic import BaseModel


class FavoriteCreate(BaseModel):
    user_id: int
    item_type: str
    item_id: int