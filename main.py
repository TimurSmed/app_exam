from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import exercises, workouts, diets, favorites

app = FastAPI(title="Fitness Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # разрешить любые домены
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(exercises.router)
app.include_router(workouts.router)
app.include_router(diets.router)
app.include_router(favorites.router)


@app.get("/")
def root():
    return {
        "message": "Fitness API running"
    }