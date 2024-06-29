from fastapi import FastAPI
from init_data import init_data
from routes.characters import router as character_router
from routes.skills import router as skill_router
from routes.roles import router as role_router

app = FastAPI()

# Initialize data
init_data()

# Include routes
app.include_router(character_router)
app.include_router(skill_router)
app.include_router(role_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
