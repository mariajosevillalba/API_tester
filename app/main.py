from fastapi import FastAPI
from .database import Base, engine
from .routes import users, tasks

app = FastAPI(
    title="Collaborative Task API",
    description="Professional API for user and task management",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(tasks.router)