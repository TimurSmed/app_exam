from fastapi import FastAPI
from api.routes import exercises, workouts, diets, favorites

app = FastAPI(title = "Fitness Backend")

app.include_router(exercises.router)
app.include_router(workouts.router)
app.include_router(diets.router)
app.include_router(favorites.router)

@app.get("/")
def root():
    return {"message": "Fitness API running"}